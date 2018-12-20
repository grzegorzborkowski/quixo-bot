import random
import numpy as np
from enum import Enum
from collections import namedtuple
import random
import math
from functools import cmp_to_key
from abc import ABC, abstractmethod
import copy

EMPTY_FIELD =  ' '
O_MARK = 'O'
X_MARK = 'X'

PUSH_UP = 'PUSH_UP'
PUSH_DOWN = 'PUSH_DOWN'
PUSH_LEFT = 'PUSH_LEFT'
PUSH_RIGHT = 'PUSH_RIGHT'

Move = namedtuple('Move', ['player_mark', 'x', 'y', 'direction'])

class BorderFieldPossibleMoves(Enum):
    LEFT_TOP_CORNER = 0
    LEFT_BOTTOM_CORNER = 1
    RIGHT_TOP_CORNER = 2
    RIGHT_BOTTOM_CORNER = 3
    TOP_ROW = 4
    BOTTOM_ROW = 5
    LEFT_COLUMN = 6
    RIGHT_COLUMN = 7

class AbstractPlayer(ABC):

    def __init__(self):
        self.max_iteration_number = None
        self.mark = None
        self.gameField = None
        self.is_disqualified = False
        self.has_game_ended = None
        self.has_won = None
        self.possible_moves = {
            BorderFieldPossibleMoves.LEFT_TOP_CORNER : [PUSH_UP, PUSH_LEFT],
            BorderFieldPossibleMoves.LEFT_BOTTOM_CORNER : [PUSH_DOWN, PUSH_LEFT],
            BorderFieldPossibleMoves.RIGHT_TOP_CORNER : [PUSH_UP, PUSH_RIGHT],
            BorderFieldPossibleMoves.RIGHT_BOTTOM_CORNER : [PUSH_DOWN, PUSH_RIGHT],
            BorderFieldPossibleMoves.TOP_ROW : [PUSH_UP, PUSH_LEFT, PUSH_RIGHT],
            BorderFieldPossibleMoves.BOTTOM_ROW : [PUSH_DOWN, PUSH_LEFT, PUSH_RIGHT],
            BorderFieldPossibleMoves.LEFT_COLUMN : [PUSH_UP, PUSH_DOWN, PUSH_LEFT],
            BorderFieldPossibleMoves.RIGHT_COLUMN : [PUSH_UP, PUSH_DOWN, PUSH_RIGHT]
        }

    def setMaxIterationNumber(self, maxNumber):
        self.max_iteration_number = maxNumber

    def setTypeOfAssignedMark(self, mark):
        self.mark = mark

    def setStateOfGameField(self, gameField):
        self.gameField = np.array(gameField)

    def setInformationAboutDisqualification(self, info):
        self.is_disqualified = info

    def setInformationAboutGameEnd(self, info):
        self.has_game_ended = info

    def setInformationAboutWinning(self, info):
        self.has_won = info

    @abstractmethod
    def makeMove(self):
        possible_moves = list(self.__findAllPosibleMoves__())
        return random.choice(possible_moves)

    def __findAllPosibleMovesForGivenBorder__(self, border, mark_to_return):
        all_possible_border_fields = self.allPossibleBorderFieldsForBorder(border, mark_to_return)
        for posible_border_field in all_possible_border_fields:
            position = self.getPositionBasedOnCoordinates(posible_border_field[0], posible_border_field[1])
            possible_moves_for_position = self.possible_moves[position]
            for possible_move in possible_moves_for_position:
                yield Move(mark_to_return, posible_border_field[0], posible_border_field[1], possible_move)

    # REFACTOR
    def allPossibleBorderFieldsForBorder(self, border, mark_to_return):
        rows, columns = border.shape[0], border.shape[1]
        for x in range (rows):
            for y in range (columns):
                if x == 0 or y == 0 or x == rows-1 or y == rows-1:
                    if border[y][x] == EMPTY_FIELD or border[y][x] == mark_to_return:
                        yield (x, y, border[y][x])


    def __findAllPosibleMoves__(self):
        all_possible_border_fields = self.allPossibleBorderFields()
        for posible_border_field in all_possible_border_fields:
            position = self.getPositionBasedOnCoordinates(posible_border_field[1], posible_border_field[0])
            possible_moves_for_position = self.possible_moves[position]
            for possible_move in possible_moves_for_position:
                yield Move(self.mark, posible_border_field[0], posible_border_field[1], possible_move)

    def allPossibleBorderFields(self):
        rows, columns = self.gameField.shape[0], self.gameField.shape[1]
        for x in range (rows):
            for y in range (columns):
                if x == 0 or y == 0 or x == rows-1 or y == rows-1:
                    if self.gameField[y][x] == EMPTY_FIELD or self.gameField[y][x] == self.mark:
                        yield (x, y, self.gameField[y][x])

    def getPositionBasedOnCoordinates(self, x, y):
        x_last = self.gameField.shape[1]-1
        y_last = self.gameField.shape[0]-1
        if x == 0 and y == 0:
            return BorderFieldPossibleMoves.LEFT_TOP_CORNER
        elif x == x_last and y == 0:
            return BorderFieldPossibleMoves.LEFT_BOTTOM_CORNER
        elif x == 0 and y == y_last:
            return BorderFieldPossibleMoves.RIGHT_TOP_CORNER
        elif x == x_last and y == y_last:
            return BorderFieldPossibleMoves.RIGHT_BOTTOM_CORNER
        elif x == 0:
            return BorderFieldPossibleMoves.TOP_ROW
        elif x == x_last:
            return BorderFieldPossibleMoves.BOTTOM_ROW
        elif y == 0:
            return BorderFieldPossibleMoves.LEFT_COLUMN
        elif y == y_last:
            return BorderFieldPossibleMoves.RIGHT_COLUMN

    def simulate_state_after_move(self, board, move):
        x, y, direction = move[1], move[2], move[3]
        current_state = copy.deepcopy(board)
        current_state[y][x] = move.player_mark

        if direction == PUSH_RIGHT:
            if y==0:
                current_state[x] = np.roll(current_state[x], shift=-1)
            else:
                for i in range (y, len(current_state[x])-1):
                    current_state[x][i] = current_state[x][i+1]
                current_state[x][len(current_state[x])-1] = move.player_mark

        elif direction == PUSH_LEFT:
            if y==len(current_state[x])-1:
                current_state[x] = np.roll(current_state[x], shift=1)
            else:
                for i in reversed(range(1,y+1)):
                    current_state[x][i] = current_state[x][i-1]
                current_state[x][0] = move.player_mark

        elif direction == PUSH_UP:
            if x == len(current_state)-1:
                 current_state[:, y] = np.roll(current_state[:, y], shift=1)
            else:
                for i in reversed(range(1,x+1)):
                    current_state[i][y] = current_state[i-1][y]
                current_state[0][y] = move.player_mark

        else:
            if x == 0:
                current_state[:, y] = np.roll(current_state[:, y], shift=-1)
            else:
                for i in range(x, len(current_state)-1):
                    current_state[i][y] = current_state[i+1][y]
                current_state[len(current_state)-1][y] = move.player_mark

        return current_state

    def number_of_mark_on_axis(self, axis):
        number_of_X, number_of_O = 0, 0
        for x in np.nditer(axis):
            if x == X_MARK:
                number_of_X += 1
            elif x == O_MARK:
                number_of_O += 1
        return (number_of_X, number_of_O)

    def number_of_mark_on_diagonal(self, axis):
        number_of_X, number_of_O = 0, 0
        for x in axis:
            if x == X_MARK:
                number_of_X += 1
            elif x == O_MARK:
                number_of_O += 1
        return (number_of_X, number_of_O)


    def check_winning_condition_for_axis(self, rows_or_columns_or_diagonals, mark):
        x_limit = self.gameField.shape[0]
        y_limit = self.gameField.shape[1]
        for row_result in rows_or_columns_or_diagonals:
            if mark == X_MARK and row_result[0] == x_limit: return True
            elif mark == O_MARK and row_result[1] == x_limit: return True
        return False

    def check_if_player_won_row(self, current_state, mark):
        x_limit, y_limit = self.gameField.shape[0], self.gameField.shape[1]
        for i in range (0, x_limit):
            column, mark_result = current_state[i], 0
            for el in column:
                if el == mark:
                   mark_result += 1
            if mark_result == x_limit:
                return True
        return False

    def check_if_player_won_column(self, current_state, mark):
        x_limit, y_limit = self.gameField.shape[0], self.gameField.shape[1]
        for i in range (0, y_limit):
            column = current_state[:, i]
            mark_result = 0
            for el in column:
                if el == mark:
                   mark_result += 1
            if mark_result == y_limit:
                return True
        return False

    def check_if_player_won_diagonal(self, current_state, mark):
        x_limit = self.gameField.shape[0]
        y_limit = self.gameField.shape[1]
        first_diagonal, second_diagonal = current_state.diagonal(), np.fliplr(current_state).diagonal()
        marks_on_first_diagonal, marks_on_second_diagonal = self.number_of_mark_on_diagonal(first_diagonal), self.number_of_mark_on_diagonal(second_diagonal)
        if mark == X_MARK and (marks_on_first_diagonal[0] == x_limit or marks_on_second_diagonal[0] == x_limit):
            return True
        if mark == O_MARK and (marks_on_first_diagonal[1] == x_limit or marks_on_second_diagonal[1] == x_limit):
            return True
        return False

    def check_if_player_won(self, current_state, mark):
        return self.check_if_player_won_column(current_state, mark) or self.check_if_player_won_row(current_state, mark) or self.check_if_player_won_diagonal(current_state, mark)


class Player(AbstractPlayer):

    def __init__(self):
        super().__init__()

    def makeMove(self):
        return self.findBestMove()

    def findBestMove(self):
        bestValue = -1000
        bestMove = None
        possible_moves = list(self.__findAllPosibleMoves__())
        foundAnyMoveWithoutPruning = False

        possible_moves = self.shuffle_possible_moves(possible_moves, self.gameField)
        bestMove = possible_moves[0]
        for move in possible_moves:
            board = self.simulate_state_after_move(self.gameField, move)
            evaluation = self.minimax(board, 0, False, -1000, 1000)
            if evaluation[1] and foundAnyMoveWithoutPruning:
                bestMove = move
                bestValue = evaluation[0]
            elif evaluation[0] > bestValue:
                bestMove = move
                bestValue = evaluation[0]
        return bestMove

    def evaluate_board(self, board):
        return self.score_for_board(board)

    def score_for_board(self, board):
        x_limit = self.gameField.shape[0]
        y_limit = self.gameField.shape[1]
        result_for_board = 0

        rows = []
        columns = []
        x_limit = self.gameField.shape[0]
        y_limit = self.gameField.shape[1]
        for i in range (0, x_limit):
            row = board[i]
            O_MARK_res, X_MARK_res = 0, 0
            for el in row:
                if el == O_MARK:
                    O_MARK_res += 1
                if el == X_MARK:
                    X_MARK_res += 1
                if O_MARK_res == y_limit:
                    return (500, True)
                if X_MARK_res == y_limit:
                    return (-500, True)
            rows.append((O_MARK, X_MARK))

        for i in range (0, y_limit):
            column = board[:, i]
            O_MARK_res, X_MARK_res = 0, 0
            for el in column:
                if el == O_MARK:
                    O_MARK_res += 1
                if el == X_MARK:
                    X_MARK_res += 1
                if O_MARK_res == y_limit:
                    return (500, True)
                if X_MARK_res == y_limit:
                    return (-500, True)
            columns.append((O_MARK, X_MARK))

        for row_result in rows:
            if row_result[0] == x_limit-1: result_for_board -= 50
            elif row_result[0] == x_limit-2: result_for_board -= 20
            if row_result[1] == x_limit-1: result_for_board += 50
            if row_result[1] == x_limit-2: result_for_board += 20
        for row_result in columns:
            if row_result[0] == x_limit-1: result_for_board -= 50
            elif row_result[0] == x_limit-2: result_for_board -= 20
            if row_result[1] == x_limit-1: result_for_board += 50
            elif row_result[1] == x_limit-2: result_for_board -= 20
        return (result_for_board, None)

    def is_draw(self, board):
        return False

    def shuffle_possible_moves(self, moves, board):
        moves = sorted(moves, key = cmp_to_key(lambda move1, move2: 1 if board[move1[1]][move1[2]] == EMPTY_FIELD else -1))
        return moves

    def minimax(self, board, depth, isMaximizingPlayer, alpha, beta):
        board_value = self.evaluate_board(board)
        if board_value[1] is not None:
            if board_value[1] == self.mark: #
                return (board_value[0] - depth*25, False)
            else:
                return (depth*25 - board_value[0], False)

        if self.is_draw(board):
            return (250, False)
        if depth > 1:
            return (board_value[0], True)
        if self.mark == O_MARK and isMaximizingPlayer:
            mark = O_MARK
        elif self.mark == O_MARK:
            mark = X_MARK
        if self.mark == X_MARK and isMaximizingPlayer:
            mark = X_MARK
        else:
            mark = X_MARK
        possibleMoves = list(self.__findAllPosibleMovesForGivenBorder__(board, mark))
        possibleMoves = self.shuffle_possible_moves(possibleMoves, board)

        if isMaximizingPlayer:
            bestValue = -1000
            for move in possibleMoves:
                new_state = self.simulate_state_after_move(board, move)
                value = self.minimax(new_state, depth+1, False, alpha, beta)[0]
                bestValue = max(bestValue, value)
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    break
            return (bestValue, False)

        else:
            bestValue = 1000
            for move in possibleMoves:

                new_state = self.simulate_state_after_move(board, move)
                value = self.minimax(new_state, depth+1, True, alpha, beta)[0]
                bestValue = min(bestValue, value)
                beta = min(beta, bestValue)
                if beta <= alpha:
                    break
            return (bestValue, False)
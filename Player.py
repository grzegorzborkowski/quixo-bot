import random
import numpy as np
from enum import Enum
from collections import namedtuple
import random

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

class Player:

    def __init__(self):
        self.max_iteration_number = None
        self.mark = None
        self.gameField = None
        self.is_disqualified = False
        self.has_game_ended = None
        self.has_won = None
        self.possible_moves = {
            BorderFieldPossibleMoves.LEFT_TOP_CORNER : [PUSH_DOWN, PUSH_RIGHT],
            BorderFieldPossibleMoves.LEFT_BOTTOM_CORNER : [PUSH_UP, PUSH_RIGHT],
            BorderFieldPossibleMoves.RIGHT_TOP_CORNER : [PUSH_DOWN, PUSH_LEFT],
            BorderFieldPossibleMoves.RIGHT_BOTTOM_CORNER : [PUSH_UP, PUSH_LEFT],
            BorderFieldPossibleMoves.TOP_ROW : [PUSH_DOWN, PUSH_LEFT, PUSH_RIGHT],
            BorderFieldPossibleMoves.BOTTOM_ROW : [PUSH_UP, PUSH_LEFT, PUSH_RIGHT],
            BorderFieldPossibleMoves.LEFT_COLUMN : [PUSH_UP, PUSH_DOWN, PUSH_RIGHT],
            BorderFieldPossibleMoves.RIGHT_COLUMN : [PUSH_UP, PUSH_DOWN, PUSH_LEFT]
        }
    
    def setMaxIterationNumber(self, maxNumber):
        self.max_iteration_number = maxNumber

    def setTypeOfAssignedMark(self, mark):
        self.mark = mark

    def setStateOfGameField(self, gameField):
        self.gameField = gameField

    def setInformationAboutDisqualification(self, info):
        self.is_disqualified = info

    def setInformationAboutGameEnd(self, info):
        self.has_game_ended = info

    def setInformationAboutWinning(self, info):
        self.has_won = info

    def makeMove(self):
        possible_moves = list(self.__findAllPosibleMoves__())
        return random.choice(possible_moves)

    
    def __findAllPosibleMoves__(self):
        all_possible_border_fields = self.allPossibleBorderFields()
        for posible_border_field in all_possible_border_fields:
            position = self.getPositionBasedOnCoordinates(posible_border_field[0], posible_border_field[1])
            possible_moves_for_position = self.possible_moves[position]
            for possible_move in possible_moves_for_position:
                yield Move(self.mark, posible_border_field[0], posible_border_field[1], possible_move)

    def allPossibleBorderFields(self):
        rows, columns = self.gameField.shape[0], self.gameField.shape[1]
        for x in range (rows):
            for y in range (columns):
                if x == 0 or y == 0 or x == rows-1 or y == rows-1:
                    if self.gameField[x][y] == EMPTY_FIELD or self.gameField[x][y] == self.mark:
                        yield (x, y, self.gameField[x][y])

    def getPositionBasedOnCoordinates(self, x, y, x_limit = 4, y_limit = 4):
        if x == 0 and y == 0:
            return BorderFieldPossibleMoves.LEFT_TOP_CORNER
        elif x == x_limit and y == 0:
            return BorderFieldPossibleMoves.LEFT_BOTTOM_CORNER
        elif x == 0 and y == y_limit:
            return BorderFieldPossibleMoves.RIGHT_TOP_CORNER
        elif x == x_limit and y == y_limit:
            return BorderFieldPossibleMoves.RIGHT_BOTTOM_CORNER
        elif x == 0:
            return BorderFieldPossibleMoves.TOP_ROW
        elif x == x_limit:
            return BorderFieldPossibleMoves.BOTTOM_ROW
        elif y == 0:
            return BorderFieldPossibleMoves.LEFT_COLUMN
        else:
            return BorderFieldPossibleMoves.RIGHT_COLUMN

    def simulate_state_after_move(self, current_state, move):
        x, y, direction = move[1], move[2], move[3]
        current_state[x][y] = move.player_mark
        
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
        for row_result in rows_or_columns_or_diagonals:
            if mark == X_MARK and row_result[0] == 5: return True
            elif mark == O_MARK and row_result[1] == 5: return True
        return False

    def check_if_player_won_row(self, current_state, mark):
        result = np.apply_along_axis(self.number_of_mark_on_axis, axis=1, arr=current_state)
        return self.check_winning_condition_for_axis(result, mark)

    def check_if_player_won_column(self, current_state, mark):
        result = np.apply_along_axis(self.number_of_mark_on_axis, axis=0, arr=current_state)
        return self.check_winning_condition_for_axis(result, mark)

    def check_if_player_won_diagonal(self, current_state, mark):
        first_diagonal, second_diagonal = current_state.diagonal(), np.fliplr(current_state).diagonal()
        marks_on_first_diagonal, marks_on_second_diagonal = self.number_of_mark_on_diagonal(first_diagonal), self.number_of_mark_on_diagonal(second_diagonal)
        if mark == X_MARK and (marks_on_first_diagonal[0] == 5 or marks_on_second_diagonal[0] == 5):
            return True
        if mark == O_MARK and (marks_on_first_diagonal[1] == 5 or marks_on_second_diagonal[1] == 5):
            return True
        return False

    def check_if_player_won(self, current_state, mark):
        return self.check_if_player_won_column(current_state, mark) or self.check_if_player_won_row(current_state, mark) or self.check_if_player_won_diagonal(current_state, mark)

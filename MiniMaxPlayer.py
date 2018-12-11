import random
import numpy as np
from enum import Enum
from collections import namedtuple
import random
from AbstractPlayer import *
import math
from functools import cmp_to_key

class Player(AbstractPlayer):

    def __init__(self):
        super().__init__()  
    
    def makeMove(self):
        return self.findBestMove()

    def findBestMove(self):
        bestValue = -1000
        bestMove = None
        possible_moves = list(self.__findAllPosibleMoves__())

        possible_moves = self.shuffle_possible_moves(possible_moves, self.gameField)
        for move in possible_moves:
            board = self.simulate_state_after_move(self.gameField, move)
            evaluation = self.minimax(board, 0, False, -1000, 1000)
            if evaluation > bestValue:
                bestMove = move
                bestValue = evaluation
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
        moves = sorted(moves, key = cmp_to_key(lambda move1, move2: -1 if board[move1[1]][move1[2]] == EMPTY_FIELD else 1))
        return moves

    def minimax(self, board, depth, isMaximizingPlayer, alpha, beta):
        board_value = self.evaluate_board(board)
        if board_value[1] is not None:
            if board_value[1] == self.mark: #
                return board_value[0] - depth*25
            else:
                return depth*25 - board_value[0]
        
        if self.is_draw(board):
            return 250
        if depth > 3:
            return board_value[0]

        mark = O_MARK if isMaximizingPlayer else X_MARK
        possibleMoves = list(self.__findAllPosibleMovesForGivenBorder__(board, mark))
        possibleMoves = self.shuffle_possible_moves(possibleMoves, board)
      
        if isMaximizingPlayer:
            bestValue = -1000
            for move in possibleMoves:
                new_state = self.simulate_state_after_move(board, move)
                value = self.minimax(new_state, depth+1, False, alpha, beta)
                bestValue = max(bestValue, value)
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    break
            return bestValue
        
        else:
            bestValue = 1000
            for move in possibleMoves:

                new_state = self.simulate_state_after_move(board, move)
                value = self.minimax(new_state, depth+1, True, alpha, beta)
                bestValue = min(bestValue, value)
                beta = min(beta, bestValue)
                if beta <= alpha:
                    break
            return bestValue

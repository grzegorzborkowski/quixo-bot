import random
import numpy as np
from enum import Enum
from collections import namedtuple

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
        pass
    
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
        pass

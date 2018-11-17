import random
import numpy as np
from enum import Enum

EMPTY_FIELD =  ' '
O_MARK = 'O'
X_MARK = 'X'

PUSH_UP = 'PUSH_UP' 
PUSH_DOWN = 'PUSH_DOWN'
PUSH_LEFT = 'PUSH_LEFT'
PUSH_RIGHT = 'PUSH_RIGHT'

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
        pass

    def allPossibleBorderFields(self):
        rows, columns = self.gameField.shape[0], self.gameField.shape[1]
        for x in range (rows):
            for y in range (columns):
                if x == 0 or y == 0 or x == rows-1 or y == rows-1:
                    if self.gameField[x][y] == EMPTY_FIELD or self.gameField[x][y] == self.mark:
                        yield (x, y, self.gameField[x][y])


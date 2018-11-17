import random
import numpy as np


EMPTY_FIELD =  ' '
O_MARK = 'O'
X_MARK = 'X'

class Player:

    def __init__(self):
        self.max_iteration_number = None
        self.mark = None
        self.gameField = None
        self.is_disqualified = False
        self.has_game_ended = None
        self.has_won = None

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

    
    

    

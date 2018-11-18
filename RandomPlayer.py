import random
import numpy as np
from enum import Enum
from collections import namedtuple
import random
from AbstractPlayer import *

class RandomPlayer(AbstractPlayer):

    def __init__(self):
        super().__init__()  
    
    def makeMove(self):
        possible_moves = list(self.__findAllPosibleMoves__())
        return random.choice(possible_moves)
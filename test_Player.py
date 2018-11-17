import unittest
from Player import *
import numpy as np

class TestStateMethods(unittest.TestCase):

     def test_check_return_border_fields_correctly(self):
        player = Player()
        player.setTypeOfAssignedMark(O_MARK)
        player.setStateOfGameField(
           np.array([['X', 'O', ' ', ' ', 'X'], 
                ['X', 'O', ' ', ' ', 'X'], 
                ['X', 'O', ' ', ' ', 'X'], 
                ['X', 'O', ' ', ' ', 'X'], 
                ['X', 'O', ' ', ' ', 'X']]),
        )
        border_fields = list(player.allPossibleBorderFields())
        print (border_fields)
        expected = [(0, 1, O_MARK),(0, 2, EMPTY_FIELD), (0, 3, EMPTY_FIELD), (4, 1, O_MARK), (4,2, EMPTY_FIELD), (4,3, EMPTY_FIELD)]
        self.assertSequenceEqual(border_fields, expected)

    
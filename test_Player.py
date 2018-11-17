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
        expected = [(0, 1, O_MARK),(0, 2, EMPTY_FIELD), (0, 3, EMPTY_FIELD), (4, 1, O_MARK), (4,2, EMPTY_FIELD), (4,3, EMPTY_FIELD)]
        self.assertSequenceEqual(border_fields, expected)

    def test_get_position_based_on_coordinates(self):
        player = Player()
        player.setTypeOfAssignedMark(X_MARK)
        player.setStateOfGameField(
           np.array([
                ['X', 'O', 'O', ' ', 'X'], 
                ['O', 'O', ' ', ' ', 'O'], 
                ['O', 'O', ' ', ' ', 'O'], 
                [' ', 'O', ' ', ' ', ' '], 
                ['X', 'O', 'O', ' ', 'X']]),
        )
        border_fields = list(player.allPossibleBorderFields())
        field_position = list(map(lambda field : player.getPositionBasedOnCoordinates(field[0], field[1]),
                            border_fields))
        zipped = list(zip(border_fields, field_position))
        expected = [((0, 0, X_MARK), BorderFieldPossibleMoves.LEFT_TOP_CORNER),
                    ((0, 3, EMPTY_FIELD), BorderFieldPossibleMoves.TOP_ROW),
                    ((0, 4, X_MARK), BorderFieldPossibleMoves.RIGHT_TOP_CORNER),
                    ((3, 0, EMPTY_FIELD), BorderFieldPossibleMoves.LEFT_COLUMN),
                    ((3, 4, EMPTY_FIELD), BorderFieldPossibleMoves.RIGHT_COLUMN),
                    ((4, 0, X_MARK), BorderFieldPossibleMoves.LEFT_BOTTOM_CORNER),
                    ((4, 3, EMPTY_FIELD), BorderFieldPossibleMoves.BOTTOM_ROW),
                    ((4, 4, X_MARK), BorderFieldPossibleMoves.RIGHT_BOTTOM_CORNER)]
        self.assertSequenceEqual(zipped, expected)

    def test_simulate_state_after_move_push_right(self):
        player = Player()
        player.setTypeOfAssignedMark(X_MARK)
        player.setStateOfGameField(
           np.array([
                [' ', ' ', ' ', ' ', 'X'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']]))
        move = Move(X_MARK, 0, 4, PUSH_LEFT)
        new_state = player.simulate_state_after_move(player.gameField, move)
        print (new_state)
        self.assertTrue(False)
    
    def test_simulate_state_after_move_push_left(self):
        self.assertTrue(False)
    
    def test_simulate_state_after_move_push_up(self):
        self.assertTrue(False)

    def test_simulate_state_after_move_push_down(self):
        self.assertTrue(False)

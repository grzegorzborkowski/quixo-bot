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
        move = Move(X_MARK, 0, 0, PUSH_RIGHT)

        expected = np.array([
                [' ', ' ', ' ', 'X', 'X'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']])
        new_state = player.simulate_state_after_move(player.gameField, move)
        self.assertTrue(np.array_equal(expected, new_state))

    def test_simulate_state_after_move_push_right_2(self):
        player = Player()
        player.setTypeOfAssignedMark(X_MARK)
        player.setStateOfGameField(
           np.array([
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', 'O', 'X', 'X', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']]))
        move = Move(X_MARK, 2, 0, PUSH_RIGHT)
        expected = np.array([
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                ['O', 'X', 'X', ' ', 'X'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']])
        new_state = player.simulate_state_after_move(player.gameField, move)
        self.assertTrue(np.array_equal(expected, new_state))
    
    def test_simulate_state_after_move_push_right_3(self):
        player = Player()
        player.setTypeOfAssignedMark(X_MARK)
        player.setStateOfGameField(
           np.array([
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                ['X', 'O', 'X', 'X', 'O'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']]))
        move = Move(X_MARK, 2, 0, PUSH_RIGHT)
        expected = np.array([
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                ['O', 'X', 'X', 'O', 'X'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']])
        new_state = player.simulate_state_after_move(player.gameField, move)
        self.assertTrue(np.array_equal(expected, new_state))

    def test_simulate_state_after_move_push_left(self):
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

        expected = np.array([
                ['X', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']])
        new_state = player.simulate_state_after_move(player.gameField, move)
        self.assertTrue(np.array_equal(expected, new_state))

    def test_simulate_state_after_move_push_left_2(self):
        player = Player()
        player.setTypeOfAssignedMark(X_MARK)
        player.setStateOfGameField(
           np.array([
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                ['X', ' ', 'X', 'X', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']]))
        move = Move(X_MARK, 2, 4, PUSH_LEFT)

        expected = np.array([
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                ['X', 'X', ' ', 'X', 'X'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']])
        new_state = player.simulate_state_after_move(player.gameField, move)
        self.assertTrue(np.array_equal(expected, new_state))

    def test_simulate_state_after_move_push_left_3(self):
        player = Player()
        player.setTypeOfAssignedMark(X_MARK)
        player.setStateOfGameField(
           np.array([
                [' ', ' ', 'X', 'O', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                ['X', ' ', 'X', 'X', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']]))
        move = Move(X_MARK, 0, 2, PUSH_LEFT)

        expected = np.array([
                ['X', ' ', ' ', ' ', 'O'], 
                [' ', ' ', ' ', ' ', ' '], 
                ['X', ' ', 'X', 'X', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']])
        new_state = player.simulate_state_after_move(player.gameField, move)
        self.assertTrue(np.array_equal(expected, new_state))

    def test_simulate_state_after_move_push_up(self):
        player = Player()
        player.setTypeOfAssignedMark(X_MARK)
        player.setStateOfGameField(
           np.array([
                [' ', ' ', ' ', ' ', 'X'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', 'X', ' '], 
                [' ', ' ', ' ', 'O', ' '], 
                [' ', ' ', ' ', ' ', ' ']]))
        move = Move(X_MARK, 4, 3, PUSH_UP)

        expected = np.array([
                [' ', ' ', ' ', 'X', 'X'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', 'X', ' '], 
                [' ', ' ', ' ', 'O', ' ']])
        new_state = player.simulate_state_after_move(player.gameField, move)
        print ("STATE",)
        print(new_state)
        print()
        print ("EXPECTED", expected)
        self.assertTrue(np.array_equal(expected, new_state))

    def test_simulate_state_after_move_push_down(self):
        player = Player()
        player.setTypeOfAssignedMark(X_MARK)
        player.setStateOfGameField(
           np.array([
                [' ', ' ', ' ', ' ', 'X'], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', 'X', ' '], 
                [' ', ' ', ' ', 'O', ' '], 
                [' ', ' ', ' ', ' ', ' ']]))
        move = Move(X_MARK, 0, 3, PUSH_DOWN)

        expected = np.array([
                [' ', ' ', ' ', ' ', 'X'], 
                [' ', ' ', ' ', 'X', ' '], 
                [' ', ' ', ' ', 'O', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', 'X', ' ']])
        new_state = player.simulate_state_after_move(player.gameField, move)
        print ("STATE",)
        print(new_state)
        print()
        print ("EXPECTED", expected)
        self.assertTrue(np.array_equal(expected, new_state))

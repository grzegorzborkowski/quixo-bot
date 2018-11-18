import unittest
from Player import *
import numpy as np

class TestWinConditions(unittest.TestCase):
    
    def test_check_player_won_row(self):
        player = Player()
        player.setStateOfGameField(
           np.array([
                ['X', 'O', 'O', ' ', 'X'], 
                ['O', 'O', 'O', 'O', 'O'], 
                ['O', 'O', ' ', ' ', 'O'], 
                [' ', ' ', ' ', ' ', ' '], 
                ['X', 'O', 'O', ' ', 'X']]),
        )
        self.assertTrue(player.check_if_player_won_row(player.gameField, O_MARK))
        self.assertFalse(player.check_if_player_won_row(player.gameField, X_MARK))
    
    def test_check_player_won_column(self):
        player = Player()
        player.setStateOfGameField(
           np.array([
                ['X', 'O', 'O', ' ', 'X'], 
                ['O', 'O', ' ', 'O', 'O'], 
                ['O', 'O', ' ', ' ', 'O'], 
                [' ', 'O', ' ', ' ', ' '], 
                ['X', 'O', 'O', ' ', 'X']]),
        )
        self.assertTrue(player.check_if_player_won_column(player.gameField, O_MARK))
        self.assertFalse(player.check_if_player_won_column(player.gameField, X_MARK))

    def test_check_player_won_diagonal(self):
        player = Player()
        player.setStateOfGameField(
           np.array([
                ['X', 'O', 'O', ' ', 'X'], 
                ['O', 'X', ' ', 'O', 'O'], 
                ['O', 'O', 'X', ' ', 'O'], 
                [' ', 'O', ' ', 'X', ' '], 
                ['X', 'O', 'O', ' ', 'X']]),
        )
        self.assertTrue(player.check_if_player_won_diagonal(player.gameField, X_MARK))
        self.assertFalse(player.check_if_player_won_diagonal(player.gameField, O_MARK))

    def test_check_player_won_diagonal_2(self):
        player = Player()
        player.setStateOfGameField(
           np.array([
                ['X', 'O', 'O', ' ', 'O'], 
                ['O', 'X', ' ', 'O', 'O'], 
                ['O', 'O', 'O', ' ', 'O'], 
                [' ', 'O', ' ', 'X', ' '], 
                ['O', 'O', 'O', ' ', 'X']]),
        )
        self.assertTrue(player.check_if_player_won_diagonal(player.gameField, O_MARK))
        self.assertFalse(player.check_if_player_won_diagonal(player.gameField, X_MARK))
    
import unittest

from src.Game.Chess import Chess
from src.Game.Movement import Movement
from src.Model.ChessBoard import ChessBoard
from src.Model.Player import Player
from src.Model.ChessPiece import *


class MovementTest(unittest.TestCase):

    def test_vertical_movement(self):
        chessboard = ChessBoard()
        movement = Movement(chessboard)
        self.assertEqual(movement.vertical_movement_unlimited("D7"), ["D8", "D6", "D5", "D4", "D3", "D2", "D1"])

    def test_horizontal_movement(self):
        chessboard = ChessBoard()
        movement = Movement(chessboard)
        self.assertEqual(movement.horizontal_movement_unlimited("D7"), ["A7", "B7", "C7", "E7", "F7", "G7", "H7"])

    def test_right_diagonal_movement(self):
        chessboard = ChessBoard()
        movement = Movement(chessboard)
        self.assertEqual(movement.right_diagonal_movement_unlimited("D7"), ["C8", "E6", "F5", "G4", "H3"])

    def test_left_diagonal_movement(self):
        chessboard = ChessBoard()
        movement = Movement(chessboard)
        self.assertEqual(movement.left_diagonal_movement_unlimited("D7"), ["E8", "C6", "B5", "A4"])
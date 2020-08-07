import unittest

from src.Game.Chess import Chess
from src.Game.Movement.ChessMovement import *
from src.Model.ChessBoard import ChessBoard
from src.Model.Player import Player
from src.Model.ChessPiece import *


class ChessMovementTest(unittest.TestCase):

    def test_rook_movement(self):
        rook_movement = RookMovement()
        squares = rook_movement.movement("D7")
        self.assertEqual(squares, ["D8", "D6", "D5", "D4", "D3", "D2", "D1",
                                   "A7", "B7", "C7", "E7", "F7", "G7", "H7"])

    def test_bishop_movement(self):
        bishop_movement = BishopMovement()
        squares = bishop_movement.movement("D7")
        self.assertEqual(squares, ["E8", "C6", "B5", "A4", "C8", "E6", "F5", "G4", "H3"])


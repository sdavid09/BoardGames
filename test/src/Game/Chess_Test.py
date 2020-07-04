import unittest

from src.Game.Chess import Chess
from src.Model.ChessBoard import ChessBoard
from src.Model.ChessPiece import *


class ChessTest(unittest.TestCase):

    def test_setup(self):
        chessboard = ChessBoard()
        chess = Chess(chessboard)
        chess.setup()
        self.assertTrue(isinstance(chess.chessboard['a8'], Rook))
        self.assertTrue(isinstance(chess.chessboard['b8'], Knight))
        self.assertTrue(isinstance(chess.chessboard['c8'], Bishop))
        self.assertTrue(isinstance(chess.chessboard['d8'], Queen))
        self.assertTrue(isinstance(chess.chessboard['e8'], King))
        self.assertTrue(isinstance(chess.chessboard['f8'], Bishop))
        self.assertTrue(isinstance(chess.chessboard['g8'], Knight))
        self.assertTrue(isinstance(chess.chessboard['h8'], Rook))
        self.assertTrue(isinstance(chess.chessboard['a7'], Pawn))

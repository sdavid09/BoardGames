import unittest

from src.Game.Chess import Chess
from src.Model.ChessBoard import ChessBoard
from src.Model.ChessPiece import *


class ChessTest(unittest.TestCase):

    def test_setup(self):
        chess = ChessBoard()
        rook = Rook(1, "white", '')
        Chess.setup(chess)
        self.assertEqual(chess[0], [rook, 'HORSE', 'BISHOP', 'QUEEN', 'KING', 'BISHOP', 'HORSE', 'ROOK'] )
        self.assertEqual(chess[1], ['PAWN'] * 8 )
        self.assertEqual(chess[6], ['PAWN'] * 8 )
        self.assertEqual(chess[7], ['ROOK', 'HORSE', 'BISHOP', 'QUEEN', 'KING', 'BISHOP', 'HORSE', 'ROOK'])

    # def test_invalid__chess_notation(self):
    #     chess_board = ChessBoard()
    #     row, col = chess_board.check_chess_notation('ab11')
    #     self.assertEqual(row, '')
    #     self.assertEqual(col, '')

    # def test_valid__chess_notation(self):
    #     chess_board = ChessBoard()
    #     row, col = chess_board.check_chess_notation('a1')
    #     self.assertEqual(row, 'a')
    #     self.assertEqual(col, '1')
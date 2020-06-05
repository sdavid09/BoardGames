import unittest

from src.Board.ChessBoard import ChessBoard

class ChessBoardTest(unittest.TestCase):
    def test_board_is_8x8(self):
        # check if board is a 8x8, 64 pieces
        chess_board = ChessBoard()
        self.assertEqual(len(chess_board), 64)
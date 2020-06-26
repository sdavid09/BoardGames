import unittest

from src.Model.ChessBoard import ChessBoard

class ChessBoardTest(unittest.TestCase):
    def test_board_is_8x8(self):
        # check if board is a 8x8, 64 pieces
        chess_board = ChessBoard()
        self.assertEqual(len(chess_board), 64)

    def test_set_and_get_item_by_chess_notation(self):
        chess_board = ChessBoard()
        king =   u'\u265A'
        chess_board['a1'] = king
        self.assertEqual(chess_board['a1'], king)

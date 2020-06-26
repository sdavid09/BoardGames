import unittest

from src.Game.Chess import Chess


class ChessTest(unittest.TestCase):
    def test_pieces_setup(self):
        pass

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
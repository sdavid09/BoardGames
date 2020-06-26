import unittest

from src.Model.ChessBoard import ChessBoard

class ChessBoardTest(unittest.TestCase):
    def test_board_is_8x8(self):
        # check if board is a 8x8, 64 pieces
        chess_board = ChessBoard()
        self.assertEqual(len(chess_board), 64)

    def test_set_and_get_item_by_chess_notation(self):
        chess_board = ChessBoard()
        rook =   u'\u2656'
        chess_board['a1'] = rook
        self.assertEqual(chess_board['a1'], rook)

    def test_pieces_starting_location(self):
        chess_board = ChessBoard()
        chess_board.setup_initial_pieces()

        self.assertEqual(chess_board[0], ['ROOK', 'HORSE', 'BISHOP', 'QUEEN', 'KING', 'BISHOP', 'HORSE', 'ROOK'] )
        self.assertEqual(chess_board[1], ['PAWN'] * 8 )
        self.assertEqual(chess_board[6], ['PAWN'] * 8 )
        self.assertEqual(chess_board[7], ['ROOK', 'HORSE', 'BISHOP', 'QUEEN', 'KING', 'BISHOP', 'HORSE', 'ROOK'])


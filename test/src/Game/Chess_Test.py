import unittest

from src.Game.Chess import Chess
from src.Model.ChessBoard import ChessBoard
from src.Model.Player import Player
from src.Model.ChessPiece import *


class ChessTest(unittest.TestCase):

    def test_setup_first_player(self):
        chessboard = ChessBoard()
        player_one = Player("PlayerOne", 1)
        player_two = Player("PlayerTwo", 2)
        chess = Chess(chessboard, player_one, player_two)
        chess.setup()
        self.assertTrue(isinstance(chess.chessboard['a8'], Rook))
        self.assertTrue(isinstance(chess.chessboard['b8'], Knight))
        self.assertTrue(isinstance(chess.chessboard['c8'], Bishop))
        self.assertTrue(isinstance(chess.chessboard['d8'], Queen))
        self.assertTrue(isinstance(chess.chessboard['e8'], King))
        self.assertTrue(isinstance(chess.chessboard['f8'], Bishop))
        self.assertTrue(isinstance(chess.chessboard['g8'], Knight))
        self.assertTrue(isinstance(chess.chessboard['h8'], Rook))
        [self.assertTrue(isinstance(piece, Pawn)) for piece in chess.chessboard[1]]

    def test_setup_second_player(self):
        chessboard = ChessBoard()
        player_one = Player("PlayerOne", 1)
        player_two = Player("PlayerTwo", 2)
        chess = Chess(chessboard, player_one, player_two)
        chess.setup()
        self.assertTrue(isinstance(chess.chessboard['a1'], Rook))
        self.assertTrue(isinstance(chess.chessboard['b1'], Knight))
        self.assertTrue(isinstance(chess.chessboard['c1'], Bishop))
        self.assertTrue(isinstance(chess.chessboard['d1'], Queen))
        self.assertTrue(isinstance(chess.chessboard['e1'], King))
        self.assertTrue(isinstance(chess.chessboard['f1'], Bishop))
        self.assertTrue(isinstance(chess.chessboard['g1'], Knight))
        self.assertTrue(isinstance(chess.chessboard['h1'], Rook))
        self.assertTrue(isinstance(chess.chessboard['a2'], Pawn))
        [self.assertTrue(isinstance(piece, Pawn)) for piece in chess.chessboard[6]]

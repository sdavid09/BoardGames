
from src.Model.ChessPiece import *
from src.Model.ChessBoard import ChessBoard
from src.Model.Player import Player

class Chess:
    def __init__(self, chessboard: ChessBoard, 
                       player_one: Player, player_two: Player):
        self.chessboard = chessboard
        self.player_one = player_one
        self.player_two = player_two

    def setup(self):

        self.add_first_player_pieces()
        self.add_second_player_pieces()

    def add_first_player_pieces(self):

        self.chessboard[0] = [
        Rook("white", u'\u2656'),
        Knight("white", u'\u2658'),
        Bishop("white", u'\u2657'),
        Queen("white", u'\u2655' ),
        King("white", u'\u2654' ),
        Bishop("white", u'\u2657'),
        Knight("white", u'\u2658'),
        Rook("white", u'\u2656')]
        self.chessboard[1] = [Pawn("white", u'\u2659')] * len(self.chessboard[1])

    def add_second_player_pieces(self):

        self.chessboard[7] = [
        Rook("black", u'\u265C'),
        Knight("black", u'\u265A'),
        Bishop("black", u'\u2657'),
        Queen("black", u'\u265B' ),
        King("black", u'\u2654' ),
        Bishop("black", u'\u265D'),
        Knight("black", u'\u265E'),
        Rook("black", u'\u265C')]
        self.chessboard[6] = [Pawn("black", u'\u265F')] * len(self.chessboard[1])

    def is_valid_move(self):
        pass

    def check(self):
        pass

    def castle(self):
        pass

    def next_turn(self):
        pass


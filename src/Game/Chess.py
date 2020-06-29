
from src.Model.ChessPiece import *
from src.Model.ChessBoard import ChessBoard

class Chess:

    @staticmethod
    def setup(board: ChessBoard):
        # row of pawns at 2nd row and 6th row
        rook = Rook(1, "white", '')
        board[0] = [rook, 'HORSE', 'BISHOP', 'QUEEN', 'KING', 'BISHOP', 'HORSE', 'ROOK']
        board[1] = ["PAWN"] * len(board[1])
        board[6] = ["PAWN"] * len(board[1])
        board[7] = ['ROOK', 'HORSE', 'BISHOP', 'QUEEN', 'KING', 'BISHOP', 'HORSE', 'ROOK']

    def is_valid_move(self):
        pass

    def check(self):
        pass

    def castle(self):
        pass

    def next_turn(self):
        pass


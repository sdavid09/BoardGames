
from src.Model.ChessPiece import *
from src.Model.ChessBoard import ChessBoard
from src.Model.Player import Player

class Movement:
    def __init__(self, chessboard: ChessBoard):
        self.chessboard = chessboard

    def vertical_movement_unlimited(self, current_location):
        row, col = self.chessboard.check_chess_notation(current_location)
        chess_row, chess_col = self.chessboard.row[row.upper()], self.chessboard.col[int(col)]
        available = [( chess_row, i ) for i in range(self.chessboard.board.y_size) if i != chess_col]
        spots = [self.chessboard.convert_to_chess_notation(spot) for spot in available]
        return [ "".join(row + str(col)) for row, col in spots]

    def horizontal_movement_unlimited(self, current_location):
        row, col = self.chessboard.check_chess_notation(current_location)
        chess_row, chess_col = self.chessboard.row[row.upper()], self.chessboard.col[int(col)]
        available = [( i , chess_col ) for i in range(self.chessboard.board.x_size) if i != chess_row]
        spots = [self.chessboard.convert_to_chess_notation(spot) for spot in available]
        return [ "".join(row + str(col)) for row, col in spots]




from src.Model.ChessPiece import *
from src.Model.ChessBoard import ChessBoard
from src.Model.Player import Player
from .SubMovement import *
check_chess_notation = ChessBoard.check_chess_notation

class CardinalDirections:
    def __init__(self):
        self.chessboard = ChessBoard()

    def vertical_movement_unlimited(self, current_location):
        row, col = check_chess_notation(current_location)
        chess_row, chess_col = self.chessboard.row[row.upper()], self.chessboard.col[int(col)]
        squares = [( chess_row, i ) for i in range(self.chessboard.board.y_size) if i != chess_col]
        return squares

    def vertical_movement_one(self, current_location):
        row, col = self.chessboard.check_chess_notation(current_location)
        chess_row, chess_col = self.chessboard.row[row.upper()], self.chessboard.col[int(col)]
        squares = [( chess_row, i ) for i in range(1) if i != chess_col]
        return squares

    def horizontal_movement_unlimited(self, current_location):
        row, col = self.chessboard.check_chess_notation(current_location)
        chess_row, chess_col = self.chessboard.row[row.upper()], self.chessboard.col[int(col)]
        squares = [( i , chess_col ) for i in range(self.chessboard.board.x_size) if i != chess_row]
        return squares

    def horizontal_and_vertical_movement_unlimited(self, current_location):
        vertical_squares = self.vertical_movement_unlimited(current_location)
        horizontal_squares = self.horizontal_movement_unlimited(current_location)
        return vertical_squares + horizontal_squares

class OrdinalDirections:

    def right_and_left_diagonal_movement_unlimited(self, current_location, count=None):
        right_squares = self.right_diagonal_movement_unlimited(current_location, count)
        left_squares = self.left_diagonal_movement_unlimited(current_location, count)
        return right_squares + left_squares

    def right_and_left_diagonal_movement_one(self, current_location, count=1):
        right_squares = self.right_diagonal_movement_unlimited(current_location, count)
        left_squares = self.left_diagonal_movement_unlimited(current_location, count)
        return right_squares + left_squares

    def right_diagonal_movement_unlimited(self, current_location, count=None):
        return lower_right(current_location, count) + upper_left(current_location, count)

    def left_diagonal_movement_unlimited(self, current_location, count=None):
        return lower_left(current_location, count) +  upper_right(current_location, count)
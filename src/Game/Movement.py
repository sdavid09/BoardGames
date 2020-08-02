
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

    def right_diagonal_movement_unlimited(self, current_location):
        row, col = self.chessboard.check_chess_notation(current_location)
        chess_row, chess_col = self.chessboard.row[row.upper()], self.chessboard.col[int(col)]
        squares = []
        squares += self.left_bound(chess_row, chess_col, -1, -1)
        squares += self.right_bound(chess_row, chess_col, 1, 1)
        spots = [self.chessboard.convert_to_chess_notation(spot) for spot in squares]
        return [ "".join(str(row) + str(col)) for row, col in spots]

    def left_diagonal_movement_unlimited(self, current_location):
        row, col = self.chessboard.check_chess_notation(current_location)
        chess_row, chess_col = self.chessboard.row[row.upper()], self.chessboard.col[int(col)]
        squares = []
        squares += self.left_bound(chess_row, chess_col, 1, -1)
        squares += self.right_bound(chess_row, chess_col, -1, 1)
        spots = [self.chessboard.convert_to_chess_notation(spot) for spot in squares]
        return [ "".join(str(row) + str(col)) for row, col in spots]

    def left_bound(self, chess_row, chess_col, chess_row_inc, chess_col_inc):
        squares = []
        for square in range ( chess_row ):
            chess_row += chess_row_inc
            chess_col += chess_col_inc
            if(chess_col < 0 or chess_row < 0 or chess_col > 7 or chess_row > 7):
                break
            squares.append((chess_row, chess_col))
        return squares

    def right_bound(self, chess_row, chess_col, chess_row_inc, chess_col_inc):
        squares = []
        for square in range ( chess_row, self.chessboard.board.x_size):
            chess_row += chess_row_inc
            chess_col += chess_col_inc
            if(chess_col > 7 or chess_row > 7 or chess_col < 0 or chess_row < 0):
                break
            squares.append((chess_row, chess_col))
        return squares


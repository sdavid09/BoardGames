from src.Model.ChessBoard import ChessBoard
MAX = 7
MIN = 0

def square_iterator(coordinates, grid_row_inc, grid_col_inc, count=None):
        squares = []
        grid_row, grid_col = coordinates

        temp_counter = 0
        for val in range(MAX):
            if (grid_row == MIN or grid_row == MAX or
                grid_col == MIN or grid_col == MAX or
                temp_counter == count ):
                break
            grid_row += grid_row_inc
            grid_col += grid_col_inc
            squares.append((grid_row, grid_col))
            temp_counter += 1

        return squares

def convert_to_grid_notation(current_location):
    chess_row, chess_col = ChessBoard.check_chess_notation(current_location)
    print(chess_row, chess_col)
    grid_row, grid_col = ChessBoard.row[chess_row.upper()], ChessBoard.col[int(chess_col)]
    return grid_row, grid_col

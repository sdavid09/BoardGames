from .MovementUtils import *

def lower_left(current_location, count=None):
    grid_row, grid_col = convert_to_grid_notation(current_location)
    squares = square_iterator((grid_row, grid_col), -1, -1, count)
    return squares

def lower_right(current_location, count=None):
    grid_row, grid_col = convert_to_grid_notation(current_location)
    squares = square_iterator((grid_row, grid_col), +1, -1, count)
    return squares

def upper_left(current_location, count=None):
    grid_row, grid_col = convert_to_grid_notation(current_location)
    squares = square_iterator((grid_row, grid_col), -1, 1, count)
    return squares

def upper_right(current_location, count=None):
    grid_row, grid_col = convert_to_grid_notation(current_location)
    squares = square_iterator((grid_row, grid_col), 1, 1, count)
    return squares

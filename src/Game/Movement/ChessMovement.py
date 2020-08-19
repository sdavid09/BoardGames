from abc import ABCMeta, abstractmethod
from src.Model.ChessBoard import ChessBoard
from src.Game.Movement.Directions import *

class ChessMovement(metaclass=ABCMeta):

    @abstractmethod
    def movement(self):
        pass

    def format_to_chess_notation(self, squares):
        chess_squares = [ChessBoard.convert_to_chess_notation(spot) for spot in squares]
        return [ "".join(str(row) + str(col)) for row, col in chess_squares]

class RookMovement(ChessMovement):
    def movement(self, location):
        movement = CardinalDirections()
        squares = movement.horizontal_and_vertical_movement_unlimited(location)
        return self.format_to_chess_notation(squares)

class KnightMovement(ChessMovement):
    def movement(self):
        pass

class BishopMovement(ChessMovement):
    def movement(self, location):
        movement = OrdinalDirections()
        squares = movement.right_and_left_diagonal_movement_unlimited(location)
        return self.format_to_chess_notation(squares)

class QueenMovement(ChessMovement):
    def movement(self, location):
        cardinal_movement = CardinalDirections()
        ordinal_movement = OrdinalDirections()
        squares = ordinal_movement.right_and_left_diagonal_movement_unlimited(location)
        squares += cardinal_movement.horizontal_and_vertical_movement_unlimited(location)
        return self.format_to_chess_notation(squares)

class KingMovement(ChessMovement):
    def movement(self):
        pass

class PawnMovement(ChessMovement):
    def movement(self):
        pass
from abc import ABC, abstractmethod

class Board:
    @abstractmethod
    def display(self):
        pass

class ChessBoard(Board):
    pass


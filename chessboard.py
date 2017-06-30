#!/usr/bin/python
from board import Board 

class ChessBoard(Board):
    def __init__(self, xsize, ysize):
        super(ChessBoard, self).__init__(xsize, ysize)

chess = ChessBoard(8,8)
chess.displayBoard()

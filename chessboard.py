#!/usr/bin/python
from board import Board 

whitepieces = {
    'King'   : u'\u2654',
    'Queen'  : u'\u2655', 
    'Rook'   : u'\u2656',
    'Bishop' : u'\u2657',
    'Knight' : u'\u2658',
    'Pawn'   : u'\u2659',
}

blackpieces = {
    'King'   : u'\u265A',
    'Queen'  : u'\u265B', 
    'Rook'   : u'\u265C',
    'Bishop' : u'\u265D',
    'Knight' : u'\u265E',
    'Pawn'   : u'\u265F',
}

class ChessBoard(Board):
    def __init__(self):
        super(ChessBoard, self).__init__(8, 8) #Chess board is a 8x8 board

    def setStartingPieces(self):
#Setup Black Pieces
        self.board[1][1] = blackpieces['Rook']
        self.board[1][8] = blackpieces['Rook']
        self.board[1][2] = blackpieces['Knight']
        self.board[1][7] = blackpieces['Knight']
        self.board[1][3] = blackpieces['Bishop']
        self.board[1][6] = blackpieces['Bishop']
        self.board[1][4] = blackpieces['Queen']
        self.board[1][5] = blackpieces['King']
        for i in range(1,9):
            self.board[2][i] = blackpieces['Pawn']
#Setup White Pieces
        self.board[8][1] = whitepieces['Rook']
        self.board[8][8] = whitepieces['Rook']
        self.board[8][2] = whitepieces['Knight']
        self.board[8][7] = whitepieces['Knight']
        self.board[8][3] = whitepieces['Bishop']
        self.board[8][6] = whitepieces['Bishop']
        self.board[8][4] = whitepieces['Queen']
        self.board[8][5] = whitepieces['King']
        for i in range(1,9):
            self.board[7][i] = whitepieces['Pawn']
chess = ChessBoard()
chess.setStartingPieces()
chess.displayBoard()

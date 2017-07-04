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
    def __init__(self, xsize = 8, ysize = 8):
        super(ChessBoard, self).__init__(xsize,ysize) #Chess board is a 8x8 board

    def setStartingPieces(self):
#Setup Black Pieces
        self.board[0][1] = blackpieces['Rook']
        self.board[0][8] = blackpieces['Rook']
        self.board[0][2] = blackpieces['Knight']
        self.board[0][7] = blackpieces['Knight']
        self.board[0][3] = blackpieces['Bishop']
        self.board[0][6] = blackpieces['Bishop']
        self.board[0][4] = blackpieces['Queen']
        self.board[0][5] = blackpieces['King']
        for i in range(1,9):
            self.board[1][i] = blackpieces['Pawn']
#Setup White Pieces
        self.board[7][1] = whitepieces['Rook']
        self.board[7][8] = whitepieces['Rook']
        self.board[7][2] = whitepieces['Knight']
        self.board[7][7] = whitepieces['Knight']
        self.board[7][3] = whitepieces['Bishop']
        self.board[7][6] = whitepieces['Bishop']
        self.board[7][4] = whitepieces['Queen']
        self.board[7][5] = whitepieces['King']
        for i in range(1,9):
            self.board[6][i] = whitepieces['Pawn']
        self.board[8][0] = ' '
chess = ChessBoard()
chess.setStartingPieces()
chess.displayBoard()
chess.moveBoardPieces()

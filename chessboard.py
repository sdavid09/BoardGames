#!/usr/bin/python
from board import Board 

whitepieces = {
    'WKing'   : u'\u2654',
    'WQueen'  : u'\u2655', 
    'WRook'   : u'\u2656',
    'WBishop' : u'\u2657',
    'WKnight' : u'\u2658',
    'WPawn'   : u'\u2659',
}

blackpieces = {
    'BKing'   : u'\u265A',
    'BQueen'  : u'\u265B', 
    'BRook'   : u'\u265C',
    'BBishop' : u'\u265D',
    'BKnight' : u'\u265E',
    'BPawn'   : u'\u265F',
}
validMove = {
   
    'King'   : [[1,1],[-1,-1],[-1,0],[0,-1],[1,0],[-1,1],[0,1],[1,-1]],
    'Queen'  : '', 
    'Rook'   : [[x,0] for x in range (0, 8)],
    'Bishop' : '',
    'Knight' : [[1,2],[-1,2],[1,-2],[2,1],[-2,-1],[2,-1],[-2,1]],
    'Pawn'   : [[1, 0] , [-1, 0]] ,

}
#Additional valid moves for Rook
validMove['Rook'] += [[0,y] for y in range (0, 8)]
validMove['Rook'] += [[x,0] for x in range (-8, 0)]
validMove['Rook'] += [[x,0] for x in range (0, -8)]
validMove['Rook'] += [[0,y] for y in range (0, -8)]
validMove['Rook'] += [[0,y] for y in range (-8, 0)]


class ChessBoard (Board):
    def __init__(self, xsize = 8, ysize = 8):
        super(ChessBoard, self).__init__(xsize,ysize) #Chess board is a 8x8 board
        self.p1pieces = whitepieces
        self.p2pieces = blackpieces
        self.pieces = dict(whitepieces.items() + blackpieces.items())
        self.vldmove = validMove
        
    def setStartingPieces(self):
#Setup Black Pieces
        self.board[0][1] = blackpieces['BRook']
        self.board[0][8] = blackpieces['BRook']
        self.board[0][2] = blackpieces['BKnight']
        self.board[0][7] = blackpieces['BKnight']
        self.board[0][3] = blackpieces['BBishop']
        self.board[0][6] = blackpieces['BBishop']
        self.board[0][4] = blackpieces['BQueen']
        self.board[0][5] = blackpieces['BKing']
        for i in range(1,9):
            self.board[1][i] = blackpieces['BPawn']
#Setup White Pieces
        self.board[7][1] = whitepieces['WRook']
        self.board[7][8] = whitepieces['WRook']
        self.board[7][2] = whitepieces['WKnight']
        self.board[7][7] = whitepieces['WKnight']
        self.board[7][3] = whitepieces['WBishop']
        self.board[7][6] = whitepieces['WBishop']
        self.board[7][4] = whitepieces['WQueen']
        self.board[7][5] = whitepieces['WKing']
        for i in range(1,9):
            self.board[6][i] = whitepieces['WPawn']
        self.board[8][0] = ' '


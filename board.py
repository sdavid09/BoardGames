#!/usr/bin/python

class Board(object):

    def __init__(self, xsize, ysize):
        self.xsize = xsize + 1
        self.ysize = ysize + 1
        self.board = []
        self.setupBoard()

    def setupBoard(self):
        """Setup Board"""
        for i in range( 0, self.ysize):
            self.board.append(["0"]*self.xsize)
        self.createGrid()
        self.board[0][0] = ' '
        self.setBoardPieces()

    def createGrid(self):
        """Create a Grid Reference Row are Alphabets and Columns by Number"""
        k = 0
        for i in range(1, self.xsize):
            self.board[0][i] = chr( ord('a') + k)
            k+=1
        for i in range(1, self.ysize):
            self.board[i][0] = str(i)

    def setBoardPieces(self): 
        print "Board:"

    def displayBoard(self):
        """Print out Board"""
        for row in self.board:
            print " ".join(row)

#!/usr/bin/python
import time
import os

class Board(object):

    def __init__(self, xsize, ysize):
        self.xsize = xsize + 1 
        self.ysize = ysize + 1
        self.row = xsize 
        self.col = ysize
        self.board = []
        self.board_alphakey = {}
        self.board_numkey = {}
        self.setupBoard()

    def setupBoard(self):
        """Setup Board"""
        self.board = [['0' for x in range(self.xsize)] for y in range(self.ysize)] # Create 2d Array
        self.createGrid()

    def createGrid(self):
        """Create a Grid Reference Row are Alphabets and Columns by Number"""
        k = 0
        for i in range(1, self.xsize):
            self.board[self.col][i] = chr( ord('a') + k) # x axis of alphabet
            self.board_alphakey[chr( ord('a') + k)] = i
            k+=1
        y = self.col
        for i in range(0, self.ysize):
            self.board[i][0] = str(y) # y axis of numbers
            if y != 0:
                self.board_numkey[y] = abs( y - self.col)
            y -= 1
        print (self.board_numkey )
        print (self.board_alphakey)


    def displayBoard(self):
        """Print out Board"""
        for i in range (5):
            time.sleep(.1)
        os.system("clear")
        for row in self.board:
            print(" ".join(row))

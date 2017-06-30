#!/usr/bin/python

class Board(object):

    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.board = []
        self.setupBoard()

    def setupBoard(self):
        for i in range( 0, self.ysize):
            self.board.append(["0"]*self.xsize)

    def displayBoard(self):
        for row in self.board:
            print " ".join(row)

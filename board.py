#!/usr/bin/python

import re

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
        for i in range( 0, self.ysize):
            self.board.append(["0"] * self.xsize )
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
        print self.board_numkey
 
    def moveBoardPieces(self): 
        """Move the Board Pieces"""
        while True:
            user_input = raw_input("Enter Board Space: ")
            board_pattern = re.compile(r'([a-zA-Z])([0-9]+)')
            result = board_pattern.search(user_input)
            if(result):
                y_row = result.group(1) #alpha values
                x_row = int(result.group(2)) # num value
                if y_row in self.board_alphakey and x_row in self.board_numkey:
                    y1_row = self.board_alphakey[y_row]
                    x1_row = self.board_numkey[x_row]
                    print " X-value: %s Y-Value: %s\n" %(x1_row, y1_row)
                    self.board[x1_row][y1_row] = "X"
                    self.displayBoard()
                else:
                    print "Out of Board Range \n"
            elif user_input == "exit":
                break
            else:
                print "Invalid Input \n"

    def displayBoard(self):
        """Print out Board"""
        for row in self.board:
            print" ".join(row)

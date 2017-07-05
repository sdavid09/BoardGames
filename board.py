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
        self.player = 0
        self.p1pieces = {}
        self.p2pieces = {}
        self.vldmove = {}
        self.playerturn = 0

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
        print self.board_numkey 
        print self.board_alphakey

    def checkValidMove(self, piece, x1 , y1 , x2 , y2 ):
        if piece == u'\u2654' or piece == u'\u265A':
            print "KING!\n"
            valid = False
            for key, value in self.vldmove.items():
                for x,y in value:
                    print x,y
                    if (x1 + x) == x2 and (y1 + y) == y2:
                        return True
                
            return valid

    def moveBoardPieces(self): 
        """Accept User input and move pieces on that grid reference"""
        result = False
        while True:
            user_input = raw_input("Enter Board Space: ")
            if user_input == "exit":
                break
            else:
                board_pattern = re.compile(r'(^[a-z])([0-9])\s([a-z])([0-9]$)') # pattern can still have a3e2 as valid
                result = board_pattern.search(user_input)
                if(result):
                    y_row = result.group(1) #alpha values
                    x_row = int(result.group(2)) # num value
                    y2_row = result.group(3)
                    x2_row = int(result.group(4))
                    if y_row in self.board_alphakey and x_row in self.board_numkey:
                        y_row_n = self.board_alphakey[y_row]
                        x_row_n = self.board_numkey[x_row]
                        if self.board[x_row_n][y_row_n] != '0':
                            if self.board[x_row_n][y_row_n] in self.p1pieces.values():
                                print "Player 1 Selected \n"
                                self.player =1 
                            else:
                                print "Player 2 Selected \n"
                                self.player =2 
                            if y2_row in self.board_alphakey and x2_row in self.board_numkey:
                                print " X-value: %s Y-Value: %s\n" %(x_row_n, y_row_n)
                                y2_row_n = self.board_alphakey[y2_row]
                                x2_row_n = self.board_numkey[x2_row]
                                if (self.player == 1 and self.board[x2_row_n][y2_row_n] not in self.p1pieces.values()) or (self.player ==2 and self.board[x2_row_n][y2_row_n] not in self.p2pieces.values()) :
                                    if self.checkValidMove(self.board[x_row_n][y_row_n],x_row_n, y_row_n, x2_row_n, y2_row_n):
                                        val = self.board[x_row_n].pop(y_row_n)
                                        self.board[x_row_n].insert(y_row_n,'0')
                                        self.board[x2_row_n].pop(y2_row_n)
                                        self.board[x2_row_n].insert(y2_row_n,val)
                                        self.displayBoard()
                                else:
                                    print "Player's piece occupying\n"
                                    continue
                    else    :    
                        print "Out of Board Range \n"
                else:
                    print "Invalid Input \n"

    def displayBoard(self):
        """Print out Board"""
        for row in self.board:
            print" ".join(row)

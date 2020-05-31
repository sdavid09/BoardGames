#!/usr/bin/python


import re
import os
import sys
from chessboard import *

class Game ( object):
    
    def __init__(self):
        self.p1pieces = {}
        self.p2pieces = {}
        self.playerturn = 0
        self.player = 0

    def checkValidMove(self, game, piece, x1, y1, x2, y2 ):
            valid = False
            print ("x1: {}, y1: {}, x2: {}, y3: {}".format(str(x1), str(y1), str(x2), str(y2)))
            for key1, val in game.pieces.items():
                if val == piece:
                    #print "Found Piece! %s %s" %( key1[1:], val)
                    break
            piece = key1[1:]
            for key, value in game.vldmove.items():
                if key == piece:
                    for x,y in value:
                        #print x,y
                        if (x1 + x) == x2 and (y1 + y) == y2:
                            return True
                
            return valid

    def moveBoardPieces(self, game): 
        """Accept User input and move pieces on that grid reference"""
        result = False
        while True:
            user_input = input("Enter Board Space: ")
            if user_input == "exit":
                break
            else:
                board_pattern = re.compile(r'(^[a-z])([0-9])\s?([a-z])([0-9]$)') # pattern can still have a3e2 as valid
                result = board_pattern.search(user_input)
                if(result):
                    y_row = result.group(1) #alpha values
                    x_row = int(result.group(2)) # num value
                    y2_row = result.group(3)
                    x2_row = int(result.group(4))
                    if y_row in game.board_alphakey and x_row in game.board_numkey:
                        y_row_n = game.board_alphakey[y_row]
                        x_row_n = game.board_numkey[x_row]
                        if game.board[x_row_n][y_row_n] != '0':
                            if game.board[x_row_n][y_row_n] in game.p1pieces.values():
                                print ("Player 1 Selected \n")
                                self.player =1 
                            else:
                                print( "Player 2 Selected \n")
                                self.player =2 
                            if y2_row in game.board_alphakey and x2_row in game.board_numkey:
                                print (" X-value: {} Y-Value: {} \n".format(x_row_n, y_row_n))
                                y2_row_n = game.board_alphakey[y2_row]
                                x2_row_n = game.board_numkey[x2_row]
                                if (self.player == 1 and game.board[x2_row_n][y2_row_n] not in game.p1pieces.values()) or (self.player ==2 and game.board[x2_row_n][y2_row_n] not in game.p2pieces.values()) :
                                    if self.checkValidMove(game,game.board[x_row_n][y_row_n],x_row_n, y_row_n, x2_row_n, y2_row_n):
                                        val = game.board[x_row_n].pop(y_row_n)
                                        game.board[x_row_n].insert(y_row_n,'0')
                                        game.board[x2_row_n].pop(y2_row_n)
                                        game.board[x2_row_n].insert(y2_row_n,val)
                                        game.displayBoard()
                                    else: 
                                        print ("Invalid Move!\n")
                                else:
                                    print ("Player's piece occupying\n")
                                    continue
                    else    :    
                        print ("Out of Board Range \n")
                else:
                    print ("Invalid Input \n")


chess = ChessBoard()
chess.setStartingPieces()
chess.displayBoard()
game = Game()
game.moveBoardPieces(chess)

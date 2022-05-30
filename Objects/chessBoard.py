
import numpy 
import pygame 
import Objects.chess as chess
import tkinter as tk
import copy

class Board:
     
     gameChess = chess.Chess()
     pieceList = gameChess.pieces() 
     screen = pygame.display.set_mode((640 , 640))

     # take in the object and update it with a new cordinate
     # initialize board and pieces
     def __init__(self):
        pygame.init()
        self.clickedlist = []
        pygame.display.set_caption('Chess')
        self.updateBoard(self.pieceList)

     # Update the board with the list of pieces on the board
     def updateBoard(self , pList):
        black = (205,192,176)
        white = (255,228,196)
        color = white
        self.clickedlist = []

        self.screen.fill('red')
        for x in range(8):
                for y in range(8):
                    rect = pygame.Rect(y*80, x*80, 80, 80)
                    image = pygame.draw.rect(self.screen, color, rect , 0)
                    if color == white:
                        color = black
                    else:
                        color = white
                    self.clickedlist.append(image)
                if color == white:
                    color = black
                else:
                    color = white
        self.gameChess.displayPieces(self.screen ,pList)

 
    

        
        
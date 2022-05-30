# Game.py is where it handle multiple game event as well as function , I might have to create a class seperate board and chess function
import Objects.chessBoard as board
import Objects.chess as chess
import pygame 

class Game:

    gameChess = chess.Chess()
    gameBoard = board.Board()
    
    def __init__(self):
        pass

    # ------------------------------------------------------
    # THIS IS BOARD EVENT
    # ------------------------------------------------------

    # Highlight the box
    def highlight(self , x , y):
        rect = pygame.Rect(x, y, 80, 80)
        pygame.draw.rect(self.gameBoard.screen, (0, 255, 0), rect , 4)

    # take a list then display the pieces on the chessboard
    def displayPieces(self, screen, list):
        for i in list:
            rect_1 = pygame.Rect(i.x, i.y, 80, 80)
            recCenter = i.image.get_rect(center = rect_1.center)
            screen.blit(i.image , recCenter)

    # ------------------------------------------------------
    # THIS IS CHESS EVENT
    # ------------------------------------------------------

    # Check for valid move and return if it's possible or not
    def validMove(self, piece, destination,  x = 1000 ,y = 1000 , emptyList = []):
        print("origin: " , piece.x , piece.y)
        for i in piece.move(x , y , emptyList):
            print("cord is" , i.x , i.y)
            if destination.x == i.x and destination.y == i.y:
                piece.first = False
                return True
        return False
    
    # Check if the king is dead or not , if it's then win the game
    def winCondition(self, object):

        if(isinstance(object, chess.King)): 
            if self.gameChess.checkColor(object.color):
                print("White lost , black wins")
            else:
                print("Black lost , white wins")
            pygame.quit()
            quit()

    # check what type of 
    def checkMove(self , object):
        if(isinstance(object, chess.Pawn)):
            pass
        elif(isinstance(object, chess.Rook)):
            pass
        elif(isinstance(object, chess.Knight)):
            pass
        elif(isinstance(object, chess.Bishop)):
            pass
        elif(isinstance(object, chess.Queen)):
            pass
        else:
            pass
    
    # move for the Pawn
    def pawnMove(self , eatX ,eatY , emptyList):
        validMove = []
        doubleWhiteMove = self.y- 80*2
        doubleBlackMove = self.y + 80*2
        whiteMove = self.y - 80
        blackMove = self.y + 80
        # Need to check seperately for black and white
        # First we check for whenver there is a piece that it can kill first or nah
        # shouldn't be moving if there's a piece in front of it
        # White check
        if(self.checkColor(self.color)):
            if self.first and eatY != doubleWhiteMove:
                validMove.append(chess.Valid(self.x, doubleWhiteMove))
            if eatY != whiteMove:
                validMove.append(chess.Valid(self.x, whiteMove))

        # if eatable then do this
            if (eatX == self.x - 80 and eatY == self.y - 80):
                validMove.append(chess.Valid(self.x - 80, self.y - 80))
            if (eatX == self.x + 80 and eatY == self.y - 80):
                validMove.append(chess.Valid(self.x + 80, self.y - 80))

        # If not then it's black
        else:
            if self.first and eatY != doubleBlackMove:
                validMove.append(chess.Valid(self.x, doubleBlackMove))
            if eatY != blackMove:
                validMove.append(chess.Valid(self.x, blackMove))

            # if eatable then do this
            if eatX == self.x + 80 and eatY == self.y + 80:
                validMove.append(chess.Valid(self.x + 80, self.y + 80))
            if eatX == self.x - 80 and eatY == self.y + 80:
                validMove.append(chess.Valid(self.x - 80, self.y + 80))

        # Return the list 
        return validMove  

    # move for the rook 
    def rookMove(self , eatX ,eatY , emptyList):
        validMove = []
        bx = self.x
        by = self.y
        xBlock = True
        # add all striaght x and y line into the list, at least until it doesn't get block
        # add all going across left and right
        while bx >= 0 or xBlock == False:
            blocked_piece = [s for s in emptyList if s.x == bx]
            if blocked_piece:
                if blocked_piece[0].color == self.color:
                    xBlock = False
            validMove.append(chess.Valid(bx , self.y))
            bx = bx - 80
        bx = self.x
        xBlock = True

        while bx <= 640 or xBlock == False:
            blocked_piece = [s for s in emptyList if s.x == bx]
            if blocked_piece:
                if blocked_piece[0].color == self.color:
                    xBlock = False
            validMove.append(chess.Valid(bx , self.y))
            bx = bx + 80
        bx = self.x
        xBlock = True
        
        # add all going up or down
        while by >= 0 or  xBlock == False:
            blocked_piece = [s for s in emptyList if s.x == bx]
            if blocked_piece:
                if blocked_piece[0].color == self.color:
                    xBlock = False
            validMove.append(chess.Valid(self.x , by))
            by = by - 80
        by = self.y
        xBlock = True

        while by <= 640 or xBlock == False:
            blocked_piece = [s for s in emptyList if s.x == bx]
            if blocked_piece:
                if blocked_piece[0].color == self.color:
                    xBlock = False
            validMove.append(chess.Valid(self.x , by))
            by = by + 80
            print(by)
        by = self.y
        xBlock = True
        

        return validMove
                                        
    # move for the Knight
    def knightMove(self , eatX ,eatY , emptyList):
        pass 

    # move for the Bishop
    def bishopMove(self , eatX ,eatY , emptyList):
        pass 

    # move for the Queen
    def queenMove(self , eatX ,eatY , emptyList):
        pass 

    # move for the King
    def kingMove(self , eatX ,eatY , emptyList):
        pass 
    
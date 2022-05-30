
from asyncio.windows_events import NULL
import Objects.chessBoard as board
import Objects.chess as chess
import Objects.game as game
import pygame 
import warnings
import tkinter as tk

warnings.filterwarnings("ignore", message="Numerical issues were encountered ")

#Initialize to show the board and stuff
gameBoard = board.Board()
gameChess = chess.Chess()
gameEvent = game.Game()

pieceList = gameChess.pieces()
posBox = gameBoard.clickedlist

# window = tk.Tk()
# window.mainloop()
# White is 0, always goes first
turnColor = 0

# First piece is always empty
first_piece = None

# Loop through the entire game
while(True):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # Get the collided chess rect   
            clicked_box = next(s for s in posBox if s.collidepoint(pos)) 

            # Check if there is a piece in that spot
            clicked_pieces = [s for s in pieceList if s.x == clicked_box.x and s.y == clicked_box.y] 

            # check for the first piece in the board
            if first_piece is None and clicked_pieces and clicked_pieces[0].color == turnColor:
                first_piece = clicked_pieces[0]
                gameEvent.highlight(clicked_box.x , clicked_box.y)

                
            # If not then first_piece must have it already
            elif first_piece:
                
                # check if the second click is empty , then move it to the spot
                if not clicked_pieces:

                    # check if the move is valid 
                    # If valid then continue with stuff
                    if(gameEvent.validMove(first_piece , clicked_box , 1000 , 1000 , pieceList)):
                        old_x = first_piece.x
                        old_y = first_piece.y

                        # first we need to alter the list
                        for i in pieceList:
                            if i.x == old_x and i.y == old_y:
                                i.x = clicked_box.x
                                i.y = clicked_box.y
                                break

                        # then update the board                    
                        gameBoard.updateBoard(pieceList)
                        turnColor = 1 - turnColor 
                        first_piece = None
                    
                    # If not then print something idk
                    else:
                        print("The move is not valid , please try a different move")
                
                # Then there is a second piece got clicked
                else:

                    # Same color will just just highlight the newer one and make it the first piece
                    if(first_piece.color == clicked_pieces[0].color):
                        first_piece = clicked_pieces[0]
                        gameBoard.updateBoard(pieceList)
                        gameEvent.highlight(clicked_box.x , clicked_box.y)

                    # We got ourselves a challanger
                    else:
                        if(gameEvent.validMove(first_piece ,clicked_box, clicked_box.x , clicked_box.y)):
                            print("Different color , a lot of things needs to do")
                            old_x = first_piece.x
                            old_y = first_piece.y
                            for i in pieceList:
                                if i.x == old_x and i.y == old_y:
                                    removePiece = clicked_pieces[0]
                                    pieceList.remove(removePiece)
                                    gameEvent.winCondition(removePiece)
                                    i.x = clicked_box.x
                                    i.y = clicked_box.y
                                    break
                            
                            # then update the board                    
                            gameBoard.updateBoard(pieceList)
                            turnColor = 1 - turnColor 
                            first_piece = None
                
    pygame.display.flip()


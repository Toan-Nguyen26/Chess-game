import pygame
# Chess will have 32 pieces , 16 blacks and 16 whites
# The whites will move first and color = 0, black is 1
class Chess:

  def __init__(self):
    pass
  # Chess pieces have 3 variables : color , x and y cord
  # This functions initialize the chess pieces then put them into a list of 32 pieces total
  def pieces(self):
        self.list = []

        # Adding black pieces first : 8 pawn , 2 rooks , 2 knights , 2 bishop , king and queen
        x = 0
        while x < 640:
            self.list.append(Pawn(1 , x, 80))
            x = x + 80
        
        self.list.append(Rook(1 , 0 , 0))
        self.list.append(Rook(1 , 560 , 0))

        self.list.append(Knight(1 , 80 , 0))
        self.list.append(Knight(1 , 480 , 0))

        self.list.append(Bishop(1 , 160 , 0))
        self.list.append(Bishop(1 , 400 , 0))

        self.list.append(Queen(1 , 240 , 0))
        
        self.list.append(King(1 , 320 , 0))

        # Adding second pieces later : 8 pawn , 2 rooks , 2 knights , 2 bishop , king and queen
        x = 0
        while x < 640:
            self.list.append(Pawn(0 , x, 480))
            x = x + 80
        
        self.list.append(Rook(0 , 0 , 560))
        self.list.append(Rook(0 , 560 , 560))

        self.list.append(Knight(0 , 80 , 560))
        self.list.append(Knight(0 , 480 , 560))

        self.list.append(Bishop(0 , 160 , 560))
        self.list.append(Bishop(0 , 400 , 560))

        self.list.append(Queen(0 , 240 , 560))
        
        self.list.append(King(0 , 320 , 560))

        return self.list

  # take a list then display the pieces on the chessboard
  def displayPieces(self, screen, list):
      for i in list:
        rect_1 = pygame.Rect(i.x, i.y, 80, 80)
        recCenter = i.image.get_rect(center = rect_1.center)
        screen.blit(i.image , recCenter)

      
   # create a list of 32 chess pieces
   # Check for the color of the pieces , white will always move first
  def checkColor(self , color):
    if(color == 0):
      return True
    else:
      return False
  

  def create(self ,color, x ,y):
    self.color = color
    self.x = x
    self.y = y

# validation move, check to see if it's ok or not
class Valid:
  def __init__(self,x , y):
      self.x = x
      self.y = y
  
class Pawn(Chess):
  def __init__(self , color , x , y):
    Chess.create(self, color , x , y)
    self.first = True
    
    if(self.checkColor(color)):
      self.image = pygame.image.load('Images/wPawn.jpg')
    else:
      self.image = pygame.image.load('Images/bPawn.jpg')

  # checked for blocked and if it's the first move of the Pawn , then it can move forward up to two tiles
  def move(self , eatX ,eatY, emptyList):
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
        validMove.append(Valid(self.x, doubleWhiteMove))
      if eatY != whiteMove:
        validMove.append(Valid(self.x, whiteMove))

      # if eatable then do this
      if (eatX == self.x - 80 and eatY == self.y - 80):
        validMove.append(Valid(self.x - 80, self.y - 80))
      if (eatX == self.x + 80 and eatY == self.y - 80):
        validMove.append(Valid(self.x + 80, self.y - 80))

    # If not then it's black
    else:
      if self.first and eatY != doubleBlackMove:
        validMove.append(Valid(self.x, doubleBlackMove))
      if eatY != blackMove:
        validMove.append(Valid(self.x, blackMove))

      # if eatable then do this
      if eatX == self.x + 80 and eatY == self.y + 80:
        validMove.append(Valid(self.x + 80, self.y + 80))
      if eatX == self.x - 80 and eatY == self.y + 80:
        validMove.append(Valid(self.x - 80, self.y + 80))

    # Return the list 
    return validMove
  
  # If the condition were met , turn the rook into either a Queen, Bishop, Knight or Bishop
  def promotion(self):
    pass



class Bishop(Chess):
  def __init__(self , color , x , y):
    Chess.create(self, color , x , y)
    if(self.checkColor(color)):
      self.image = pygame.image.load('Images/wBishop.jpg')
    else:
      self.image = pygame.image.load('Images/bBishop.jpg')
      

  def move(self):
    pass


class Rook(Chess):
  def __init__(self , color , x , y):
    Chess.create(self, color , x , y)
    self.name = 'Rook'
    if(self.checkColor(color)):
      self.image = pygame.image.load('Images/wRook.jpg')
    else:
      self.image = pygame.image.load('Images/bRook.jpg')

  # Rook move willl be all left and right of all direction
  # Haven't check if it's block or not
  def move(self , eatX ,eatY , emptyList):
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
      validMove.append(Valid(bx , self.y))
      bx = bx - 80
    bx = self.x
    xBlock = True

    while bx <= 640 or xBlock == False:
      blocked_piece = [s for s in emptyList if s.x == bx]
      if blocked_piece:
        if blocked_piece[0].color == self.color:
          xBlock = False
      validMove.append(Valid(bx , self.y))
      bx = bx + 80
    bx = self.x
    xBlock = True
    
    # add all going up or down
    while by >= 0 or  xBlock == False:
      blocked_piece = [s for s in emptyList if s.x == bx]
      if blocked_piece:
        if blocked_piece[0].color == self.color:
          xBlock = False
      validMove.append(Valid(self.x , by))
      by = by - 80
    by = self.y
    xBlock = True

    while by <= 640 or xBlock == False:
      blocked_piece = [s for s in emptyList if s.x == bx]
      if blocked_piece:
        if blocked_piece[0].color == self.color:
          xBlock = False
      validMove.append(Valid(self.x , by))
      by = by + 80
      print(by)
    by = self.y
    xBlock = True

    return validMove


class Knight(Chess):
  def __init__(self , color , x , y):
    Chess.create(self, color , x , y)
    self.name = 'Knight'
    if(self.checkColor(color)):
      self.image = pygame.image.load('Images/wKnight.jpg')
    else:
      self.image = pygame.image.load('Images/bKnight.jpg')
    
  def move(self):
    pass


class Queen(Chess):
  def __init__(self , color , x , y):
    Chess.create(self, color , x , y)
    if(self.checkColor(color)):
      self.image = pygame.image.load('Images/wQueen.jpg')
    else:
      self.image = pygame.image.load('Images/bQueen.jpg')

  def move(self):
    pass


class King(Chess):
  def __init__(self , color , x , y):
    Chess.create(self, color , x , y)
    if(self.checkColor(color)):
      self.image = pygame.image.load('Images/wKing.jpg')
    else:
      self.image = pygame.image.load('Images/bKing.jpg')


  def move(self):
    pass



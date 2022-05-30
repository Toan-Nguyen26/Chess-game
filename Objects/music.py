import pygame

class Music:
    def __init__(self):
       
        pygame.init()

        pygame.mixer.init()

        pygame.mixer.music.load('Objects/ost.mp3')

        pygame.mixer.music.play(-1)

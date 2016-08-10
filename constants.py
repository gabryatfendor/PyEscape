import pygame
from pygame.locals import *

FPS = 60  # frames per second to update the screen
WINWIDTH = 800  # width of the program's window, in pixels
WINHEIGHT = 600  # height in pixels
CENTERX = WINWIDTH/2
CENTERY = WINHEIGHT/2

FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 128)

# Images for the 4 directions
charImgs = {'left': pygame.image.load('imgs/left.png'),
            'right': pygame.image.load('imgs/right.png'),
            'up': pygame.image.load('imgs/up.png'),
            'down': pygame.image.load('imgs/down.png')}

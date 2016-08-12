import pygame
from pygame.locals import *

FPS = 60  # frames per second to update the screen
WINWIDTH = 800  # width of the program's window, in pixels
WINHEIGHT = 600  # height in pixels
CENTERX = WINWIDTH/2
CENTERY = WINHEIGHT/2

TILESIDE = 50

SCREENMAXXTILE = WINWIDTH/TILESIDE
SCREENMAXYTILE = WINHEIGHT/TILESIDE
PLAYERXONSCREEN = (SCREENMAXXTILE/2)*TILESIDE
PLAYERYONSCREEN = (SCREENMAXYTILE/2)*TILESIDE
SCREENMAXTILE = SCREENMAXXTILE*SCREENMAXYTILE

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

tiles = {'grass': pygame.image.load('tiles/grass.png'),
         'water': pygame.image.load('tiles/water.png'),
         'tree': pygame.image.load('tiles/tree.png'),
         'wall': pygame.image.load('tiles/wall.png'),
         'outside': pygame.image.load('tiles/outside.png')}

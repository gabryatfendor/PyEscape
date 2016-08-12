import pygame
from pygame.locals import *

pygame.init()
infoObject = pygame.display.Info()
FPS = 60  # frames per second to update the screen
WINWIDTH = infoObject.current_w  # width of the program's window, in pixels
WINHEIGHT = infoObject.current_h  # height in pixels
CENTERX = WINWIDTH/2
CENTERY = WINHEIGHT/2

TILESIDE = 64
EXTRATILES = 2 #extra tiles to draw for not messing up with resolution

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
         'water': [pygame.image.load('tiles/water1.png'),
         		   pygame.image.load('tiles/water2.png')],
         'tree': [pygame.image.load('tiles/tree1.png'),
         		  pygame.image.load('tiles/tree2.png'),
         		  pygame.image.load('tiles/tree3.png')],
         'wall': pygame.image.load('tiles/wall.png'),
         'mountains': pygame.image.load('tiles/mountains.png'),
         'nothing': pygame.image.load('tiles/nothing.png')}

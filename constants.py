import pygame
from pygame.locals import *

pygame.init()
infoObject = pygame.display.Info()
FPS = 60  # frames per second to update the screen
WINWIDTH = 1024  # width of the program's window, in pixels
WINHEIGHT = 768  # height in pixels
CENTERX = WINWIDTH/2
CENTERY = WINHEIGHT/2

TILESIDE = 16
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
charImgs = {'left': pygame.transform.scale(pygame.image.load('imgs/left.png'), (TILESIDE, TILESIDE)),
            'right': pygame.transform.scale(pygame.image.load('imgs/right.png'), (TILESIDE, TILESIDE)),
            'up': pygame.transform.scale(pygame.image.load('imgs/up.png'), (TILESIDE, TILESIDE)),
            'down': pygame.transform.scale(pygame.image.load('imgs/down.png'), (TILESIDE, TILESIDE))}

tiles = {'grass': pygame.transform.scale(pygame.image.load('tiles/grass.png'), (TILESIDE, TILESIDE)),
         'water': [pygame.transform.scale(pygame.image.load('tiles/water1.png'), (TILESIDE, TILESIDE)),
         		   pygame.transform.scale(pygame.image.load('tiles/water2.png'), (TILESIDE, TILESIDE))],
         'tree': [pygame.transform.scale(pygame.image.load('tiles/tree1.png'), (TILESIDE, TILESIDE)),
         		  pygame.transform.scale(pygame.image.load('tiles/tree2.png'), (TILESIDE, TILESIDE)),
         		  pygame.transform.scale(pygame.image.load('tiles/tree3.png'), (TILESIDE, TILESIDE))],
         'wall': pygame.transform.scale(pygame.image.load('tiles/wall.png'), (TILESIDE, TILESIDE)),
         'mountains': pygame.transform.scale(pygame.image.load('tiles/mountains.png'), (TILESIDE, TILESIDE)),
         'nothing': pygame.transform.scale(pygame.image.load('tiles/nothing.png'), (TILESIDE, TILESIDE))}

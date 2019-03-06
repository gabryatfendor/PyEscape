import pygame

from .screen import Screen

class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 128)

class Images:

    charImgs = {'left': pygame.transform.scale(pygame.image.load('imgs/left.png'), (Screen.TILESIDE, Screen.TILESIDE)),
                'right': pygame.transform.scale(pygame.image.load('imgs/right.png'), (Screen.TILESIDE, Screen.TILESIDE)),
                'up': pygame.transform.scale(pygame.image.load('imgs/up.png'), (Screen.TILESIDE, Screen.TILESIDE)),
                'down': pygame.transform.scale(pygame.image.load('imgs/down.png'), (Screen.TILESIDE, Screen.TILESIDE))}

    tiles = {'grass': pygame.transform.scale(pygame.image.load('tiles/grass.png'), (Screen.TILESIDE, Screen.TILESIDE)),
            'water': [pygame.transform.scale(pygame.image.load('tiles/water1.png'), (Screen.TILESIDE, Screen.TILESIDE)),
                    pygame.transform.scale(pygame.image.load('tiles/water2.png'), (Screen.TILESIDE, Screen.TILESIDE))],
            'tree': [pygame.transform.scale(pygame.image.load('tiles/tree1.png'), (Screen.TILESIDE, Screen.TILESIDE)),
                    pygame.transform.scale(pygame.image.load('tiles/tree2.png'), (Screen.TILESIDE, Screen.TILESIDE)),
                    pygame.transform.scale(pygame.image.load('tiles/tree3.png'), (Screen.TILESIDE, Screen.TILESIDE))],
            'wall': pygame.transform.scale(pygame.image.load('tiles/wall.png'), (Screen.TILESIDE, Screen.TILESIDE)),
            'mountains': pygame.transform.scale(pygame.image.load('tiles/mountains.png'), (Screen.TILESIDE, Screen.TILESIDE)),
            'nothing': pygame.transform.scale(pygame.image.load('tiles/nothing.png'), (Screen.TILESIDE, Screen.TILESIDE))}
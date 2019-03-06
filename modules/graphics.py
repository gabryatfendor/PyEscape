""" Data regarding images show in games and graphic in general """

import pygame

from .screen import Screen

class Color:
    """  Colors used in application from pygame library """
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 128)

class Images:
    """ Tiles used in game """
    default = Screen.TILESIDE, Screen.TILESIDE
    charImgs = {'left': pygame.transform.scale(pygame.image.load('imgs/left.png'), default),
                'right': pygame.transform.scale(pygame.image.load('imgs/right.png'), default),
                'up': pygame.transform.scale(pygame.image.load('imgs/up.png'), default),
                'down': pygame.transform.scale(pygame.image.load('imgs/down.png'), default)}

    tiles = {'grass': pygame.transform.scale(pygame.image.load('tiles/grass.png'), default),
             'water': [pygame.transform.scale(pygame.image.load('tiles/water1.png'), default),
                       pygame.transform.scale(pygame.image.load('tiles/water2.png'), default)],
             'tree': [pygame.transform.scale(pygame.image.load('tiles/tree1.png'), default),
                      pygame.transform.scale(pygame.image.load('tiles/tree2.png'), default),
                      pygame.transform.scale(pygame.image.load('tiles/tree3.png'), default)],
             'wall': pygame.transform.scale(pygame.image.load('tiles/wall.png'), default),
             'mountains': pygame.transform.scale(pygame.image.load('tiles/mountains.png'), default),
             'nothing': pygame.transform.scale(pygame.image.load('tiles/nothing.png'), default)}

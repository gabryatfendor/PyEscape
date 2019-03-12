""" Data regarding images show in games and graphic in general """

import pygame

from .screen import Screen

class Color:
    """  Colors used in application from pygame library """
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 128)

class Tiles:
    """ Tiles used in game """
    default = Screen.TILESIDE, Screen.TILESIDE
    default_player = {'left': pygame.transform.scale(pygame.image.load('tiles/player/left.png'), default),
                'right': pygame.transform.scale(pygame.image.load('tiles/player/right.png'), default),
                'up': pygame.transform.scale(pygame.image.load('tiles/player/up.png'), default),
                'down': pygame.transform.scale(pygame.image.load('tiles/player/down.png'), default)}

    environment = {'grass': pygame.transform.scale(pygame.image.load('tiles/environment/grass.png'), default),
             'water': [pygame.transform.scale(pygame.image.load('tiles/environment/water1.png'), default),
                       pygame.transform.scale(pygame.image.load('tiles/environment/water2.png'), default)],
             'tree': [pygame.transform.scale(pygame.image.load('tiles/environment/tree1.png'), default),
                      pygame.transform.scale(pygame.image.load('tiles/environment/tree2.png'), default),
                      pygame.transform.scale(pygame.image.load('tiles/environment/tree3.png'), default)],
             'wall': pygame.transform.scale(pygame.image.load('tiles/environment/wall.png'), default),
             'mountains': pygame.transform.scale(pygame.image.load('tiles/environment/mountains.png'), default),
             'nothing': pygame.transform.scale(pygame.image.load('tiles/environment/nothing.png'), default)}
    
    knight = {'left': pygame.transform.scale(pygame.image.load('tiles/npc/knight_west.png'), default),
                'right': pygame.transform.scale(pygame.image.load('tiles/npc/knight_east.png'), default),
                'up': pygame.transform.scale(pygame.image.load('tiles/npc/knight_north.png'), default),
                'down': pygame.transform.scale(pygame.image.load('tiles/npc/knight_south.png'), default)}
    

""" Data regarding images show in games and graphic in general """

import pygame

from enums.direction import Direction
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
    default_player = {Direction.WEST.name: pygame.transform.scale(pygame.image.load('tiles/player/left.png'), default),
                      Direction.EAST.name: pygame.transform.scale(pygame.image.load('tiles/player/right.png'), default),
                      Direction.NORTH.name: pygame.transform.scale(pygame.image.load('tiles/player/up.png'), default),
                      Direction.SOUTH.name: pygame.transform.scale(pygame.image.load('tiles/player/down.png'), default)}

    environment = {'grass': pygame.transform.scale(pygame.image.load('tiles/environment/grass.png'), default),
                   'water': [pygame.transform.scale(pygame.image.load('tiles/environment/water1.png'), default),
                             pygame.transform.scale(pygame.image.load('tiles/environment/water2.png'), default)],
                   'tree': [pygame.transform.scale(pygame.image.load('tiles/environment/tree1.png'), default),
                            pygame.transform.scale(pygame.image.load('tiles/environment/tree2.png'), default),
                            pygame.transform.scale(pygame.image.load('tiles/environment/tree3.png'), default)],
                   'wall': pygame.transform.scale(pygame.image.load('tiles/environment/wall.png'), default),
                   'mountains': pygame.transform.scale(pygame.image.load('tiles/environment/mountains.png'), default),
                   'nothing': pygame.transform.scale(pygame.image.load('tiles/environment/nothing.png'), default),
                   'exit': pygame.transform.scale(pygame.image.load('tiles/environment/exit.png'), default)}

    knight = {Direction.WEST.name: pygame.transform.scale(pygame.image.load('tiles/npc/knight_west.png'), default),
              Direction.EAST.name: pygame.transform.scale(pygame.image.load('tiles/npc/knight_east.png'), default),
              Direction.NORTH.name: pygame.transform.scale(pygame.image.load('tiles/npc/knight_north.png'), default),
              Direction.SOUTH.name: pygame.transform.scale(pygame.image.load('tiles/npc/knight_south.png'), default)}

class Images:
    """Iamges used in game"""
    image_game_over = pygame.image.load("images/game_over.png")
    image_winner = pygame.image.load("images/winner.jpg")

    @staticmethod
    def center_image(image, screen_width=Screen.WINWIDTH, screen_height=Screen.WINHEIGHT):
        """Return origin with centered image"""
        image_size = image.get_rect().size
        image_middle_x = int(image_size[0]/2)
        image_middle_y = int(image_size[1]/2)
        return [(int(screen_width/2)-image_middle_x), (int(screen_height/2)-image_middle_y)]

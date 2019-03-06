""" Properties concerning the display (dimension, x & y coordinates etc.) """

import pygame

class Screen:
    """ Properties concerning the display """
    WINWIDTH = 1024  # width of the program's window, in pixels
    WINHEIGHT = 768  # height in pixels
    CENTERX = WINWIDTH/2
    CENTERY = WINHEIGHT/2

    TILESIDE = 64
    EXTRATILES = 2 #extra tiles to draw for not messing up with resolution

    MAXXTILE = WINWIDTH/TILESIDE
    MAXYTILE = WINHEIGHT/TILESIDE
    PLAYERXONSCREEN = (MAXXTILE/2)*TILESIDE
    PLAYERYONSCREEN = (MAXYTILE/2)*TILESIDE
    SCREENMAXTILE = MAXXTILE*MAXYTILE

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    
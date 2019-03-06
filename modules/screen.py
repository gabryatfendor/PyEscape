import pygame

class Screen:
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

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))


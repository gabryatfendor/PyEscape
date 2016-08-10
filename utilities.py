import sys, pygame
from pygame.locals import *
from constants import *


def mainMenu():
    #  Title variables
    fontObjTitle = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObjTitle = fontObjTitle.render('PyRPG', True, RED, WHITE)
    textRectObjTitle = textSurfaceObjTitle.get_rect()
    textRectObjTitle.center = (CENTERX, 50)

    #  Subtitle variables
    fontObjSubitle = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObjSubtitle = fontObjSubitle.render('Press Space to Start, H for help', True, BLUE, WHITE)
    textRectObjSubtitle = textSurfaceObjSubtitle.get_rect()
    textRectObjSubtitle.center = (CENTERX, 120)

    menuAppeared = False
    while True:  # the main menu loop
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(textSurfaceObjTitle, textRectObjTitle)
        if menuAppeared:
            DISPLAYSURF.blit(textSurfaceObjSubtitle, textRectObjSubtitle)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE and menuAppeared:
                    DISPLAYSURF.fill(WHITE)
                    return
                elif event.key == K_h:
                    helpMenu()
                if not menuAppeared:
                    menuAppeared = True

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def helpMenu():
    fontObjHelp = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObjHelp = fontObjHelp.render('Press esc to go back in main menu', True, BLACK, WHITE)
    textRectObjHelp = textSurfaceObjHelp.get_rect()
    textRectObjHelp.x = 10
    textRectObjHelp.y = 10 

    while True:  # the main menu loop
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(textSurfaceObjHelp, textRectObjHelp)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    DISPLAYSURF.fill(WHITE)
                    return

        pygame.display.update()
        FPSCLOCK.tick(FPS)		

def terminate():
	pygame.quit()
	sys.exit()
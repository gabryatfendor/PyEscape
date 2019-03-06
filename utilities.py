import sys, pygame
from pygame.locals import *
from modules.screen import Screen
from modules.graphics import Color
from modules.game import Game

def mainMenu():
    #  Title variables
    fontObjTitle = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObjTitle = fontObjTitle.render('PyRPG', True, Color.RED, Color.WHITE)
    textRectObjTitle = textSurfaceObjTitle.get_rect()
    textRectObjTitle.center = (Screen.CENTERX, 50)

    #  Subtitle variables
    fontObjSubitle = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObjSubtitle = fontObjSubitle.render('Press Space to Start, H for help, ESC to exit the game', True, Color.BLUE, Color.WHITE)
    textRectObjSubtitle = textSurfaceObjSubtitle.get_rect()
    textRectObjSubtitle.center = (Screen.CENTERX, 120)

    menuAppeared = False
    while True:  # the main menu loop
        Screen.DISPLAYSURF.fill(Color.WHITE)
        Screen.DISPLAYSURF.blit(textSurfaceObjTitle, textRectObjTitle)
        if menuAppeared:
            Screen.DISPLAYSURF.blit(textSurfaceObjSubtitle, textRectObjSubtitle)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE and menuAppeared:
                    Screen.DISPLAYSURF.fill(Color.WHITE)
                    return
                elif event.key == K_h:
                    helpMenu()
                elif event.key == K_ESCAPE:
                    terminate()
                if not menuAppeared:
                    menuAppeared = True

        pygame.display.update()
        Game.FPSCLOCK.tick(Game.FPS)

# TODO: write something in it
def helpMenu():
    fontObjHelp = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObjHelp = fontObjHelp.render('Press esc to go back in main menu,', True, Color.BLACK, Color.WHITE)
    textRectObjHelp = textSurfaceObjHelp.get_rect()
    textRectObjHelp.x = 10
    textRectObjHelp.y = 10

    while True:  # the main menu loop
        Screen.DISPLAYSURF.fill(Color.WHITE)
        Screen.DISPLAYSURF.blit(textSurfaceObjHelp, textRectObjHelp)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Screen.DISPLAYSURF.fill(Color.WHITE)
                    return

        pygame.display.update()
        Game.FPSCLOCK.tick(Game.FPS)

def terminate():
	pygame.quit()
	sys.exit()

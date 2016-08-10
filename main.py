import sys, os, pygame
from pygame.locals import *
from constants import *
from utilities import mainMenu, terminate, convertMap

def main():

    # Pygame initialization
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    DISPLAYSURF.fill(WHITE)

    pygame.display.set_caption('PyRPG')
    
    mainMenu()
    currentMapFile = open("maps/start.map","r")
    currentMap = convertMap(currentMapFile)
    currentMapFile.close()
    print currentMap
    #write char first time
    imageToDraw = charImgs['up']
    DISPLAYSURF.blit(imageToDraw, (CENTERX, CENTERY))
    while True:
        playerMove = None
        keyPressed = False
        redrawChar = False
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                # Handle key presses
                keyPressed = True
                if event.key == K_LEFT:
                    imageToDraw = charImgs['left']
                    redrawChar = True
                elif event.key == K_RIGHT:
                    imageToDraw = charImgs['right']
                    redrawChar = True
                elif event.key == K_UP:
                    imageToDraw = charImgs['up']
                    redrawChar = True
                elif event.key == K_DOWN:
                    imageToDraw = charImgs['down']
                    redrawChar = True
                elif event.key == K_ESCAPE:
                    terminate()
        if redrawChar == True:
            DISPLAYSURF.blit(imageToDraw, (CENTERX, CENTERY))
        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()

if __name__ == '__main__':
	main()
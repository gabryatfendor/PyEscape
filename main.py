import sys, os, pygame
from pygame.locals import *
from constants import *
from utilities import *
from test import *

def main():

    # Pygame initialization
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    DISPLAYSURF.fill(WHITE)

    pygame.display.set_caption('PyRPG')
    
    mainMenu()

    arrayMap = convertMap("maps/start.map")
    walkabilityMap = createWalkabilityMap(arrayMap)
    if TESTING:
        compareWalkabilityMap(arrayMap, walkabilityMap)
    tileMap = convertMapToTile(arrayMap)
    playerCoordinate = setPlayerStartingPoint(arrayMap)
    xToDraw = (TILESIDE * playerCoordinate[0]) + OFFSETX
    yToDraw = (TILESIDE * playerCoordinate[1]) + OFFSETY
    #write char first time
    charToDraw = charImgs['up']
    DISPLAYSURF.blit(charToDraw, (CENTERX, CENTERY))
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                # Handle key presses
                if event.key == K_LEFT:
                    if(walkabilityMap[playerCoordinate[0]-1][playerCoordinate[1]]):
                        charToDraw = charImgs['left']
                        xToDraw -= TILESIDE
                        playerCoordinate[0]-=1
                elif event.key == K_RIGHT:
                    if(walkabilityMap[playerCoordinate[0]+1][playerCoordinate[1]]):
                        charToDraw = charImgs['right']
                        xToDraw += TILESIDE
                        playerCoordinate[0]+=1
                elif event.key == K_UP:
                    if(walkabilityMap[playerCoordinate[0]][playerCoordinate[1]-1]):
                        charToDraw = charImgs['up']
                        yToDraw -= TILESIDE
                        playerCoordinate[1]-=1
                elif event.key == K_DOWN:
                    if(walkabilityMap[playerCoordinate[0]][playerCoordinate[1]+1]):
                        charToDraw = charImgs['down']
                        yToDraw += TILESIDE
                        playerCoordinate[1]+=1
                elif event.key == K_ESCAPE:
                    terminate()
        drawMap(tileMap)
        DISPLAYSURF.blit(charToDraw, (xToDraw, yToDraw))
        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()

if __name__ == '__main__':
	main()
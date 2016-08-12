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
    playerCoordinate = setPlayerStartingPoint("maps/start.map")
    walkabilityMap = createWalkabilityMap(arrayMap)
    if TESTING:
        compareWalkabilityMap(arrayMap, walkabilityMap)
    tileMap = convertMapToTile(arrayMap)
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
                    charToDraw = charImgs['left']
                    if(walkabilityMap[playerCoordinate[0]-1][playerCoordinate[1]]):
                        xToDraw -= TILESIDE
                        playerCoordinate[0]-=1
                elif event.key == K_RIGHT:
                    charToDraw = charImgs['right']
                    if(walkabilityMap[playerCoordinate[0]+1][playerCoordinate[1]]):
                        xToDraw += TILESIDE
                        playerCoordinate[0]+=1
                elif event.key == K_UP:
                    charToDraw = charImgs['up']
                    if(walkabilityMap[playerCoordinate[0]][playerCoordinate[1]-1]):
                        yToDraw -= TILESIDE
                        playerCoordinate[1]-=1
                elif event.key == K_DOWN:
                    charToDraw = charImgs['down']
                    if(walkabilityMap[playerCoordinate[0]][playerCoordinate[1]+1]):
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
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
    mapDimension = [len(arrayMap[0]),len(arrayMap)]
    print "Map loaded, dimension %r" % mapDimension
    playerCoordinate = setPlayerStartingPoint("maps/start.map")
    walkabilityMap = createWalkabilityMap(arrayMap)
    tileMap = convertMapToTile(arrayMap)
    
    #write char first time
    charToDraw = charImgs['down']
    while True:
        for event in pygame.event.get(): # event handling loop
            DISPLAYSURF.fill(WHITE)
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                # Handle key presses
                if event.key == K_LEFT:
                    charToDraw = charImgs['left']
                    if(walkabilityMap[playerCoordinate[0]-1][playerCoordinate[1]]):
                        playerCoordinate[0]-=1
                elif event.key == K_RIGHT:
                    charToDraw = charImgs['right']
                    if(walkabilityMap[playerCoordinate[0]+1][playerCoordinate[1]]):
                        playerCoordinate[0]+=1
                elif event.key == K_UP:
                    charToDraw = charImgs['up']
                    if(walkabilityMap[playerCoordinate[0]][playerCoordinate[1]-1]):
                        playerCoordinate[1]-=1
                elif event.key == K_DOWN:
                    charToDraw = charImgs['down']
                    if(walkabilityMap[playerCoordinate[0]][playerCoordinate[1]+1]):
                        playerCoordinate[1]+=1
                elif event.key == K_ESCAPE:
                    terminate()
        drawMap(tileMap,playerCoordinate, charToDraw, mapDimension)
        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()

if __name__ == '__main__':
	main()
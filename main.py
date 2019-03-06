import pygame

from pygame.locals import *
from modules.game import Game
from modules.screen import Screen
from modules.graphics import Color, Images
from modules.map import *
from utilities import mainMenu, terminate

def main():

    # Pygame initialization
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    Screen.DISPLAYSURF.fill(Color.WHITE)

    pygame.display.set_caption('PyRPG')

    # Draw the main menu
    mainMenu()

    arrayMap = convertMap("maps/start.map")
    mapDimension = [len(arrayMap[0]),len(arrayMap)]
    print ("Map loaded, dimension %r" % mapDimension)
    playerCoordinate = setPlayerStartingPoint("maps/start.map")
    walkabilityMap = createWalkabilityMap(arrayMap)
    tileMap = convertMapToTile(arrayMap)

    #write char first time
    charToDraw = Images.charImgs['down']
    while True:
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            charToDraw = Images.charImgs['left']
            if(walkabilityMap[playerCoordinate[0]-1][playerCoordinate[1]]):
                playerCoordinate[0]-=1
        elif keys[K_RIGHT]:
            charToDraw = Images.charImgs['right']
            if(walkabilityMap[playerCoordinate[0]+1][playerCoordinate[1]]):
                playerCoordinate[0]+=1
        elif keys[K_UP]:
            charToDraw = Images.charImgs['up']
            if(walkabilityMap[playerCoordinate[0]][playerCoordinate[1]-1]):
                playerCoordinate[1]-=1
        elif keys[K_DOWN]:
            charToDraw = Images.charImgs['down']
            if(walkabilityMap[playerCoordinate[0]][playerCoordinate[1]+1]):
                playerCoordinate[1]+=1
        for event in pygame.event.get(): # event handling loop
            Screen.DISPLAYSURF.fill(Color.WHITE)
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                # Handle key presses
                if event.key == K_ESCAPE:
                    terminate()
        drawMap(tileMap,playerCoordinate, charToDraw, mapDimension, Images.tiles['mountains'])
        pygame.display.update() # draw DISPLAYSURF to the screen.
        Game.FPSCLOCK.tick()

if __name__ == '__main__':
	main()

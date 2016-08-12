import sys, pygame, random
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
    textSurfaceObjSubtitle = fontObjSubitle.render('Press Space to Start, H for help, ESC to exit the game', True, BLUE, WHITE)
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
                elif event.key == K_ESCAPE:
                    terminate()
                if not menuAppeared:
                    menuAppeared = True

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def helpMenu():
    fontObjHelp = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObjHelp = fontObjHelp.render('Press esc to go back in main menu,', True, BLACK, WHITE)
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

def convertMap(filepath):
#MAP IS SAVED BY COLUMN
    arrayToReturn = []
    mapStarted = False
    with open(filepath, "r") as ins:
        lineArray = []
        for line in ins:
            if(mapStarted):
                lineArray.append(line)
            if(line == "*\n"):
                mapStarted = True

    for line in lineArray:
        arrayToReturn.append(line[:-1])
    return zip(*arrayToReturn)

def convertMapToTile(mapArray):
    tileArray = []
    tileColumn = []
    for column in mapArray:
        for char in column:
            if char == ' ':
                tileColumn.append(tiles['grass'])
            elif char == 'W':
                tileColumn.append(random.choice(tiles['water']))
            elif char == 'T':
                tileColumn.append(random.choice(tiles['tree']))
            elif char == '#':
                tileColumn.append(tiles['wall'])
            elif char == '-':
                tileColumn.append(tiles['nothing'])
        tileArray.append(tileColumn)
        tileColumn = []
                
    return tileArray

def drawMap(tileArray,coord,charImg,mapDimension,outsideTile):
    columnToDraw = []
    mapToDraw = []
    for i in xrange(coord[0]-(SCREENMAXXTILE/2),coord[0]+(SCREENMAXXTILE/2)+EXTRATILES):
        for j in xrange(coord[1]-(SCREENMAXYTILE/2),coord[1]+(SCREENMAXYTILE/2)+EXTRATILES):
            if i<0 or j<0 or i>mapDimension[1]-1 or j>mapDimension[0]-1:
                columnToDraw.append(outsideTile)
            else:
                columnToDraw.append(tileArray[i][j])  
        mapToDraw.append(columnToDraw)
        columnToDraw = []
    x = 0
    y = 0
    for i,column in enumerate(mapToDraw):
        for j,tile in enumerate(mapToDraw[i]):
            DISPLAYSURF.blit(tile, (x, y))
            y += TILESIDE
        x += TILESIDE
        y = 0
    DISPLAYSURF.blit(charImg, (PLAYERXONSCREEN, PLAYERYONSCREEN))

def setPlayerStartingPoint(filepath):
    start = None
    with open(filepath, "r") as ins:
        for i,line in enumerate(ins):
            if i == 0:
                start = line.split('=',1)[-1].strip()

    playerPos = [int(x) for x in start.split(',') if x.strip().isdigit()]

    return playerPos

def createWalkabilityMap(mapArray):
    mapToReturn = []
    columnToAppend = []
    for column in mapArray:
        for char in column:
            if char == ' ':
                columnToAppend.append(True)
            else:
                columnToAppend.append(False)
        mapToReturn.append(columnToAppend)
        columnToAppend = []
    return mapToReturn
                
def terminate():
	pygame.quit()
	sys.exit()
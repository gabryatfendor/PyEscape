import random

from .screen import Screen
from .graphics import Color, Images

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
    return list(zip(*arrayToReturn))

# Convert every single char from the configuration in the path to the tile to be drawn
def convertMapToTile(mapArray):
    tileArray = []
    tileColumn = []
    for column in mapArray:
        for char in column:
            if char == ' ':
                tileColumn.append(Images.tiles['grass'])
            elif char == 'W':
                tileColumn.append(random.choice(Images.tiles['water']))
            elif char == 'T':
                tileColumn.append(random.choice(Images.tiles['tree']))
            elif char == '#':
                tileColumn.append(Images.tiles['wall'])
            elif char == '-':
                tileColumn.append(Images.tiles['nothing'])
        tileArray.append(tileColumn)
        tileColumn = []

    return tileArray

def drawMap(tileArray,coord,charImg,mapDimension,outsideTile):
    columnToDraw = []
    mapToDraw = []
    Screen.DISPLAYSURF.fill(Color.WHITE) # This is to avoid overlapping of Images.tiles
    for i in range(int(coord[0])-int((Screen.SCREENMAXXTILE/2)),int(coord[0])+int((Screen.SCREENMAXXTILE//2))+Screen.EXTRATILES):
        for j in range(int(coord[1])-int((Screen.SCREENMAXYTILE/2)),int(coord[1])+int((Screen.SCREENMAXYTILE//2))+Screen.EXTRATILES):
            if i<0 or j<0 or i>mapDimension[1]-1 or j>mapDimension[0]-1:
                columnToDraw.append(outsideTile) # Out of map bound
            else:
                columnToDraw.append(tileArray[i][j])
        mapToDraw.append(columnToDraw)
        columnToDraw = []
    x = 0
    y = 0
    for i,column in enumerate(mapToDraw):
        for j,tile in enumerate(mapToDraw[i]):
            Screen.DISPLAYSURF.blit(tile, (x, y))
            y += Screen.TILESIDE
        x += Screen.TILESIDE
        y = 0
    Screen.DISPLAYSURF.blit(charImg, (Screen.PLAYERXONSCREEN, Screen.PLAYERYONSCREEN))

# Read the player starting point from the map file and set the starting coordinate
def setPlayerStartingPoint(filepath):
    start = None
    with open(filepath, "r") as ins:
        for i,line in enumerate(ins):
            if i == 0:
                start = line.split('=',1)[-1].strip()

    playerPos = [int(x) for x in start.split(',') if x.strip().isdigit()]

    return playerPos

# Write the walkability map to be used when we move the char
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

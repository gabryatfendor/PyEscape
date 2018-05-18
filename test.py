import sys, os, pygame
from pygame.locals import *
from constants import *
from utilities import *

def compareWalkabilityMap(arrayMap, walkabilityMap):
	for i,row in enumerate(arrayMap):
		for j,char in enumerate(row):
			print("Analysing %s,%s" % (i,j))
			if char == ' ':
				if walkabilityMap[i][j] == False:
					print("Error!")
			else:
				if walkabilityMap[i][j] == True:
					print("Error!")

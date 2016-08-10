import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 60 # frames per second to update the screen
WINWIDTH = 800 # width of the program's window, in pixels
WINHEIGHT = 600 # height in pixels
CENTERX = WINWIDTH/2
CENTERY = WINHEIGHT/2


#Color 
WHITE = (255, 255, 255)

#Images for the 4 directions
charImgs = {'left' : pygame.image.load('imgs/left.png'),
            'right': pygame.image.load('imgs/right.png'),
            'up'   : pygame.image.load('imgs/up.png'),
            'down' : pygame.image.load('imgs/down.png')}

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

    # Pygame initialization
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    DISPLAYSURF.fill(WHITE)

    pygame.display.set_caption('PyRPG')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    while True:
        playerMove = None
        imageToDraw = None
        keyPressed = False
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                # Player clicked the "X" at the corner of the window.
                terminate()
            elif event.type == KEYDOWN:
                # Handle key presses
                keyPressed = True
                if event.key == K_LEFT:
                    imageToDraw = charImgs['left']
                elif event.key == K_RIGHT:
                    imageToDraw = charImgs['right']
                elif event.key == K_UP:
                    imageToDraw = charImgs['up']
                elif event.key == K_DOWN:
                    imageToDraw = charImgs['down']
        if keyPressed == True:
            DISPLAYSURF.blit(imageToDraw, (CENTERX, CENTERY))
        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()

def terminate():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()
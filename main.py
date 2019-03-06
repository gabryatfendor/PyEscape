""" File containing the main game loop """
import pygame

from modules.game import Game
from modules.screen import Screen
from modules.graphics import Color, Images
from modules.map import import_map, convert_map_to_tile, draw_walk_map, draw_map, set_char_start
from utilities import main_menu, terminate

def main():
    """ Main method containing initialization and game loop (maybe split it?)"""
    # Pygame initialization
    pygame.init()
    Screen.DISPLAYSURF.fill(Color.WHITE)

    pygame.display.set_caption('PyRPG')

    # Draw the main menu
    main_menu()

    array_map = import_map("maps/start.map")
    map_dimension = [len(array_map[0]), len(array_map)]
    print("Map loaded, dimension %r" % map_dimension)
    player_coord = set_char_start("maps/start.map")
    walkability_map = draw_walk_map(array_map)
    tile_map = convert_map_to_tile(array_map)

    #write char first time
    char_to_draw = Images.charImgs['down']
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            char_to_draw = Images.charImgs['left']
            if walkability_map[player_coord[0]-1][player_coord[1]]:
                player_coord[0] -= 1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            char_to_draw = Images.charImgs['right']
            if walkability_map[player_coord[0]+1][player_coord[1]]:
                player_coord[0] += 1
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            char_to_draw = Images.charImgs['up']
            if walkability_map[player_coord[0]][player_coord[1]-1]:
                player_coord[1] -= 1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            char_to_draw = Images.charImgs['down']
            if walkability_map[player_coord[0]][player_coord[1]+1]:
                player_coord[1] += 1
        for event in pygame.event.get(): # event handling loop
            Screen.DISPLAYSURF.fill(Color.WHITE)
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                # Handle key presses
                if event.key == pygame.K_ESCAPE:
                    terminate()
        draw_map(tile_map, player_coord, char_to_draw, map_dimension, Images.tiles['mountains'])
        pygame.display.update() # draw DISPLAYSURF to the screen.
        Game.FPSCLOCK.tick()

if __name__ == '__main__':
    main()

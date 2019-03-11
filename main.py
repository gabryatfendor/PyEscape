""" File containing the main game loop """
import pygame
from modules.game import Game, Menu
from modules.screen import Screen
from modules.graphics import Color
from modules.map import Map

def main():
    """ Main method containing initialization and game loop (maybe split it?)"""
    # Pygame initialization
    pygame.init()
    Screen.DISPLAYSURF.fill(Color.WHITE)
    game_object = Game()
    main_menu = Menu()
    map_object = Map()

    pygame.display.set_caption('PyRPG')

    # Draw the main menu
    main_menu.main_menu()

    array_map = map_object.import_map("maps/lvl_01.map")
    map_dimension = [len(array_map[0]), len(array_map)]
    print("Map loaded, dimension {}".format(map_dimension))
    player_coord = map_object.set_char_start("maps/lvl_01.map")
    walkability_map = map_object.draw_walk_map(array_map)
    tile_map = map_object.convert_map_to_tile(array_map)
    game_object.main_loop(walkability_map, player_coord, tile_map, map_dimension)

if __name__ == '__main__':
    main()

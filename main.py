""" File containing the main game loop """
import pygame
from modules.game import Game, Menu
from modules.screen import Screen
from modules.graphics import Color
from modules.map import Map
from modules.ai import Npc

def main():
    """ Main method containing initialization and game loop (maybe split it?)"""
    # Pygame initialization
    pygame.init()
    Screen.DISPLAYSURF.fill(Color.WHITE)
    game_object = Game()
    main_menu = Menu()
    pygame.display.set_caption('PyRPG')

    # Draw the main menu
    main_menu.main_menu()

    array_map = Map.import_map("maps/lvl_01.map")
    map_dimension = [len(array_map[0]), len(array_map)]
    print("Map loaded, dimension {}".format(map_dimension))
    player_coord = Map.set_char_start("maps/lvl_01.map")
    # This data will need to be saved somewhere else and not hardcoded
    npc_coords = [[11, 5], [5, 3]]
    npc_array = Npc.create_npc_array(npc_coords)
    walkability_map = Map.draw_walk_map(array_map, npc_array)
    tile_map = Map.convert_map_to_tile(array_map)
    game_object.main_loop(walkability_map, player_coord, tile_map, map_dimension, npc_array)

if __name__ == '__main__':
    main()

""" File containing the main game loop """
import pygame
from modules.game import Game, Menu
from modules.screen import Screen
from modules.graphics import Color

def main():
    """ Main method containing initialization and game loop"""
    # Pygame initialization
    pygame.init()

    Screen.DISPLAYSURF.fill(Color.WHITE)
    pygame.display.set_caption('PyRPG')

    # Draw the main menu
    Menu.main_menu()

    game_object = Game()
    game_object.LEVEL_LIST = Game.load_level_list("maps/")

    for level in game_object.LEVEL_LIST:
        game_object.main_loop(level)

if __name__ == '__main__':
    main()

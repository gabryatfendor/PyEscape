""" File containing the main game loop """
import pygame
from modules.game import Game, Menu
from modules.screen import Screen
from modules.graphics import Color
from modules.audio import Music

def main():
    """ Main method containing initialization and game loop"""
    # Pygame initialization
    pygame.init()

    Screen.DISPLAYSURF.fill(Color.WHITE)
    pygame.display.set_caption('PyRPG')

    # Music starts
    pygame.mixer.init()
    Music.play_music(Music.background_music, True, 0.4)

    # Draw the main menu
    Menu.main_menu()
    replay = True

    while replay:
        game_object = Game()
        game_object.game_setup()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    pass
                elif event.key == pygame.K_n:
                    replay = False
                    break

if __name__ == '__main__':
    main()

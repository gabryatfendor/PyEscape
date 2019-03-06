""" Common method to be used in the application """

import sys
import pygame
from modules.screen import Screen
from modules.graphics import Color
from modules.game import Game
from modules.strings import Menu

def main_menu():
    """ Menu printed before starting the game """
    #  Title variables
    font_title = pygame.font.Font('freesansbold.ttf', 32)
    surface_title = font_title.render('PyRPG', True, Color.RED, Color.WHITE)
    rect_title = surface_title.get_rect()
    rect_title.center = (Screen.CENTERX, 50)

    #  Subtitle variables
    font_subtitle = pygame.font.Font('freesansbold.ttf', 18)
    surface_subtitle = font_subtitle.render(Menu.menu_intro, True, Color.BLUE, Color.WHITE)
    rect_subtitle = surface_subtitle.get_rect()
    rect_subtitle.center = (Screen.CENTERX, 120)

    has_menu_appeared = False
    while True:  # the main menu loop
        Screen.DISPLAYSURF.fill(Color.WHITE)
        Screen.DISPLAYSURF.blit(surface_title, rect_title)
        if has_menu_appeared:
            Screen.DISPLAYSURF.blit(surface_subtitle, rect_subtitle)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and has_menu_appeared:
                    Screen.DISPLAYSURF.fill(Color.WHITE)
                    return
                elif event.key == pygame.K_h:
                    help_menu()
                elif event.key == pygame.K_ESCAPE:
                    terminate()
                if not has_menu_appeared:
                    has_menu_appeared = True

        pygame.display.update()
        Game.FPSCLOCK.tick(Game.FPS)

# TODO: write something in it
def help_menu():
    """ Screen that appears whenever help is triggered """
    font_obj_help = pygame.font.Font('freesansbold.ttf', 18)
    text_surface_obj_help = font_obj_help.render(Menu.menu_exit, True, Color.BLACK, Color.WHITE)
    text_rect_obj_help = text_surface_obj_help.get_rect()
    text_rect_obj_help.x = 10
    text_rect_obj_help.y = 10

    while True:  # the main menu loop
        Screen.DISPLAYSURF.fill(Color.WHITE)
        Screen.DISPLAYSURF.blit(text_surface_obj_help, text_rect_obj_help)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Screen.DISPLAYSURF.fill(Color.WHITE)
                    return

        pygame.display.update()
        Game.FPSCLOCK.tick(Game.FPS)

def terminate():
    """ Exit from the game """
    pygame.quit()
    sys.exit()

""" Game common properties """
import sys
import pygame
from .graphics import Color, Tiles
from .screen import Screen
from .map import Map
from .strings import Common
from .ai import Npc

class Game:
    """ Game common utilities """
    FPS = 60  # frames per second to update the screen

    def main_loop(self, walk_matrix, player_coords, tile_matrix, dimension, npc_array):
        """ Main game loop """
        clock = pygame.time.Clock()
        npc_move_event = pygame.USEREVENT + 1
        pygame.time.set_timer(npc_move_event, Npc.NPC_MOVE_SPEED)

        #write char first time
        background_tile = Map.set_background("maps/lvl_01.map")
        char_to_draw = Map.set_char_start_orientation("maps/lvl_01.map")

        while True:
            clock.tick(self.FPS)

            if pygame.event.get(pygame.QUIT):
                break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.terminate()

            player_coords = Game.move_player(keys, player_coords, walk_matrix)
            char_to_draw = Game.change_orientation_tile(keys, char_to_draw)
            for event in pygame.event.get(): # event handling loop
                if event.type == npc_move_event:
                    print("I like to move move")

            Map.draw_map(tile_matrix, player_coords, char_to_draw, dimension, background_tile, npc_array)
            pygame.display.update() # draw DISPLAYSURF to the screen.

        self.terminate()

    @staticmethod
    def move_player(keys, player_coords, walk_matrix):
        """Change coords after key pressing from player"""
        new_player_coords = player_coords
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if walk_matrix[player_coords[0]-1][player_coords[1]]:
                new_player_coords[0] -= 1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if walk_matrix[player_coords[0]+1][player_coords[1]]:
                new_player_coords[0] += 1
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if walk_matrix[player_coords[0]][player_coords[1]-1]:
                new_player_coords[1] -= 1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if walk_matrix[player_coords[0]][player_coords[1]+1]:
                new_player_coords[1] += 1
        return new_player_coords

    @staticmethod
    def change_orientation_tile(keys, original_orientation_img):
        """Change tile due to new orientation"""
        char_to_draw = original_orientation_img
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            char_to_draw = Tiles.default_player['left']
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            char_to_draw = Tiles.default_player['right']
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            char_to_draw = Tiles.default_player['up']
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            char_to_draw = Tiles.default_player['down']
        return char_to_draw

    def terminate(self):
        """ Exit from the game """
        pygame.quit()
        sys.exit()

class Menu:
    """ Main game menu """
    def main_menu(self):
        """ Menu printed before starting the game """
        #  Title variables
        font_title = pygame.font.Font('freesansbold.ttf', 32)
        surface_title = font_title.render('PyRPG', True, Color.RED, Color.WHITE)
        rect_title = surface_title.get_rect()
        rect_title.center = (Screen.CENTERX, 50)

        #  Subtitle variables
        font_subtitle = pygame.font.Font('freesansbold.ttf', 18)
        surface_subtitle = font_subtitle.render(Common.menu_intro, True, Color.BLUE, Color.WHITE)
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
                        self.help_menu()
                    elif event.key == pygame.K_ESCAPE:
                        Game.terminate(Game)
                    if not has_menu_appeared:
                        has_menu_appeared = True

            pygame.display.update()

    # TODO: write something in it
    def help_menu(self):
        """ Screen that appears whenever help is triggered """
        font_obj = pygame.font.Font('freesansbold.ttf', 18)
        text_surface_obj = font_obj.render(Common.menu_exit, True, Color.BLACK, Color.WHITE)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.x = 10
        text_rect_obj.y = 10

        while True:  # the main menu loop
            Screen.DISPLAYSURF.fill(Color.WHITE)
            Screen.DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Screen.DISPLAYSURF.fill(Color.WHITE)
                        return

            pygame.display.update()

""" Game common properties """
import os
import sys
import pygame

from enums.direction import Direction
from .graphics import Color, Tiles
from .screen import Screen
from .map import Map
from .strings import Common
from .ai import Npc
from .level import Level

class Game:
    """ Game common utilities """
    FPS = 60  # frames per second to update the screen
    PLAYER_MOVE_SPEED = int(FPS * 2)
    LEVEL_LIST = []

    def main_loop(self, level):
        """ Main game loop """
        game_over = False
        print("Entering \"{}\"".format(level.name))
        clock = pygame.time.Clock()
        npc_move_event = pygame.USEREVENT + 1
        player_move_event = pygame.USEREVENT + 2

        pygame.time.set_timer(npc_move_event, Npc.NPC_MOVE_SPEED)
        pygame.time.set_timer(player_move_event, Game.PLAYER_MOVE_SPEED)

        #write char first time
        char_to_draw = Tiles.default_player[level.player_direction]

        while True:
            clock.tick(self.FPS)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                Game.terminate()

            for event in pygame.event.get(): # event handling loop
                if event.type == npc_move_event:
                    level.npc_array = Npc.move_npc(level.npc_array, level.walkability_map)
                if event.type == player_move_event:
                    level.player_coords = Game.move_player(keys, level.player_coords, level.walkability_map)
                    char_to_draw = Game.change_orientation_tile(keys, char_to_draw)
                if event.type == pygame.QUIT:
                    Game.terminate()

            for npc in level.npc_array:
                if npc.check_collision(level):
                    Game.game_over()
                    game_over = True
                    return game_over
            if level.player_coords == level.exit_coords:
                print("You escaped \"{}\"".format(level.name))
                break

            Map.draw_map(level, char_to_draw)
            pygame.display.update() # draw DISPLAYSURF to the screen.
        return game_over

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
            char_to_draw = Tiles.default_player[Direction.WEST.name]
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            char_to_draw = Tiles.default_player[Direction.EAST.name]
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            char_to_draw = Tiles.default_player[Direction.NORTH.name]
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            char_to_draw = Tiles.default_player[Direction.SOUTH.name]
        return char_to_draw

    @staticmethod
    def load_level_list(level_directory):
        """Load all .map files in level_directory"""
        level_list = []
        for level_path in sorted(os.listdir(level_directory)):
            current_level = Level(level_directory + level_path, Direction.SOUTH.name, 'mountains')
            current_level.name = Level.set_level_name(os.path.splitext(level_path)[0])
            level_list.append(current_level)
        return level_list

    @staticmethod
    def game_over():
        """Handling death"""
        print("GAME OVER BITCH")

    @staticmethod
    def terminate():
        """ Exit from the game """
        print("Quitting...")
        pygame.quit()
        sys.exit()

class Menu:
    """ Main game menu """

    @staticmethod
    def main_menu():
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
                        Menu.help_menu()
                    elif event.key == pygame.K_ESCAPE:
                        Game.terminate()
                    if not has_menu_appeared:
                        has_menu_appeared = True

            pygame.display.update()

    @staticmethod
    def help_menu():
        """ Screen that appears whenever help is triggered """
        font_obj = pygame.font.Font('freesansbold.ttf', 18)
        text_surface_obj = font_obj.render(Common.menu_help_body_line1, True, Color.BLACK, Color.WHITE)
        text_surface_obj_2 = font_obj.render(Common.menu_help_body_line2, True, Color.BLACK, Color.WHITE)
        text_surface_obj_exit = font_obj.render(Common.menu_help_exit, True, Color.BLACK, Color.WHITE)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj_2 = text_surface_obj_2.get_rect()
        text_rect_obj_exit = text_surface_obj_exit.get_rect()
        text_rect_obj.x = 10
        text_rect_obj.y = 10
        text_rect_obj_exit.x = 10
        text_rect_obj_2.x = 10
        text_rect_obj_2.y = 40
        text_rect_obj_exit.y = 100

        while True:  # the main menu loop
            Screen.DISPLAYSURF.fill(Color.WHITE)
            Screen.DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
            Screen.DISPLAYSURF.blit(text_surface_obj_2, text_rect_obj_2)
            Screen.DISPLAYSURF.blit(text_surface_obj_exit, text_rect_obj_exit)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Screen.DISPLAYSURF.fill(Color.WHITE)
                        return

            pygame.display.update()

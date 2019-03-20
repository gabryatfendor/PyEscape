"""Game common properties"""
import os
import sys
import pygame

from enums.direction import Direction
from .graphics import Color, Tiles, Images
from .screen import Screen
from .map import Map
from .strings import Common
from .ai import Npc
from .level import Level
from .audio import Sound

class Game:
    """Game common utilities"""
    FPS = 60  #frames per second to update the screen
    player_move_speed = int(FPS * 2)
    level_list = []

    def game_setup(self):
        """Method to recall the game if game_over or win"""
        self.level_list = Game.load_level_list("maps/")
        levels_won = 0
        enemy_speed = Menu.difficulty_menu()
        for level in self.level_list:
            current_level_won = self.main_loop(level, int(Game.FPS * enemy_speed))
            if current_level_won:
                levels_won += 1
            else:
                break

        if levels_won == len(self.level_list):
            Game.youre_winner()
        else:
            Game.game_over()

    def main_loop(self, level, enemy_speed):
        """Main game loop"""
        game_won = True
        print("Entering \"{}\"".format(level.name))
        clock = pygame.time.Clock()
        npc_move_event = pygame.USEREVENT + 1
        player_move_event = pygame.USEREVENT + 2

        pygame.time.set_timer(npc_move_event, enemy_speed)
        pygame.time.set_timer(player_move_event, Game.player_move_speed)

        #starting tile orientation for player
        char_to_draw = Tiles.default_player[level.player_direction]

        while True:
            clock.tick(self.FPS)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                Game.terminate()

            for event in pygame.event.get(): #event handling loop
                if event.type == npc_move_event:
                    level.npc_array = Npc.move_npc(level.npc_array, level.walkability_map)
                if event.type == player_move_event:
                    level.player_coords = Game.move_player(keys, level.player_coords, level.walkability_map)
                    char_to_draw = Game.change_orientation_tile(keys, char_to_draw)
                if event.type == pygame.QUIT:
                    Game.terminate()

            for npc in level.npc_array:
                if npc.check_collision(level):
                    game_won = False
                    return game_won
            if level.player_coords == level.exit_coords:
                print("You escaped \"{}\"".format(level.name))
                break

            Map.draw_map(level, char_to_draw)
            pygame.display.update() #draw displaye_surface to the screen.

        return game_won

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
    def game_over():
        """Handling death"""
        game_over_centered = Images.center_image(Images.image_game_over)
        while True:
            Screen.display_surface.fill(Color.BLACK)
            Screen.display_surface.blit(Images.image_game_over, (game_over_centered[0], game_over_centered[1]))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
                if event.type == pygame.QUIT:
                    Game.terminate()

            pygame.display.update()

    @staticmethod
    def load_level_list(level_directory):
        """Load all .map files in level_directory"""
        level_list = []
        for level_path in sorted(os.listdir(level_directory)):
            #TODO: the next line shouldn't have hard coded parameters
            current_level = Level(level_directory + level_path, Direction.SOUTH.name, 'mountains')
            current_level.name = Level.set_level_name(os.path.splitext(level_path)[0])
            level_list.append(current_level)
        return level_list

    @staticmethod
    def move_player(keys, player_coords, walk_matrix):
        """Change coords after key pressing from player"""
        new_player_coords = player_coords
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if walk_matrix[player_coords[0]-1][player_coords[1]]:
                new_player_coords[0] -= 1
            else:
                Sound.play_sound(Sound.sound_walk_against_wall, 0.40)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if walk_matrix[player_coords[0]+1][player_coords[1]]:
                new_player_coords[0] += 1
            else:
                Sound.play_sound(Sound.sound_walk_against_wall, 0.40)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if walk_matrix[player_coords[0]][player_coords[1]-1]:
                new_player_coords[1] -= 1
            else:
                Sound.play_sound(Sound.sound_walk_against_wall, 0.40)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if walk_matrix[player_coords[0]][player_coords[1]+1]:
                new_player_coords[1] += 1
            else:
                Sound.play_sound(Sound.sound_walk_against_wall, 0.40)
        return new_player_coords

    @staticmethod
    def terminate():
        """Exit from the game"""
        print("Quitting...")
        pygame.quit()
        sys.exit()

    @staticmethod
    def youre_winner():
        """Handling winning"""
        winner_centered = Images.center_image(Images.image_winner)
        print(winner_centered)
        while True:
            Screen.display_surface.fill(Color.BLACK)
            Screen.display_surface.blit(Images.image_winner, (winner_centered[0], winner_centered[1]))
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    Game.terminate()

            pygame.display.update()

class Menu:
    """Class to handle different menus"""

    @staticmethod
    def difficulty_menu():
        """Menu printed to choose difficulty """
        font = pygame.font.Font('freesansbold.ttf', 18)
        surface = font.render(Common.menu_difficulty, True, Color.BLUE, Color.WHITE)
        rect = surface.get_rect()
        rect.center = (Screen.center_x, 120)

        while True:
            Screen.display_surface.fill(Color.WHITE)
            Screen.display_surface.blit(surface, rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 25
                    elif event.key == pygame.K_2:
                        return 20
                    elif event.key == pygame.K_3:
                        return 15
                    elif event.key == pygame.K_4:
                        return 10
                    elif event.key == pygame.K_5:
                        return 5
                if event.type == pygame.QUIT:
                    Game.terminate()

            pygame.display.update()

    @staticmethod
    def help_menu():
        """Screen that appears whenever help is triggered"""
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

        while True:  #the main menu loop
            Screen.display_surface.fill(Color.WHITE)
            Screen.display_surface.blit(text_surface_obj, text_rect_obj)
            Screen.display_surface.blit(text_surface_obj_2, text_rect_obj_2)
            Screen.display_surface.blit(text_surface_obj_exit, text_rect_obj_exit)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Screen.display_surface.fill(Color.WHITE)
                        return

            pygame.display.update()

    @staticmethod
    def main_menu():
        """Menu printed before starting the game """
        #Title variables
        font_title = pygame.font.Font('freesansbold.ttf', 32)
        surface_title = font_title.render('PyRPG', True, Color.RED, Color.WHITE)
        rect_title = surface_title.get_rect()
        rect_title.center = (Screen.center_x, 50)

        #Subtitle variables
        font_subtitle = pygame.font.Font('freesansbold.ttf', 18)
        surface_subtitle = font_subtitle.render(Common.menu_intro, True, Color.BLUE, Color.WHITE)
        rect_subtitle = surface_subtitle.get_rect()
        rect_subtitle.center = (Screen.center_x, 120)

        has_menu_appeared = False
        while True:  #the main menu loop
            Screen.display_surface.fill(Color.WHITE)
            Screen.display_surface.blit(surface_title, rect_title)
            if has_menu_appeared:
                Screen.display_surface.blit(surface_subtitle, rect_subtitle)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and has_menu_appeared:
                        Screen.display_surface.fill(Color.WHITE)
                        return
                    elif event.key == pygame.K_h:
                        Menu.help_menu()
                    elif event.key == pygame.K_ESCAPE:
                        Game.terminate()
                    if not has_menu_appeared:
                        has_menu_appeared = True
                if event.type == pygame.QUIT:
                    Game.terminate()

            pygame.display.update()

""" Module containing methods related to map creation/import/conversion """

import random

from .screen import Screen
from .graphics import Color, Tiles

class Map:
    """ Everything regarding the game map """

    @staticmethod
    def import_map(file_path):
        """ Importing map from file line by line """
        array_to_return = []
        map_started = False
        with open(file_path, "r") as ins:
            line_array = []
            for line in ins:
                if map_started:
                    line_array.append(line)
                if line == "*\n":
                    map_started = True

        for line in line_array:
            array_to_return.append(line[:-1])
        return list(zip(*array_to_return))

    @staticmethod
    def convert_map_to_tile(map_array):
        """ Convert every single char from the configuration in the path to the tile to be drawn """
        tile_array = []
        tile_column = []
        for column in map_array:
            for char in column:
                if char == ' ':
                    tile_column.append(Tiles.environment['grass'])
                elif char == 'W':
                    tile_column.append(random.choice(Tiles.environment['water']))
                elif char == 'T':
                    tile_column.append(random.choice(Tiles.environment['tree']))
                elif char == '#':
                    tile_column.append(Tiles.environment['wall'])
                elif char == '-':
                    tile_column.append(Tiles.environment['nothing'])
            tile_array.append(tile_column)
            tile_column = []

        return tile_array

    def draw_map(self, tile_array, player_coords, char_img, map_dimension, outside_tile, npc_array):
        """ Map rendering from imported file """
        column_to_draw = []
        map_to_draw = []
        Screen.DISPLAYSURF.fill(Color.WHITE) # This is to avoid overlapping of tiles
        max_x = Screen.MAXXTILE
        max_y = Screen.MAXYTILE
        extra_space = Screen.EXTRATILES

        rendered_array_width = range(int(player_coords[0])-int((max_x/2)), int(player_coords[0])+int((max_x//2))+extra_space)
        rendered_array_height = range(int(player_coords[1])-int((max_y/2)), int(player_coords[1])+int((max_y//2))+extra_space)
        # using as center player coordinates (since player is always drawn in the center) we draw only data from the array
        for i in rendered_array_width:
            for j in rendered_array_height:
                # up to max_x or max_y. If we have any index values that goes negative or over the limit, we print background
                if i < 0 or j < 0 or i > map_dimension[1]-1 or j > map_dimension[0]-1:
                    column_to_draw.append(outside_tile) # Out of map bound
                else:
                    column_to_draw.append(tile_array[i][j])
            map_to_draw.append(column_to_draw)
            column_to_draw = []
        row = 0
        column = 0

        for line in map_to_draw:
            for tile in line:
                Screen.DISPLAYSURF.blit(tile, (row, column))
                column += Screen.TILESIDE
            row += Screen.TILESIDE
            column = 0

        # the player is always drawn in the center of the screen (PLAYERXONSCREEN, PLAYERYONSCREEN)
        # we do this at the end to overwrite the floor in player's place
        Screen.DISPLAYSURF.blit(char_img, (Screen.PLAYERXONSCREEN, Screen.PLAYERYONSCREEN))

        # to print npc in the correct place we convert the coords they have in the array with the screen coordinates
        # (screen is always a subset of the map).
        for npc in npc_array:
            if npc.x in rendered_array_width and npc.y in rendered_array_height:
                render_coordinate = self.arr_coord_to_render_coord(npc.x, npc.y, rendered_array_width, rendered_array_height)
                Screen.DISPLAYSURF.blit(npc.current_tile, (render_coordinate[0] * Screen.TILESIDE, render_coordinate[1] * Screen.TILESIDE))

    def arr_coord_to_render_coord(self, npc_x, npc_y, rendered_array_width, rendered_array_height):
        """Converting map array coordinates to actual rendering coordinate"""
        x_rendered = 0
        y_rendered = 0
        for idx, i in enumerate(rendered_array_width):
            if i == npc_x:
                x_rendered = idx
        for idx, j in enumerate(rendered_array_height):
            if j == npc_y:
                y_rendered = idx

        return [x_rendered, y_rendered]

    @staticmethod
    def set_char_start(file_path):
        """ Read the player starting point from the map file and set the starting coordinate """
        start = None
        with open(file_path, "r") as ins:
            for line in ins:
                if line.startswith("START"):
                    start = line.split('=', 1)[-1].strip()

        player_pos = [int(x) for x in start.split(',') if x.strip().isdigit()]

        return player_pos

    @staticmethod
    def set_char_start_orientation(file_path):
        """ Read from map file player initial direction and return image """
        direction = None
        image = None
        with open(file_path, "r") as ins:
            for line in ins:
                if line.startswith("DIRECTION"):
                    direction = line.split('=', 1)[-1].strip()

        if direction == "N":
            image = Tiles.default_player['up']
        elif direction == "S":
            image = Tiles.default_player['down']
        elif direction == "W":
            image = Tiles.default_player['left']
        elif direction == "E":
            image = Tiles.default_player['right']

        return image

    @staticmethod
    def set_background(file_path):
        """ Read from map file background tile """
        background_string = None
        image = None
        with open(file_path, "r") as ins:
            for line in ins:
                if line.startswith("BACKGROUND"):
                    background_string = line.split('=', 1)[-1].strip()

        image = Tiles.environment[background_string]
        return image

    @staticmethod
    def draw_walk_map(map_array, npc_array):
        """ Write the walkability map to be used when we move the char directly from the array map imported from the file (nothing dynamic in it) """
        map_to_return = []
        column_to_append = []
        for column in map_array:
            for char in column:
                if char == ' ':
                    column_to_append.append(True)
                else:
                    column_to_append.append(False)
            map_to_return.append(column_to_append)
            column_to_append = []

        #Overwrite with false where we have enemies
        for npc in npc_array:
            map_to_return[npc.x][npc.y] = False

        return map_to_return

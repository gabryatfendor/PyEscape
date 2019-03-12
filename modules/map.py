""" Module containing methods related to map creation/import/conversion """

import random

from .screen import Screen
from .graphics import Color, Tiles

class Map:
    """ Everything regarding the game map """

    def import_map(self, file_path):
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

    def convert_map_to_tile(self, map_array):
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

        #print("range for i -> {}, {}".format(int(player_coords[0])-int((max_x/2)), int(player_coords[0])+int((max_x//2))+extra_space))
        #print("range for j -> {}, {}".format(int(player_coords[1])-int((max_y/2)), int(player_coords[1])+int((max_y//2))+extra_space))
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

        for npc in npc_array:
            if npc.x in rendered_array_width and npc.y in rendered_array_height:
                offset = self.set_npc_offset(rendered_array_width, rendered_array_height, map_dimension)
                Screen.DISPLAYSURF.blit(npc.current_tile, ((npc.x + offset[0]) * Screen.TILESIDE, (npc.y + offset[1]) * Screen.TILESIDE))

    def set_npc_offset(self, rendered_array_widht, rendered_array_height, map_dimension):
        x_offset = 0
        y_offset = 0
        for i in rendered_array_widht:
            if i < 0:
                x_offset += 1
            elif i > map_dimension[1]-1:
                x_offset -= 1
        for j in rendered_array_height:
            if j < 0:
                y_offset += 1
            elif j > map_dimension[0]-1:
                y_offset -= 1

        return [x_offset, y_offset]

    def set_char_start(self, file_path):
        """ Read the player starting point from the map file and set the starting coordinate """
        start = None
        with open(file_path, "r") as ins:
            for line in ins:
                if line.startswith("START"):
                    start = line.split('=', 1)[-1].strip()

        player_pos = [int(x) for x in start.split(',') if x.strip().isdigit()]

        return player_pos

    def set_char_start_orientation(self, file_path):
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

    def set_background(self, file_path):
        """ Read from map file background tile """
        background_string = None
        image = None
        with open(file_path, "r") as ins:
            for line in ins:
                if line.startswith("BACKGROUND"):
                    background_string = line.split('=', 1)[-1].strip()

        image = Tiles.environment[background_string]
        return image

    def draw_walk_map(self, map_array):
        """ Write the walkability map to be used when we move the char """
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
        return map_to_return

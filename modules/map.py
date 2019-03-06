""" Module containing methods related to map creation/import/conversion """

import random

from .screen import Screen
from .graphics import Color, Images

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

def convert_map_to_tile(map_array):
    """ Convert every single char from the configuration in the path to the tile to be drawn """
    tile_array = []
    tile_column = []
    for column in map_array:
        for char in column:
            if char == ' ':
                tile_column.append(Images.tiles['grass'])
            elif char == 'W':
                tile_column.append(random.choice(Images.tiles['water']))
            elif char == 'T':
                tile_column.append(random.choice(Images.tiles['tree']))
            elif char == '#':
                tile_column.append(Images.tiles['wall'])
            elif char == '-':
                tile_column.append(Images.tiles['nothing'])
        tile_array.append(tile_column)
        tile_column = []

    return tile_array

def draw_map(tile_array, coord, char_img, map_dimension, outside_tile):
    """ Map rendering from imported file """
    column_to_draw = []
    map_to_draw = []
    Screen.DISPLAYSURF.fill(Color.WHITE) # This is to avoid overlapping of tiles
    max_x = Screen.MAXXTILE
    max_y = Screen.MAXYTILE
    extra_space = Screen.EXTRATILES

    for i in range(int(coord[0])-int((max_x/2)), int(coord[0])+int((max_x//2))+extra_space):
        for j in range(int(coord[1])-int((max_y/2)), int(coord[1])+int((max_y//2))+extra_space):
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
    Screen.DISPLAYSURF.blit(char_img, (Screen.PLAYERXONSCREEN, Screen.PLAYERYONSCREEN))

def set_char_start(file_path):
    """ Read the player starting point from the map file and set the starting coordinate """
    start = None
    with open(file_path, "r") as ins:
        for i, line in enumerate(ins):
            if i == 0:
                start = line.split('=', 1)[-1].strip()

    player_pos = [int(x) for x in start.split(',') if x.strip().isdigit()]

    return player_pos

def draw_walk_map(map_array):
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

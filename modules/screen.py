"""Properties concerning the display (dimension, x & y coordinates etc.)"""
import pygame

class Screen:
    """Properties concerning the display """
    win_width = 1024  #width of the program's window, in pixels
    win_height = 768  #height in pixels
    center_x = win_width/2
    center_y = win_height/2

    tile_side_length = 64
    extra_tile_space = 2 #extra tiles to draw for not messing up with resolution

    max_tile_x_axis = win_width/tile_side_length
    max_tile_y_axis = win_height/tile_side_length
    player_x_coord_on_screen = (max_tile_x_axis/2)*tile_side_length
    player_y_coord_on_screen = (max_tile_y_axis/2)*tile_side_length
    max_tile_on_screen = max_tile_x_axis*max_tile_y_axis

    display_surface = pygame.display.set_mode((win_width, win_height))
    
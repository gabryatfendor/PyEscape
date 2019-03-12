"""Data related to entities not controlled by the player"""

from .screen import Screen

class Npc:
    """Class for non playable character in game"""
    def __init__(self, x, y, tile_array):
        """Initializer with coordinates and tile"""
        self.x = x
        self.y = y
        self.tile_array = tile_array
        self.current_tile = tile_array['right']

    def move(self, new_x, new_y, direction):
        """Set new position for NPC"""
        self.x = new_x
        self.y = new_y
        if direction == 'e':
            self.current_tile = self.tile_array['right']
        elif direction == 'w':
            self.current_tile = self.tile_array['left']
        elif direction == 'n':
            self.current_tile = self.tile_array['up']
        elif direction == 's':
            self.current_tile = self.tile_array['down']

"""Data related to entities not controlled by the player"""

from .graphics import Tiles

class Npc:    
    """Class for non playable character in game"""
    NPC_MOVE_SPEED = 3000

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

    @staticmethod
    def create_npc_array(npc_coords):
        """Given a coords array, istantiate npcs"""
        npc_array = []

        #instantiate npcs
        for tuples in npc_coords:
            new_npc = Npc(tuples[0], tuples[1], Tiles.knight)
            npc_array.append(new_npc)

        return npc_array

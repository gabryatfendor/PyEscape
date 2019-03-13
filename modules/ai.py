"""Data related to entities not controlled by the player"""

from random import randint
from .graphics import Tiles

class Npc:
    """Class for non playable character in game"""
    NPC_MOVE_SPEED = 1000

    def __init__(self, x, y, tile_array):
        """Initializer with coordinates and tile"""
        self.x = x
        self.y = y
        self.tile_array = tile_array
        self.current_tile = tile_array['right']

    @staticmethod
    def move_npc(npc_array, walk_matrix):
        """Change x and y of every npc"""
        for npc in npc_array:
            direction = randint(1, 4)
            if direction == 1:
                npc.current_tile = npc.tile_array['up']
                if walk_matrix[npc.x][npc.y-1]: #north
                    walk_matrix[npc.x][npc.y] = True
                    walk_matrix[npc.x][npc.y-1] = False
                    npc.y -= 1
            elif direction == 2:
                npc.current_tile = npc.tile_array['right']
                if walk_matrix[npc.x+1][npc.y]: #east
                    walk_matrix[npc.x][npc.y] = True
                    walk_matrix[npc.x+1][npc.y] = False
                    npc.x += 1
            elif direction == 3:
                npc.current_tile = npc.tile_array['down']
                if walk_matrix[npc.x][npc.y+1]: #south
                    walk_matrix[npc.x][npc.y] = True
                    walk_matrix[npc.x][npc.y+1] = False
                    npc.y += 1
            elif direction == 4:
                npc.current_tile = npc.tile_array['left']
                if walk_matrix[npc.x-1][npc.y]: #west
                    walk_matrix[npc.x][npc.y] = True
                    walk_matrix[npc.x-1][npc.y] = False
                    npc.x -= 1
        return [npc_array, walk_matrix]

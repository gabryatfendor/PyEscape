"""Data related to entities not controlled by the player"""
import random
from enums.direction import Direction

class Npc:
    """Class for non playable character in game"""

    def __init__(self, x, y, tile_array):
        """Initializer with coordinates and tile"""
        self.x_coord = x
        self.y_coord = y
        self.tile_array = tile_array
        self.current_tile = tile_array[Direction.EAST.name]

    def check_collision(self, level):
        """If NPC is on the same spot of player at any time, game over!"""
        collided = False
        if self.x_coord == level.player_coords[0] and self.y_coord == level.player_coords[1]:
            collided = True
        return collided

    @staticmethod
    def move_npc(npc_array, walk_matrix):
        """Change x and y of every npc"""
        for npc in npc_array:
            direction = random.choice(list(Direction))
            npc.current_tile = npc.tile_array[direction.name]
            if direction.name == Direction.NORTH.name:
                if walk_matrix[npc.x_coord][npc.y_coord-1]:
                    npc.y_coord -= 1
            elif direction.name == Direction.EAST.name:
                if walk_matrix[npc.x_coord+1][npc.y_coord]:
                    npc.x_coord += 1
            elif direction.name == Direction.SOUTH.name:
                if walk_matrix[npc.x_coord][npc.y_coord+1]:
                    npc.y_coord += 1
            elif direction.name == Direction.WEST.name:
                if walk_matrix[npc.x_coord-1][npc.y_coord]:
                    npc.x_coord -= 1
        return npc_array

"""Enumerator handling the 4 possible directions"""

from enum import Enum

class Direction(Enum):
    """Every cardinal direction is converted to a number"""
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

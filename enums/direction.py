"""Enumerator handling the 4 possible cardinal points"""
from enum import Enum

class Direction(Enum):
    """Every cardinal point is converted to a number"""
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

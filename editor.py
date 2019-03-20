"""Graphical editor to create and modify levels"""
from modules.game import Game

def main():
    """Loading maps"""
    levels = Game.load_level_list("maps/")
    print("Levels currently loaded:")
    for level in levels:
        print(level.name)


if __name__ == '__main__':
    main()

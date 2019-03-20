"""Graphical editor to create and modify levels"""
from modules.game import Game

def main():
    """Loading maps"""
    levels = Game.load_level_list("maps/")
    print("Levels currently loaded:")
    for level in levels:
        print(level.name)
        print_level(level.level_path)

def print_level(level_path):
    with open(level_path, "r") as ins:
        line_array = []
        for line in ins:
            line_array.append(line)
    for line in line_array:
        print(line)

if __name__ == '__main__':
    main()

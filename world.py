"""This script is used to create the world for the game"""
# __author__ = James Eaton
# __date__ = 2/16/20
# pylint: disable=C0301
# pylint: disable=R0903

import tiles

WORLD = {}
STARTING_POSITION = (0, 0)

def load_tiles():
    """Function to load the tiles and create the world"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()

    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == "StartingRoom":
                global STARTING_POSITION
                STARTING_POSITION = (x, y)
            WORLD[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)


def tile_exists(x, y):
    """Function to determine if the specified tile exists"""
    return WORLD.get((x,y))

# Name: Dominic Broley
# Class: CS30 Quint 4
# Date: April 29, 2021
# Description: Game
# Adapted code from https://github.com/kynite/FishingRPG


from player import Player

player = Player(1, 1)


class MapTile:
    """Parent Class to child classes"""
    def __init__(self, x, y):
        # The X position of map tiles
        self.x = x
        # the Y position of map tiles
        self.y = y

    def __str__(self):
        """Gets the name of the child class and makes it a string"""
        return self.name


class forest(MapTile):
    """Location with ninja and chicken"""
    def __init__(self, x, y):
        self.name = "forest"
        # Position of the forest tile
        super().__init__(x, y)


class mountain(MapTile):
    """Location with zombie and steak"""
    def __init__(self, x, y):
        self.name = "mountain"
        # Position of the mountain tile
        super().__init__(x, y)


class farm(MapTile):
    """Location with apple and axe"""
    def __init__(self, x, y):
        self.name = "farm"
        # Position of the farm tile
        super().__init__(x, y)


class cave(MapTile):
    """Location with a skeleton and zombie"""
    def __init__(self, x, y):
        self.name = "cave"
        # Position of the cave tile
        super().__init__(x, y)


class barrier(MapTile):
    """Location with the end"""
    def __init__(self, x, y):
        self.name = "barrier"
        # Position of the barrier tile
        super().__init__(x, y)


class end(MapTile):
    """Location with the end"""
    def __init__(self, x, y):
        self.name = "end"
        # Position of the end tile
        super().__init__(x, y)


# The World Map
world_map = [[barrier(0, 0), barrier(1, 0), barrier(2, 0)],
             [barrier(3, 0), barrier(4, 0)],
             [barrier(0, 1), player, None, cave(3, 1), barrier(4, 1)],
             [barrier(0, 2), forest(1, 2), None],
             [mountain(3, 2), barrier(4, 2)],
             [barrier(0, 3), farm(1, 3), None],
             [end(3, 3), barrier(4, 3)],
             [barrier(0, 4), barrier(1, 4), barrier(2, 4)],
             [barrier(3, 4), barrier(4, 4)]]

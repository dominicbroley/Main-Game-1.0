from player import Player

player = Player(1, 2)

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


class mountain(MapTile):
    """Location with axe and apples"""
    def __init__(self, x, y):
        self.name = "mountain"
        # Position of the mountain tile
        super().__init__(x, y)

class farm(MapTile):
    """Location with axe and apples"""
    def __init__(self, x, y):
        self.name = "farm"
        # Position of the farm tile
        super().__init__(x, y)

class forest(MapTile):
    """Location with ninja and chicken"""
    def __init__(self, x, y):
        self.name = "forest"
        # Position of the forest tile
        super().__init__(x, y)

class cave(MapTile):
    """Location with field"""
    def __init__(self, x, y):
        self.name = "cave"
        # Position of the cave tile
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

class end(MapTile):
    """Location with the end"""
    def __init__(self, x, y):
        self.name = "end"
        # Position of the end tile
        super().__init__(x, y)


# The World Map
world_map = [[Player, mountain(1,0), farm(2,0)],
            [forest(0, 1), cave(1, 1), mountain(2,1)],
            [farm(0,2), cave(2, 2), end(2,2)]]

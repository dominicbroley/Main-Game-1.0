# Name: Dominic Broley
# Class: CS30 Quint 4
# Date: April 16, 2021
# Description: RPG Modules and Maps


# Imported Items
from gameinfo import player_one
from gameinfo import zombie
from gameinfo import skeleton
from gameinfo import ninja
from gameinfo import chicken
from gameinfo import steak
from gameinfo import apple
from gameinfo import axe
from gameinfo import forest
from gameinfo import farm
from gameinfo import cave
from gameinfo import mountain


# Printing Imported Items Verification
print("Imported Items: ")
print(player_one)
print(zombie)
print(skeleton)
print(ninja)
print(chicken)
print(steak)
print(apple)
print(axe)
print(forest)
print(farm)
print(cave)
print(mountain)


# Layout of the  9 tiles map
tile_1 = [farm, player_one, apple, axe]
tile_2 = [mountain, zombie, steak]
tile_3 = [farm, apple, axe]
tile_4 = [forest, ninja, chicken]
tile_5 = [cave, skeleton, zombie]
tile_6 = [mountain, zombie, steak]
tile_7 = [farm, apple, axe]
tile_8 = [cave, skeleton, zombie]
tile_9 = [forest, ninja, chicken]


# tiles grouped into Map
print("\nMap with each tile's information\n")
Map = [tile_1, tile_2, tile_3,
       tile_4, tile_5, tile_6,
       tile_7, tile_8, tile_9]
# prints the map information
print(Map)

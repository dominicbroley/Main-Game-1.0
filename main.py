# Name: Dominic Broley
# Class: CS30 Quint 4
# Date: April 30, 2021
# Description: Final RPG Game Assigment
# Adapted code from https://github.com/kynite/FishingRPG


# World and user information imported to main file
import world
from world import *
from player import Player
import places as pl


# Allows movement around the map
def location():
    global world_map
    """Commands that allow for movement on the map"""
    # While loop for continous play
    while True:
        # Instructions explaining how to move and quit
        print("\n\nType 'quit' to quit at any time.")
        print("\nThe map is a 3x3 tile grid. You begin in the top left.")
        print("The end of the map is the bottom right. Good Luck!")
        print("Which direction would you like to travel in?")
        print("Type one of the following: 'north', 'east', 'south', 'west'.")
        # Allows the user to move in one of the four directions
        user = input('You have chosen: ')
        # Makes all user inputs lower cased to match if statements
        user = user.lower()
        # Checks if the user types 'north'
        if user == 'north':
            # Finds user in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # If the object is a user, then move north
                    if isinstance(object, Player):
                        if isinstance(world.world_map[y - 1][x], cave):
                            pl.cave()
                        elif isinstance(world.world_map[y - 1][x], barrier):
                            pl.barrier()
                        elif isinstance(world.world_map[y - 1][x], farm):
                            pl.farm()
                        elif isinstance(world.world_map[y - 1][x], forest):
                            pl.forest()
                        elif isinstance(world.world_map[y - 1][x], mountain):
                            pl.mountain()
                        elif isinstance(world.world_map[y - 1][x], end):
                            pl.end()
                        else:
                            # Moves the user in the north
                            world.world_map[y - 1][x] = object
                            # Replaces tile with no value
                            world.world_map[y][x] = None
                            # Reloads the location call to continue the map
                            location()
                            # Returns the new y value/user position
                            return
        # Checks to see if user typed in movement command
        elif user == 'east':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move east
                    if isinstance(object, Player):
                        # Checks to see if the Player is going to move into
                        # another object and runs something else
                        if isinstance(world.world_map[y][x + 1], cave):
                            pl.cave()
                        elif isinstance(world.world_map[y][x + 1], barrier):
                            pl.barrier()
                        elif isinstance(world.world_map[y][x + 1], farm):
                            pl.farm()
                        elif isinstance(world.world_map[y][x + 1], forest):
                            pl.forest()
                        elif isinstance(world.world_map[y][x + 1], mountain):
                            pl.mountain()
                        elif isinstance(world.world_map[y][x + 1], end):
                            pl.end()
                        else:
                            # moves the player east
                            world.world_map[y][x + 1] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        # Checks to see if user typed in movement command
        elif user == 'south':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move south
                    if isinstance(object, Player):
                        # Checks to see if the Player is going to move into
                        # another object and runs something else
                        if isinstance(world.world_map[y + 1][x], cave):
                            pl.cave()
                        elif isinstance(world.world_map[y + 1][x], barrier):
                            pl.barrier()
                        elif isinstance(world.world_map[y + 1][x], farm):
                            pl.farm()
                        elif isinstance(world.world_map[y + 1][x], forest):
                            pl.forest()
                        elif isinstance(world.world_map[y + 1][x], mountain):
                            pl.mountain()
                        elif isinstance(world.world_map[y + 1][x], end):
                            pl.end()
                        else:
                            # moves the player south
                            world.world_map[y + 1][x] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        elif user == 'west':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move west
                    if isinstance(object, Player):
                        # Checks to see if the Player is going to move into
                        # another object and runs something else
                        if isinstance(world.world_map[y][x - 1], cave):
                            pl.cave()
                        elif isinstance(world.world_map[y][x - 1], barrier):
                            pl.barrier()
                        elif isinstance(world.world_map[y][x - 1], farm):
                            pl.farm()
                        elif isinstance(world.world_map[y][x - 1], forest):
                            pl.forest()
                        elif isinstance(world.world_map[y][x - 1], mountain):
                            pl.mountain()
                        elif isinstance(world.world_map[y][x - 1], end):
                            pl.end()
                        else:
                            # moves the player west
                            world.world_map[y][x - 1] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        elif user == 'quit':
            break
        else:
            print('Invalid Option')

location()

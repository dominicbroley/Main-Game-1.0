# Name: Dominic Broley
# Class: CS30 Quint 4
# Date: April 26, 2021
# Description: RPG Class Assignment
# Adapted code from https://github.com/kynite/FishingRPG


# World and user information imported to main file
import world
from player import Player


# Game only breaks when you move south and east after leaving the map
def location():
    global world_map
    """Commands that allow for movement on the map"""
    # While loop for continous play
    while True:
        # Instructions explaining how to move and quit
        print("\n\nType 'quit' to quit at any time.")
        print("\nMap is a 3x3 tile grid and you begin in the bottom middle.")
        print("If you leave the map boundaries, it will no longer work.")
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
                        # Moves the user in north direction
                            world.world_map[y - 1][x] = object
                            # Replaces tile with no value
                            world.world_map[y][x] = None
                            # Reloads the location call to continue the map
                            location()
                            # Returns the new y value or user position
                            return
        # Checks if the user types 'east'
        elif user == 'east':
            # Finds user in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # If the object is a user, then move east
                    if isinstance(object, Player):
                            # Moves the user in east direction
                            world.world_map[y][x + 1] = object
                            # Replaces tile with no value
                            world.world_map[y][x] = None
                            # Reloads the location call to continue the map
                            location()
                            # Returns the new y value/user position
                            return
        # Checks if the user types 'south'
        elif user == 'south':
            # Finds user in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # If the object is a user, then move south
                    if isinstance(object, Player):
                            # Moves the user in south direction
                            world.world_map[y + 1][x] = object
                            # Replaces tile with no value
                            world.world_map[y][x] = None
                            # Reloads the location call to continue the map
                            location()
                            # Returns the new y value/ user position
                            return
        # Checks if the user types 'west'
        elif user == 'west':
            # Finds user in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # If the object is a user, then move west
                    if isinstance(object, Player):
                        # Moves the user in west direction
                            world.world_map[y][x - 1] = object
                            # Replaces tile with no value
                            world.world_map[y][x] = None
                            # Reloads the location call to continue the map
                            location()
                            # Returns the new y value/ user position
                            return
        elif user == 'quit':
            break
        else:
            print('\nInvalid Command, please try again and check spelling.')
location()

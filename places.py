# Name: Dominic Broley
# Class: CS30 Quint 4
# Date: April 29, 2021
# Description: Game
# Adapted code from https://github.com/kynite/FishingRPG


from world import player
from enemy import *


def cave():
    while True:
        print("You enter a cave and a skeleton approaches you!")
        print("Would you like to 'fight' or 'leave'?")
        print("(Leaving will put you back on the previous tile.)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Skeleton())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Prints error message if user doesn't type a reconized command
        else:
            print("Invalid Input")


def forest():
    while True:
        print("You enter a forest and a skeleton rises from the ground")
        print("Would you like to [fight] or [leave]?")
        print("(Leaving will put you back on the previous tile.)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Skeleton())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Prints error message if user doesn't type reconized command
        else:
            print("Invalid Input")


def mountain():
    while True:
        print("You climb the mountain and a ninja approaches you.")
        print("Would you like to [fight] or [leave]?")
        print("(Leaving will put you back on the previous tile.)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Ninja())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Prints error message if user doesn't type reconized command
        else:
            print("Invalid Input")


def farm():
    while True:
        print("You walk into a farm and there is no enemies.")
        print("Would you like to [fight] or [leave]")
        print("(Leaving will put you back on the previous tile.)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            print("There is no one to fight")
        # Checks to see if user typed leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed quit
        elif action == "quit":
            break
        # Prints error message if user doesn't type reconized command
        else:
            print("Invalid Input")


def barrier():
    while True:
      print("\nThis is the edge of the map, please go another way.")
      print("Leaving will put you back on the previous tile.")
      action = input("Type 'leave' to return to previous tile. ")
      # checks to see if user typed leave
      if action == "leave":
        print("You are back on the previous tile.")
        break
      # checks to see if user type quit
      elif action == "quit":
        break
      # Prints error message if user doesn't type reconized command
      else:
        print("Invalid Input")


def end():
    while True:
        print("You have completed the game. Type 'win' to win!")
        print("(Leaving will put you on the previous tile.)")
        action = input("choose an action: ")
        # Checks to see if user typed in win
        if action == "win":
            quit()
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Prints error message if user doesn't type reconized command
        else:
            print("Invalid Input")

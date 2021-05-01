# Name: Dominic Broley
# Class: CS30 Quint 4
# Date: April 29, 2021
# Description: Game
# Adapted code from https://github.com/kynite/FishingRPG


class Enemy():
    """Parent class of Enemies determining name and health"""
    def __init__(self):
        # Creates a warning to not create raw enemies
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        """Gets the name of the child class and makes it a string"""
        return self.name


class Zombie(Enemy):
    """A hungry rotten zombie"""
    def __init__(self):
        # Name of the enemy
        self.name = "Zombie"
        # Amount of health the enemy has
        self.hp = 10
        # Damage the enemy does to player
        self.damage = 3


class Skeleton(Enemy):
    """A boney skeleton"""
    def __init__(self):
        # Name of the enemy
        self.name = "Skeleton"
        # Amount of health the enemy has
        self.hp = 20
        # Damage the enemy does to player
        self.damage = 8


class ninja(Enemy):
    """A stealthy ninja"""
    def __init__(self):
        # Name of the enemy
        self.name = "Ninja"
        # Amount of health the enemy has
        self.hp = 30
        # Damage the enemy does to player
        self.damage = 10

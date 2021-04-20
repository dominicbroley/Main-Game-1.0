# dictionaries of the characters
player_one = {
    "Player_one:":
    {"health": 100, "damage": 10,
    "description": "You."
}}
zombie = {
    "Zombie:":
    {"health": 20, "damage": 5,
    "description": "Blood thristy."
}}
skeleton = {
    "Skeleton:":
    {"health": 15, "damage": 2.5,
    "description": "Weakened skeleton that still moves around."
}}
ninja = {
    "Ninja:":
    {"health": 30, "damage": 8,
    "description": "A fast, stealthy, and deadly ninja."
}}
# puts the characters into a list
characters = [player_one, zombie, skeleton, ninja]
# dictionaries of the inventory items
chicken = {
    "Chicken":
    {"healing": 10,
    "description": "A tasty cooked chicken."
}}
steak = {
    "Steak":
    {"healing": 25,
    "description": "A very tasty and replenishing cooked piece of steak."
}}
apple = {
    "Apple":
    {"healing": 5,
    "description": "Shiny red apple."
}}
axe = {
    "Axe":
    {"damage": 10,
    "description": "A heavy and strong weapon."
}}
# puts the inventory items into a list
inventory = [chicken, steak, apple, axe]
# dicionaries of the locations
forest = {
    "Forest":
    {"enemy": "zombie",
    "description": "Zombies roam around hungry in dark forests."
}}
farm = {
    "Farm":
    {"food": "apple",
    "descritpion": "Plenty of apple trees."
}}
cave = {
    "Cave":
    {"enemy": "skeleton",
    "description": "A dark and scary place."
}}
mountain = {
    "Mountain":
    {"food": "berry",
    "description": "Plenty of berry bushes."
}}

#import character.txt
# import room.py 
# import game.py
# import save_load.py
# import commands.py
#import json
#from room import Library
#import player
#from commands import Commands
#from save_load import save_game, load_game
import commands
import room

class Player:
    def __init__(self, name, house, strength, weakness):
        self.name = name
        self.house = house
        self.strength = strength
        self.weakness = weakness
        self.inventory = [] # keeps track of what the player has collected in the game
        self.lives = 3 # the given lifes, affected by lost trials in the rooms

    @property
    def Name(self):
        return self.name

    @property
    def House(self):
        return self.house

    @property
    def Strength(self):
        return self.strength

    @property
    def Weakness(self):
        return self.weakness

    @property
    def Inventory(self):
        return ",".join(self.inventory)

    @property
    def Lives(self):
        return self.lives

    def lives_lost(self, damage,current_lives):
        self.damage=damage #initially 3, how can i make it take damage and then minus it from current lives
        #self.current_lives=lives
        if self.damage>0:
            self.current_lives-self.damage
            # self.current_lives-=1
        print(f'{self.name} takes {self.damage}!! Remaining lives are {self.current_lives}')

    def add_items(self, item ):
        self.inventory.append(item)
        print(f'{item} has been added to the inventory')

    def remove_items(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        print(f'{item} has been removed from inventory')
    
    def has_item(self,item):
        print(f'These are the items in invetory {item}') # this is for us to just check if items are being appended to the inventory, we dont really need it
        return item in self.inventory

    def getPlayer():
        players = {}
        with open('characters.txt', 'r') as file_object:
            for charact in file_object:
                players[charact.split(",")[0]) = Player(charact.split(",")[0], charact.split(",")[1], charact.split(",")[2], charact.split(",")[3])
        return players

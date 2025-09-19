import json

class Room:
    def __init__(self, name, data):
        self.name = name
        self.description = data.get("description")
        self.exits = data.get("exits")
        self.items = data.get("items")

    def __str__(self):
        des = f"Description: {self.description}\n"
        exi = f"Available exits: {self.exits}\n"
        ite = f"Visible items: {self.items}"
        return des + exi + ite

    def exit(self, direction): #command
        return self.exits.get(direction)

    def take(self, item_name, player): #command
        item_nam = item_name.lower()

        if self.name == "Ravenclaw Chamber" and item_nam == "diadem of wit":
            if player:
                return ravenclaw_riddle(player)
            return False

        if self.name == "Hufflepuff Garden" and item_nam == "medallion of loyalty":
            if player:
                return hufflepuff_riddle(player)
            return False

        if self.name == "Gryffindor Arena" and item_nam == "heart of courage":
            if player:
                return gryffindor_riddle(player)
            return False

        if item_name in self.items:
            self.items.remove(item_name)
            if player:
                player.inventory.append(item_name)
            return item_name
        return False

    def objectDict(self): #save
        return {
            "description": self.description,
            "exits": self.exits,
            "items": self.items
        }

    def getRooms():
        with open("game_data.json") as jsonfile:
            room_data = json.load(jsonfile)["rooms"]

        rooms = {}
        for room_name, data in room_data.items():
            rooms[room_name] = Room(room_name, data)
        return rooms


    def ravenclaw_riddle(player, item_name):
        if "Diadem of Wit" in player.inventory:
            print("You've already solved the riddle and claimed the Diadem of Wit.")
            return True

        print("\nA tall bronze eagle door knocker speaks:")
        print("\"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\"")
        answer = input("Your answer: ").strip().lower()

        if answer in ["echo", "an echo"]:
            print("\nThe door swings open silently. A glowing Diadem floats before you.")
            player.inventory.append("Diadem of Wit")
            return True
        else:
            print("\nThe door remains closed. Perhaps think differently and try again later.")
            return True

    def hufflepuff_riddle(player):
        if "Medallion of Loyalty" in player.inventory:
            print("You've already claimed the Medallion of Loyalty.")
            return True

        print("\nA whispering voice in the greenhouse asks:")
        print("\"I am always around but cannot be seen, I bind friends together. What am I?\"")
        answer = input("Your answer: ").strip().lower()

        if answer in ["loyalty", "friendship"]:
            print("Glowing plants part to reveal the Medallion of Loyalty.")
            player.inventory.append("Medallion of Loyalty")
        else:
            print("Nothing happens. Think carefully and try again later.")
        return True


    def gryffindor_riddle(player):
        if "Heart of Courage" in player.inventory:
            print("You've already claimed the Heart of Courage.")
            return True

        print("\nA booming voice in the arena asks:")
        print("\"I am taken by the brave, feared by the faint. What am I?\"")
        answer = input("Your answer: ").strip().lower()

        if answer in ["courage", "heart"]:
            print("A glowing Heart of Courage floats down before you.")
            player.inventory.append("Heart of Courage")
        else:
            print("The arena remains silent. Try again later.")
        return True

import room
import sys

class Go:
    @classmethod
    def go(cls, direction):
        return room.Room.getRooms().get(room.Room.exit(direction)))

class Look:
    @classmethod
    def look(cls, roomObject):
        print(roomObject)

class Take:
    @classmethod
    def takeItem(cls, itemName, playerObject):
        return room.Room.take(itemName, playerObject)

class Help:
    @classmethod
    def showCommands(cls):
        print("| Command        | Description |")
        print("|----------------|-------------|")
        print("| `go [direction]| Move the player in a specified direction. E.g. `go north`, `go east` |")
        print("| `look`         | Show the current room's description, available exits, and visible items |")
        print("| `take [item]`  | Pick up an item in the current room and add it to the player’s inventory. E.g. `take map` |")
        print("| `use [item]`   | Use an item in your inventory. For example, `use key` might unlock a door |")
        print("| `inventory`    | Show all items currently in the player’s inventory |")
        print("| `help`         | List all available commands and a short description of each |")
        print("| `save`         | Save the current game state to a file |")
        print("| `load`         | Load the previously saved game state |")
        print("| 'quit / exit'  | Exit the game Loop|")


class Quit:
    @classmethod
    def quit(cls):
        sys.exit("Thank you! for playing...")

class Inventory:
    @classmethod
    def inventory(playerObject)
        return ",".join(playerObject.inventory)

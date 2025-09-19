import commands
import player
import room
import save_load
import commands
import time

def main():
    roomObjects = []

    if os.file.exists("filename"):
        ...
    else:
        print("==========Welcome to the Hogwarts Trials Game==========")
            print("\n")
            print("Please Pick aCharacter: ")
            print("1. Harry Potter")
            print("2. Luna Lovergood")
            print("3. Dean Thomas")
            print("4. Maisile Flint")
            print("5. Elijah Bramble")

        while True:
            userInput = int(input(""))
            match userInput:
                case 1:
                    player1 = player.getPlayer()["Harry Potter"]
                    currentRoom = room.Room.getRooms()["Library"]

                case 2:
                    player1 = player.getPlayer()["Luna Lovergood"]
                    currentRoom = room.Room.getRooms()["Library"]

                case 3:
                    player1 = player.getPlayer()["Dean Thomas"]
                    currentRoom = room.Room.getRooms()["Library"]

                case 4:
                    player1 = player.getPlayer()["Maisile Flint"]
                    currentRoom = room.Room.getRooms()["Library"]

                case 5:
                    player1 = player.getPlayer()["Elijah Bramble"]
                    currentRoom = room.Room.getRooms()["Library"]

    roomObjects.append(currentRoom)
    welcome = f"{player1.Name} is currently in a {currentRoom.Name} explore and search the Legendary Wand of Merlin."
    for letter in  welcome:
        print(letter, end="")
        time.sleep(0.1)

    commands.Help.showCommands()

    while True:
        userCommand = input("what do you want to do? ")
        match userCommand:
            case "go north":
                player.moving("north")
                currentRoom =commands.Go.go("north")
                roomObjects.append(currentRoom)

            case "go east":
                player.moving("east")
                currentRoom =commands.Go.go("east")
                roomObjects.append(currentRoom)

            case "go south":
                player.moving("south")
                currentRoom =commands.Go.go("south")
                roomObjects.append(currentRoom)

            case "go west":
                player.moving("west")
                currentRoom =commands.Go.go("west")
                roomObjects.append(currentRoom)

            case "take glowing book":
            case "take truth serum":
            case "take silver ladle":
            case "take Diadem of Wit":
            case "take Medallion of Loyalty":
            case "take Heart of Courage":
            case "look":
                print(currentRoom)
            case "use[item]":
                print("This option is not available at the moment.")
            case "inventory":
                player1.Inventory()
            case "help":
                commands.Help.showCommands()
            case "save":
            case "load":
            case "quit":
                commands.Quit.quit()
            case "exit":
                commands.Quit.quit()





if __name__ == "__main__":
    main()

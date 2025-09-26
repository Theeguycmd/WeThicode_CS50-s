import inflect
import random
import player
from cards import Deck
import time
from colorama import Fore


def print_card(card):
    """Print a card in color on the screen."""
    number, color = card
    color_code = {
        "Blue": Fore.BLUE,
        "Green": Fore.GREEN,
        "Yellow": Fore.YELLOW,
        "Red": Fore.RED,
    }.get(color, "")

    print(color_code + "\t\t\t\t\t ------------")
    print(color_code + f"\t\t\t\t\t|{number}           |")
    print(color_code + "\t\t\t\t\t|            |")
    print(color_code + "\t\t\t\t\t|            |")
    print(color_code + "\t\t\t\t\t|            |")
    print(color_code + f"\t\t\t\t\t|           {number}|")
    print(color_code + "\t\t\t\t\t ------------" + Fore.RESET)


def main():
    j = inflect.engine()
    discardPile = []

    print("\nWelcome to UNO!")
    print("Goal: Empty your hand by matching number or color.")
    print("If you have one card left, shout UNO!\n")
    print("==========> N.B 2 PLAYERS ALLOWED TO PLAY <==========")

    while True:
        try:
            numberPlayers = int(input("Enter the number of players: "))
        except ValueError:
            continue

        if numberPlayers == 2:
            playerNamez = []
            for i in range(2):
                name = input(f"Enter the {j.ordinal(i+1)} player name: ")
                playerNamez.append(name)
            break

    player1 = player.Player(playerNamez[0])
    computer = player.Player(playerNamez[1])

    print("Creating deck...")
    DeckCards = Deck()
    DeckCards.getDeck()
    time.sleep(1)

    for _ in range(7):
        player1.hasCards(DeckCards.drawCard())
        computer.hasCards(DeckCards.drawCard())

    print("Dealing cards done!")

    while True:
        first = DeckCards.drawCard()
        if isinstance(first[0], int):
            discardPile.append(first)
            break
        else:
            DeckCards.reShuffle()

    currentPlayer = player1

    while len(player1.show) > 0 and len(computer.show) > 0:
        print("\nTop card on discard pile:")
        print_card(discardPile[-1])

        playable = []
        if currentPlayer == player1:
            print("\nYour cards:")
            for i, c in enumerate(player1.show, start=1):
                print(i, c)

            for c in player1.show:
                if c[0] == discardPile[-1][0] or c[1] == discardPile[-1][1]:
                    playable.append(c)
                if c[0] in ["Wild", "Wild +4"]:
                    playable.append(c)

            if playable:
                print("\nPlayable cards:")
                for i, c in enumerate(playable, start=1):
                    print(i, c)

                choice = int(input("Which one will you play? "))
                chosen = playable[choice - 1]
                discardPile.append(chosen)
                player1.removeCard(chosen)

                if chosen[0] == "Wild":
                    color = input("Pick a color (Red, Blue, Green, Yellow): ")
                    discardPile.append(("Wild", color.title()))
                elif chosen[0] == "Wild +4":
                    for _ in range(4):
                        computer.hasCards(DeckCards.drawCard())
                    color = input("Pick a color (Red, Blue, Green, Yellow): ")
                    discardPile.append(("Wild +4", color.title()))

                if len(player1.show) == 1:
                    shout = input("You have 1 card left! Type 'UNO' quickly: ")
                    if shout.strip().upper() != "UNO":
                        print("You forgot to say UNO! Drawing 2 penalty cards.")
                        for _ in range(2):
                            player1.hasCards(DeckCards.drawCard())

            else:
                print("No playable card. Drawing one...")
                player1.hasCards(DeckCards.drawCard())

            currentPlayer = computer

        else:
            time.sleep(1)
            played = False
            for c in computer.show:
                if (
                    c[0] == discardPile[-1][0]
                    or c[1] == discardPile[-1][1]
                    or c[0] in ["Wild", "Wild +4"]
                ):
                    print("Computer plays:", c)
                    discardPile.append(c)
                    computer.removeCard(c)
                    played = True

                    if c[0] == "Wild +4":
                        for _ in range(4):
                            player1.hasCards(DeckCards.drawCard())
                        new_color = random.choice(["Red", "Blue", "Green", "Yellow"])
                        discardPile.append(("Wild +4", new_color))
                        print("Computer changes color to:", new_color)

                    elif c[0] == "Wild":
                        new_color = random.choice(["Red", "Blue", "Green", "Yellow"])
                        discardPile.append(("Wild", new_color))
                        print("Computer changes color to:", new_color)
                    break

            if not played:
                print("Computer draws a card.")
                computer.hasCards(DeckCards.drawCard())

            if len(computer.show) == 1:
                print("Computer shouts: UNO!!!")

            currentPlayer = player1

    if len(player1.show) == 0:
        print(f"\n{player1.Name()} WON!!!")
    else:
        print(f"\n{computer.Name()} WON!!!")

    print("==========> Thank You For Playing <==========")


if __name__ == "__main__":
    main()

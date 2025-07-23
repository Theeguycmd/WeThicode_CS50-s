import sys

def main():
    food()

def food():
    things = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        try:
            ordered = input("Item: ")
        except EOFError:
            sys.exit("")
        else:
            if ordered.title() in things:
                total += things[ordered.title()]
                print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()



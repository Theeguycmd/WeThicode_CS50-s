import random
import sys

def main():
    
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level >= 1:
                guess = random.randint(1, level)
                while True:
                    try:
                        number = int(input("Guess: "))
                    except ValueError:
                        continue
                    else:
                        if number == guess:
                            sys.exit("Just right!")
                        elif number < guess and number >= 1:
                            print("Too small!")
                        elif number > guess and number <= level:
                            print("Too large!")
                        else:
                            continue
            continue

if __name__ == "__main__":
    main()

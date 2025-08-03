import random


def main():
    score = 0
    expression = 0
    tries = 0
    level = get_level()

    while True:
        ask = True
        X, Y = generate_integer(level)
        while ask:
            try:
                answer = int(input(f"{X} + {Y} = "))
            except ValueError:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{X} + {Y} = {X + Y}")
                    expression += 1
                    tries = 0
                    ask = False
            else:
                if answer == (X + Y):
                    score += 1
                    tries = 0
                    expression += 1
                    ask = False
                else:
                    print("EEE")
                    tries += 1
                    if tries == 3:
                        print(f"{X} + {Y} = {X + Y}")
                        expression += 1
                        tries = 0
                        ask = False
        if expression == 10:
            print(f"Score: {score}")
            break



def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level == 1 or level == 2 or level == 3:
                return level
            continue





def generate_integer(level):
    if level == 1:
        y = random.randint(0,9)
        x = random.randint(0,9)
        return [x, y]

    elif level == 2:
        y = random.randint(10, 99)
        x = random.randint(10, 99)
        return [x, y]

    else:
        y= random.randint(100, 999)
        x = random.randint(100, 999)
        return [x, y]





if __name__ == "__main__":
    main()

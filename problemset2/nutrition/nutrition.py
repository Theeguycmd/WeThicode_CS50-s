def main():
    item = input("Item: ").lower()
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "sweet cherries": 100,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "tangerine": 50,
        "watermelon": 80,
        "lime": 20
    }

    if item in fruits:
        print(f"Calories: {fruits[item]}")


main()

def main():
    toBuy = {}
    while True:
        try:
            item = input("").lower()
        except EOFError:
            print("\n")
            print("\n")
            for i in toBuy:
                print(f"{toBuy[i]} {i.upper()}")
            break
        else:
            if item.isspace() == True or item == "\n" or item == "\t" or item == "\r":
                pass
            elif item.upper() in toBuy:
                toBuy[item.upper()] += 1
            else:
                toBuy[item.upper()] = 1

if __name__ == "__main__":
    main()



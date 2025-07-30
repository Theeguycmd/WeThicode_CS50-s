def main():
    toBuy = {}
    while True:
        try:
            item = input("").strip().lower()
        except EOFError:
            print("\n")
            print("\n")
            for i in sorted(toBuy):
                print(f"{toBuy[i]} {i.upper()}")
            break
        else:
            if item == "":
                continue
            elif item.upper() in toBuy:
                toBuy[item.upper()] += 1
            else:
                toBuy[item.upper()] = 1



if __name__ == "__main__":
    main()



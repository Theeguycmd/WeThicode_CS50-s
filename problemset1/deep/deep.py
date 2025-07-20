def main():
        print(meaning())


def meaning():
        mystery = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
        match mystery:
                case "42":
                        return "Yes"
                case "forty-two":
                        return "Yes"
                case "forty two":
                        return "Yes"
                case _:
                        return "No"

main()

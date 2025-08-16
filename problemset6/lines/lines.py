import sys

def main():
    filename = validate_args()
    counter = count_lines(filename)
    print(counter)



def validate_args():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    return filename


def count_lines(filename):
    counter = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                if not line.lstrip().startswith("#") and line.strip() != "" and not line.startswith("''"):
                    counter += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return counter



if __name__ == "__main__":
    main()

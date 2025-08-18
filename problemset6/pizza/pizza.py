from tabulate import tabulate
import sys


def main():
    if validate_args():
        print(create_table(validate_args()))

def validate_args():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    return filename



def create_table(fileName):
    arrayArray = []
    try:
        with open(fileName) as file:
            for line in file:
                if line.strip() == "":
                    continue
                arrayArray.append(line.split(","))
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return tabulate(arrayArray, headers="firstrow", tablefmt="grid")




if __name__ == "__main__":
    main()

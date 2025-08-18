import csv
import sys

def main():
    if validate_args():
        print(update(validate_args()[0], validate_args()[1]))


def validate_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    if not filename1.endswith(".csv"):
        sys.exit(f"{filename1} is Not a CSV file")
    elif not filename2.endswith(".csv"):
        sys.exit(f"{filename2} is Not a CSV file")

    return [filename1, filename2]

def update(before, after):
    try:
        with open(before) as firstFile, open(after, "a") as secondFile:
            reader = csv.DictReader(firstFile)
            write = csv.writer(secondFile)
            writer = csv.DictWriter(secondFile, fieldnames=["first", "last", "house"])
            write.writerow(["first", "last", "house"])
            for row in reader:
                writer.writerow({"first": row["name"].split(",")[1], "last": row["name"].split(",")[0], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")
    else:
        return "Done"



if __name__ == "__main__":
    main()

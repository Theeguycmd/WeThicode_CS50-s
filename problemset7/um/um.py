import re
import sys


def main():
    print(count(input("Text: ")))



def count(s):
    words = s.split(" ")
    counter = 0
    for word in words:
        counter += len(re.findall(r"^um[,|]?$", word, re.IGNORECASE))
    return counter


if __name__ == "__main__":
    main()

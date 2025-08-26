import validators
import sys


def main():
    if is_valid(input("What's your email address? ")):
        sys.exit("Valid")
    print("Invalid")


def is_valid(Email):
    return validators.email(Email)


if __name__ == "__main__" :
    main()

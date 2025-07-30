import pyfiglet
import sys
from random import choice

def main():
    toUse = pyfiglet.FigletFont.getFonts()
    text = input("Input: ")
    if len(sys.argv) == 3:

        if sys.argv[1].lower() == "-f" or sys.argv[1].lower() == "--font" and sys.argv[2] in toUse:
            print(f"Output: \n{pyfiglet.figlet_format(text, font=sys.argv[2])}")
        else:
            sys.exit("Invalid usage")

    elif len(sys.argv) == 1:
        print(f"Output:\n {pyfiglet.figlet_format(text, font=choice(toUse))}")

    else:
        sys.exit("Too feww or many arguments provided")



if __name__ == "__main__":
    main()

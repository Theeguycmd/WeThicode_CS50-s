import inflect
import sys

def main():
    p = inflect.engine()
    people = []
    while True:
        try:
            name = input("Name: ").strip()
        except EOFError:
            if len(people) == 0:
                break
            sys.exit(f"\nAdieu, adieu to {p.join(people)}")
        else:
            people.append(name) 


if __name__ =="__main__":
    main()

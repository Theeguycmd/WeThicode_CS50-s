def main():
    print(validate(input("IPv4 Address: ")))



def validate(arg):
    if  "." in arg:
        numbers = arg.split(".")
        try:
            for number in [int(num) for num in numbers]:
                if 0 <=  number <= 255:
                    continue
                else:
                    return False
            return True
        except ValueError:
            return False
    else:
        return False

if __name__ == "__main__":
    main()

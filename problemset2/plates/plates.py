def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    unwanted = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~" + '"' + "\\"
    numbers = ""
    letters = ""

    for i in s:
        if i in unwanted:
            return False
        else:
            continue

    if len(s) >= 2 and len(s) <= 6:
        if len(s) == 2 and s[0].isnumeric() == False and s[1].isnumeric() == False:
            return True
        elif len(s) == 2 and s[0].isnumeric() == True:
            return False
        elif len(s) == 2 and s[1].isnumeric() == True:
            return False
        else:
            letters = letters + s[0:2]
            for j in s[2::]:
                if j.isnumeric():
                    numbers = numbers + j
                else:
                    letters = letters + j
            if int(numbers[0]) == 0:
                return False
            else:
                if letters + numbers == s:
                    return True
                else:
                    return False
    else:
        return False


main()

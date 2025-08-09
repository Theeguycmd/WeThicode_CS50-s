def main():
    while True:
        check = convert(input("Fraction: "))
        if check == "Error":
            continue
        else:
            print(gauge(check))
            break


def convert(fraction):
    if "/" in fraction:
        try:
            sum = (int(fraction.split("/")[0]) / int(fraction.split("/")[1])) * 100 
        except (ValueError, ZeroDivisionError):
            return "Error"
        else:
            if sum  <= 100 and sum >= 0:
                return int(sum)
            else:
                return "Error"
    else:
        return "Error"




def gauge(percent):
    if percent == 100 or percent == 99:
        return "F"
    elif percent == 0 or percent == 1:
        return "E"
    else:
        return f"{percent}%"




if __name__ == "__main__":
    main()

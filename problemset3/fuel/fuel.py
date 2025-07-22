def main():
    while True:
        something = input("Fraction: ")
        if "/" in something:
            num1, num2 = something.split("/")
            if int(num1) <= int(num2):
                try:
                    sum = (int(num1) / int(num2)) * 100
                except (ValueError, ZeroDivisionError):
                    pass
                else:
                    if sum == 100:
                        print("F")
                    elif sum == 0:
                        print("E")
                    else:
                        print(f"{int(sum)}%")
                    break

main()

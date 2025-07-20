def main():
        x, y, z = input("Enter an arithmetic expression: ").split()
        result = 0
        if y == "+":
                result = int(x) + int(z)
        elif y == "×" or y == "*":
                result = int(x) * int(z)
        elif y == "÷" or y == "/":
                if int(z) == 0:
                        print("Cannot devide by zero")
                else:
                        result = int(x) / int(z)
        elif y == "-":
                result = int(x) - int(z)
        else:
                print("Invalid Expression")
        print(float(result))

main()

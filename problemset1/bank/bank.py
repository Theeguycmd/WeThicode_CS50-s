def main():                                                                      
    answer = input("Greeting: ").strip().lower()
    print(f"$ {value(answer)}")


def value(greeting):
    array = greeting.split()

    if array[0] == "hello":
        return 0
    elif array[0][0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

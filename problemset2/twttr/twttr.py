def main():
    vowels = ["a", "e", "i", "o", "u"]
    userInput = input("Input: ")
    for vowel in vowels:
        if vowel in userInput or vowel.upper() in userInput:
            userInput = userInput.replace(vowel, "")
            userInput = userInput.replace(vowel.upper(), "")

    print(userInput)


main()

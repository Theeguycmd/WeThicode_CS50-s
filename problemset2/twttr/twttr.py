def main():
    print(shorten(input("Inpuut: ")))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        if vowel in word or vowel.upper() in word:
            word = word.replace(vowel, "")
            word = word.replace(vowel.upper(), "")
    return word

if __name__ == "__main__":
    main()

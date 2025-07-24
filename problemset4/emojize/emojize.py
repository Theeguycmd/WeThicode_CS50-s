import emoji

def main():
    print(withEmoji(input("Input: ")))

def withEmoji(words):
    return emoji.emojize(words)


if __name__ == "__main__":
    main()


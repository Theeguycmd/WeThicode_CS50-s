def main():
        words = input("")
        something = convert(words)
        print(something)


def convert(str):
        return str.replace(":)", "🙂").replace(":(", "🙁")

main()

def main():                                                                      
        answer = input("Greeting: ").strip().lower()
        array = answer.split()

        if array[0] == "hello":
                print("$0")
        elif array[0][0] == "h":
                print("$20")
        else:
                print("$100")
main()

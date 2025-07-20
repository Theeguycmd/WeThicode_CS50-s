def main():
    camelCase = input("camelCase: ")
    snakeCase = ""
    for case in camelCase:
        if case.isupper() == True:
            snakeCase = snakeCase + "_" + case.lower()
        else:
            snakeCase = snakeCase + case
    
    print(snakeCase)

main()

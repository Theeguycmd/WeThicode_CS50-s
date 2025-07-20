def main():
    due = 50
    accept = [25, 10, 5]
    while due > 0:
        print(f"Amount Due: {due}")
        payed = int(input("Insert Coin: "))
        if payed in accept:
            due = due - payed
    print(f"Change Owed: {abs(due)}")

main()

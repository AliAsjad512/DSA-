balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("New Balance:", balance)

    elif choice == "3":
        amount = int(input("Enter withdraw amount: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("New Balance:", balance)

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")

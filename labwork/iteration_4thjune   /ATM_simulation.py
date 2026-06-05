# Wap to simulate an ATM system

balance = 10000

# ---------------------------------------------------

while(True):

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # ---------------------------------------------------

    if(choice == 1):
        print("Current Balance = ₹", balance)

    # ---------------------------------------------------

    elif(choice == 2):
        amount = float(input("Enter amount to deposit: "))

        # validate amount
        if(amount <= 0):
            print("Amount should be positive")
        else:
            balance = balance + amount
            print("Deposit Successful")
            print("Updated Balance = ₹", balance)

    # ---------------------------------------------------

    elif(choice == 3):
        amount = float(input("Enter amount to withdraw: "))

        # validate amount
        if(amount <= 0):
            print("Amount should be positive")
        elif(amount > balance):
            print("Insufficient Balance")
        else:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance = ₹", balance)

    # ---------------------------------------------------

    elif(choice == 4):
        print("Thank You for Using ATM")
        break

    # ---------------------------------------------------

    else:
        print("Invalid Choice")

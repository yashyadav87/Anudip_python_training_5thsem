#Wap to detect suspicious transactions
#Input transaction amounts continuously
#Stop when -1 is entered
#Count transactions above ₹50000
#Count transactions below ₹1000
#Calculate total transaction amount

high_transactions=0
low_transactions=0
total_amount=0

#---------------------------------------------------
#accepting transaction amounts

while(True):

    amount=float(input("Enter transaction amount (-1 to stop): "))

    #---------------------------------------------------
    #checking termination condition

    if(amount==-1):
        break

    #---------------------------------------------------
    #validating transaction amount

    if(amount<0):
        print("Transaction amount cannot be negative")
        continue

    #---------------------------------------------------
    #counting high value transactions

    if(amount>50000):
        high_transactions+=1

    #---------------------------------------------------
    #counting low value transactions

    if(amount<1000):
        low_transactions+=1

    #---------------------------------------------------
    #adding transaction amount

    total_amount+=amount

#---------------------------------------------------
#displaying results

print("Transactions Above ₹50000 =",high_transactions)
print("Transactions Below ₹1000 =",low_transactions)
print("Total Transaction Amount =",total_amount)

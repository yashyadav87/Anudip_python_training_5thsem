#Wap to find the minimum number of notes required for a given amount
#Available notes are ₹500, ₹200, ₹100, ₹50, ₹20 and ₹10

amount=int(input("Enter the amount: "))

#validate amount
if(amount<0):
    exit("Amount cannot be negative")

#---------------------------------------------------
#calculating number of ₹500 notes

note500=amount//500
amount=amount%500

#---------------------------------------------------
#calculating number of ₹200 notes

note200=amount//200
amount=amount%200

#---------------------------------------------------
#calculating number of ₹100 notes

note100=amount//100
amount=amount%100

#---------------------------------------------------
#calculating number of ₹50 notes

note50=amount//50
amount=amount%50

#---------------------------------------------------
#calculating number of ₹20 notes

note20=amount//20
amount=amount%20

#---------------------------------------------------
#calculating number of ₹10 notes

note10=amount//10
amount=amount%10

#---------------------------------------------------
#displaying note count

print("500 x",note500)
print("200 x",note200)
print("100 x",note100)
print("50 x",note50)
print("20 x",note20)
print("10 x",note10)

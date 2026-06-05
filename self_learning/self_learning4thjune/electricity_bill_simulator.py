#Wap to calculate electricity bill using slab rates
#0-100 units     -> ₹5 per unit
#101-200 units   -> ₹7 per unit
#Above 200 units -> ₹10 per unit
#Add 10% surcharge if bill exceeds ₹5000
#Display final payable amount

units=float(input("Enter units consumed: "))

#validate units
if(units<0):
    exit("Units consumed cannot be negative")

#---------------------------------------------------
#calculating electricity bill according to slab

if(units<=100):
    bill=units*5

elif(units<=200):
    bill=(100*5)+((units-100)*7)

else:
    bill=(100*5)+(100*7)+((units-200)*10)

#---------------------------------------------------
#checking whether surcharge is applicable

if(bill>5000):
    surcharge=bill*10/100
else:
    surcharge=0

#---------------------------------------------------
#calculating final payable amount

final_bill=bill+surcharge

#---------------------------------------------------
#displaying bill details

print("Electricity Bill =",bill)
print("Surcharge =",surcharge)
print("Final Payable Amount =",final_bill)

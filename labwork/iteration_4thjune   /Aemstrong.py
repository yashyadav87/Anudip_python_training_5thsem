#Accept a number from the user and check whether it is an Armstrong Number.
#input number
num = int(input("Enter a number: "))

#validate number
if(num < 0):
    exit("Number should be non-negative")

#---------------------------------------------------

#store original number
temp = num

#count number of digits
digits = len(str(num))

#store sum of powers
sum_of_powers = 0

#---------------------------------------------------

#extract digits and calculate sum of powers
while(temp > 0):
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

#---------------------------------------------------

#verify Armstrong Number
if(sum_of_powers == num):
    print("The number is an Armstrong Number")
else:
    print("The number is not an Armstrong Number")

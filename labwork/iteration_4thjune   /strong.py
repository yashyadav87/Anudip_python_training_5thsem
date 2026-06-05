#Wap to check whether a given number is a Strong Number

#input number
num = int(input("Enter a number: "))

#validate number
if(num < 0):
    exit("Number should be non-negative")

#---------------------------------------------------

#store original number
temp = num

#store sum of factorials
sum_of_factorials = 0

#---------------------------------------------------

#extract digits and find factorial sum
while(temp > 0):
    digit = temp % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    sum_of_factorials += factorial
    temp //= 10

#---------------------------------------------------

#verify Strong Number
if(sum_of_factorials == num):
    print("The number is a Strong Number")
else:
    print("The number is not a Strong Number")
  

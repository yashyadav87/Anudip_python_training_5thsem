#Wap to check whether a given number is Prime or not and print its factors

#input number
num = int(input("Enter a number: "))

#validate number
if(num <= 0):
    exit("Number should be positive")

#---------------------------------------------------

#initialize variables
i = 1
count = 0

#---------------------------------------------------

#print factors and count them
print("Factors:", end=" ")

while(i <= num):
    if(num % i == 0):
        print(i, end=" ")
        count += 1
    i += 1

print()

#---------------------------------------------------

#verify Prime Number
if(count == 2):
    print("The number is a Prime Number")
else:
    print("The number is not a Prime Number")

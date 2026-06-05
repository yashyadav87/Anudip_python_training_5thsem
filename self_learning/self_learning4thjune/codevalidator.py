#Wap to check whether a secret code is valid or not
#A valid code must contain exactly 6 digits
#Sum of first 3 digits should be equal to sum of last 3 digits

code=input("Enter the secret code: ")

#validate code length
if(len(code)!=6):
    exit("Code should contain exactly 6 digits")

#---------------------------------------------------
#validate that all characters are digits

if(not code.isdigit()):
    exit("Code should contain only digits")

#---------------------------------------------------
#calculating sum of first 3 digits

first_half_sum=0

for i in range(3):
    first_half_sum+=int(code[i])

#---------------------------------------------------
#calculating sum of last 3 digits

second_half_sum=0

for i in range(3,6):
    second_half_sum+=int(code[i])

#---------------------------------------------------
#checking code validity

if(first_half_sum==second_half_sum):
    print("Valid Code")
else:
    print("Invalid Code")

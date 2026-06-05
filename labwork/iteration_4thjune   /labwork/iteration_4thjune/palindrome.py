#Wap to find reverse of a number and check if it is palindrome or not

num=int(input("Enter a number"))
#validate number
if(num<0):
    exit("Number should be non-negative")

#---------------------------------------------------
temp=num
reverse=0

#finding reverse number
while(temp>0):
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10

#---------------------------------------------------
print("Reverse Number =",reverse)

#checking palindrome
if(num==reverse):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

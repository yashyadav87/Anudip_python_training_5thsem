#Wap to check whether a number is a mirror number or not
#A mirror number has identical left and right halves

num=input("Enter a number: ")

#validate number
if(not num.isdigit()):
    exit("Number should contain only digits")

#---------------------------------------------------
#checking whether number has even digits

if(len(num)%2!=0):
    print("Not a Mirror Number")

else:

    #---------------------------------------------------
    #finding left and right halves

    mid=len(num)//2

    left_half=num[:mid]
    right_half=num[mid:]

    #---------------------------------------------------
    #checking mirror condition

    if(left_half==right_half):
        print("Mirror Number")
    else:
        print("Not a Mirror Number")

#Wap to check whether a number is a mountain number or not

num=int(input("Enter a number"))
#validate number
if(num<0):
    exit("Number should be non-negative")

#---------------------------------------------------
num_str=str(num)
peak_found=False
is_mountain=True

#checking mountain pattern
for i in range(len(num_str)-1):

    if(not peak_found):
        if(num_str[i+1]>num_str[i]):
            continue
        elif(num_str[i+1]<num_str[i]):
            peak_found=True
        else:
            is_mountain=False
            break

    else:
        if(num_str[i+1]>=num_str[i]):
            is_mountain=False
            break

#---------------------------------------------------
#verifying mountain number
if(not peak_found):
    is_mountain=False

#---------------------------------------------------
#displaying result
if(is_mountain):
    print("Mountain Number")
else:
    print("Not a Mountain Number")

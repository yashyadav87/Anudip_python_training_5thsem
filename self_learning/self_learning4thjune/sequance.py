#Wap to find the length of the longest continuous increasing sequence

n=int(input("Enter the number of elements"))
#validate n
if(n<=0):
    exit("Number of elements should be positive")

#---------------------------------------------------
current_length=1
longest_length=1

prev=int(input("Enter number 1"))

#---------------------------------------------------
for i in range(2,n+1):
    num=int(input("Enter number "+str(i)))

    if(num>prev):
        current_length=current_length+1
    else:
        current_length=1

    if(current_length>longest_length):
        longest_length=current_length

    prev=num

#---------------------------------------------------
print("Longest Sequence Length =",longest_length)

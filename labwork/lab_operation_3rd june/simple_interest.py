#wap to calculate simple interst (validate data)
pa = float(input( "enter priniciple amount"))
if (pa<=0):
    exit("prrinciple amout cannot be negative ")

r = float(input("enter rate"))
if (r<=0):
    exit("rate cannot be negative ")
t = float(input("enter time"))
if (t<=0):
    exit("time cannot be negative ")
else:
   
    print("simple intrest is: ",(pa*t*r)/100)

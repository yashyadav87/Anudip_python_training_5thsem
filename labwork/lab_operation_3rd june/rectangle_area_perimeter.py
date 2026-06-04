# write a program to calculate area and perimeter of rectangle

length = float(input("enter the length of rectangle:"))
breadth = float(input("enter the breadth of rectangle:"))

if(length<0 or breadth<0):
    exit("length cannot be negative")
    
area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of rectangle is",area)
print("Perimeter of rectangle is",perimeter)

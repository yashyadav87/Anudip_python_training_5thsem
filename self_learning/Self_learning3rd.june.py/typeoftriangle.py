#wap to specify the type of triangle ,if three sides form a triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input! Sides must be positive.")
elif a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")

    if a == b == c:
        print("Type: Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Type: Isosceles Triangle")
    else:
        print("Type: Scalene Triangle")
else:
    print("Not a Triangle

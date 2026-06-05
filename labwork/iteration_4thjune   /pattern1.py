# Wap to print number pyramid pattern

rows = int(input("Enter number of rows: "))

# validate rows
if(rows <= 0):
    exit("Number of rows should be positive")

# ---------------------------------------------------

# print pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# ---------------------------------------------------

# print reverse pattern
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

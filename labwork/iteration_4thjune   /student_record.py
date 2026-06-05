# Wap to calculate student result

sub1 = float(input("Enter marks of Subject 1: "))
# validate sub1
if(sub1 < 0 or sub1 > 100):
    exit("Marks should be between 0 and 100")

# ---------------------------------------------------

sub2 = float(input("Enter marks of Subject 2: "))
# validate sub2
if(sub2 < 0 or sub2 > 100):
    exit("Marks should be between 0 and 100")

# ---------------------------------------------------

sub3 = float(input("Enter marks of Subject 3: "))
# validate sub3
if(sub3 < 0 or sub3 > 100):
    exit("Marks should be between 0 and 100")

# ---------------------------------------------------

sub4 = float(input("Enter marks of Subject 4: "))
# validate sub4
if(sub4 < 0 or sub4 > 100):
    exit("Marks should be between 0 and 100")

# ---------------------------------------------------

sub5 = float(input("Enter marks of Subject 5: "))
# validate sub5
if(sub5 < 0 or sub5 > 100):
    exit("Marks should be between 0 and 100")

# ---------------------------------------------------

# calculate total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

# ---------------------------------------------------

# count failed subjects
failed_subjects = 0

if(sub1 < 40):
    failed_subjects += 1

if(sub2 < 40):
    failed_subjects += 1

if(sub3 < 40):
    failed_subjects += 1

if(sub4 < 40):
    failed_subjects += 1

if(sub5 < 40):
    failed_subjects += 1

# ---------------------------------------------------

# determine grade
if(percentage >= 90):
    grade = "A+"
elif(percentage >= 75):
    grade = "A"
elif(percentage >= 60):
    grade = "B"
elif(percentage >= 40):
    grade = "C"
else:
    grade = "Fail"

# ---------------------------------------------------

print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Number of Subjects Failed =", failed_subjects)

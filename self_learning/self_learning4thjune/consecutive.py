# Program to check whether a number is a Consecutive Digit Number

# Accept a number from the user
num = int(input("Enter a number: "))

# Store the last digit
prev_digit = num % 10

# Remove the last digit
num = num // 10

# Assume the number is consecutive
is_consecutive = True

# Check digits from right to left
while num > 0:
    current_digit = num % 10

    # Check if the next digit is exactly 1 greater
    if current_digit + 1 != prev_digit:
        is_consecutive = False
        break

    # Update previous digit
    prev_digit = current_digit

    # Remove the last digit
    num = num // 10

# Display the result
if is_consecutive:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")

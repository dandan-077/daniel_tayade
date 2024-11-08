# This program counts the number of digits in a number

# Ask the user to enter a number
number = int(input("Please enter a number: "))

# We will use this variable to keep track of the number of digits
count = 0


# Loop until the number is 0
while number > 0:
    number = number // 10  # Remove the last digit
    count += 1  # Increase the count by 1

# If the number was 0, we need to say it has 1 digit
if count == 0:
    count = 1

# Show the result to the user
print("The number of digits is:", count)

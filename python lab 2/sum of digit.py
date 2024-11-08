#sum of digit

number = int(input("Please enter a number: "))

# Initialize the sum variable
sum_of_digits = 0
# While the number is greater than 0
while number > 0:
    digit = number % 10  # Get the last digit
    sum_of_digits += digit  # Add it to the sum
    number //= 10  # Remove the last digit

# Display the result
print("The sum of the digits is:", sum_of_digits)


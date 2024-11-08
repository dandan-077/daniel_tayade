# Program to calculate the factorial of a number using a while loop
number = int(input("Enter a number to calculate its factorial: "))

# Initialize variables
factorial = 1
i = 1
while i <= number:
    factorial *= i  
    i += 1          

# printing result
print(f"The factorial of {number} is: {factorial}")



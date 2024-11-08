#Swap function

# Take two numbers as input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Print original values
print("Before swapping:")
print("First number:", a)
print("Second number:", b)

# Swap the values using a temporary variable
temp = a
a = b
b = temp

# Print swapped values
print("After swapping:")
print("First number:", a)
print("Second number:", b)

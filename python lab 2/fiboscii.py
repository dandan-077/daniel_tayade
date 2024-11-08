# Fibonacci series up to n terms!


n = int(input("Please enter the number of terms for the Fibonacci series: "))

# Initialize the first two terms
a= 0
b=1

# Initialize a counter
count = 0

print("Fibonacci Series:")
# Use a while loop to generate the Fibonacci series
while count < n:
    print(a, end=" ")  # Print the current term
    a=b
    b=a+b
    count += 1  # Increment the counter

print()  # Print a newline at the end

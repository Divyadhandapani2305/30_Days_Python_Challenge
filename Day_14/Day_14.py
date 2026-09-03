# Function to find the sum of two numbers
def add(a, b):
    return a + b

# Function to check if a number is even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to find the largest number in a list
def find_largest(numbers):
    return max(numbers)

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

number = int(input("Enter a number to check: "))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calling the functions
print("Sum:", add(num1, num2))
print("The number is:", check_even_odd(number))
print("Largest number:", find_largest(numbers))
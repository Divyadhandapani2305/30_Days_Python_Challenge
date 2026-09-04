# Global variable
number = 10
# Function to demonstrate local and global variables
def show_number():
    local_number = 5
    print("Local variable:", local_number)
    print("Global variable:", number)
# Lambda to find square
square = lambda x: x * x
# Lambda with multiple arguments
add = lambda a, b: a + b
# Calling the function
show_number()
# Calling lambda functions
print("Square of 4:", square(4))
print("Sum of 10 and 20:", add(10, 20))

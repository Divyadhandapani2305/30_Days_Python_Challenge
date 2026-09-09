try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numbers only.")
else:
    print(f"Result: {result}")
    print("Division successful!")
finally:
    print("Program execution completed.")
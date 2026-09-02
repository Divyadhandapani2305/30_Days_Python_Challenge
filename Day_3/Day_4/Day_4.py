name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
meters = height / 100
print("\n--- Personal Details ---")
print("Name:", name)
print("Age:", age)
print("Height:", height, "cm")
print("Height:", meters, "m")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")
if op == "+":
    print("Answer:", a + b)
elif op == "-":
    print("Answer:", a - b)
elif op == "*":
    print("Answer:", a * b)
elif op == "/":
    if b != 0:
        print("Answer:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
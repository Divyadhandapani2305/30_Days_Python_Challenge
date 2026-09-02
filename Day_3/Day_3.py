#ARITHMETIC OPERATORS
num1= int(input("Enter number1:"))
num2= int(input("Enter number2:"))
print("num1+num2=",num1+num2)
print("num1-num2=",num1-num2)
print("num1*num2=",num1*num2)
print("num1//num2=",num1//num2)
print("num1/num2=",num1/num2)
print("num1%num2=",num1%num2)
print("num1**num2=",num1**num2)

#COMPARISON OPERATORS
print("num1>num2=",num1>num2)
print("num1<num2=",num1<num2)
print("num1==num2=",num1==num2)
print("num1!=num2=",num1!=num2)
print("num1>=num2=",num1>=num2)
print("num1<=num2=",num1<=num2)

#LOGICAL OPERATORS
x = True
y = False
print("x and y = ",x and y)
print("x or y = ",x or y)
print("not x = ",not x)

#CODE
num = int(input("Enter a number: "))

# Positive, Negative or Zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Even or Odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
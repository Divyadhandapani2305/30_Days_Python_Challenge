num = int(input("Enter a Number:"))
if num>0:
    print("Positive")
elif num <0:
    print("Negative")
else:
    print("Zero")
    
marks = int(input("Enter marks:"))
if marks >=90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
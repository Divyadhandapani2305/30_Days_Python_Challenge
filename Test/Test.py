print("=============== 1. BASIC OUTPUT=============")
name= input("Enter Name:")
print("Welcome to Python Test!")
print("Name:",name)
print("===============2. VARIABLES=============")
a,b = list(map(int,input("Enter Number:").split()))
print("Sum:",a+b)
print("Product:",a*b)
print("===============3.Data Types=============")
a = 4
b = 4.6
name = "Divya"
print("Type of A:",type(a))
print("Type of B:",type(b))
print("Type of Name:",type(name))
print("===============4. TYPE CONVERSION==========")
str = input("Enter a String Number:")
print("String_Number:",str)
number = int(str)
print("Converted Number:",number)
print("After Adding 10:",number+10)
print("============== 5. OPERATORS ==============")
d = int(input("Enter Number:"))
q = int(input("Enter Number:"))
print("Addition:",d+q)
print("Subraction:",d-q)
print("Multiplication:",d*q)
print("Floor_Div:",d//q)
print("Div:",d/q)
print("Modulo:",d%q)
print("Expo:",d**q)
print("=============== 6. CONDITIONAL - IF ELSE ==============")
num = int(input("Enter Number:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
print("================ 7. FOR LOOP ================")  
n = int(input("Enter Number:"))
for i in range(1,n+1):
    print(i,end=" ")
print("================ 8. WHILE LOOP =============")
w = int(input("Enter Number:"))
while w >=1:
    print(w, end =" ")
    w -= 1
print()
print("------------------ 9. STRINGS ---------------")
s = input("Enter String:")
print("Upper Case:",s.upper())
print("First Char:",s[0])
print("Last Char:",s[-1])
print("---------------10. LIST OPERATIONS--------------")
my_list=[10,20,40,60]
print("original_list:",my_list)
print("Max:",max(my_list))
print("Min:",min(my_list))
print("Sum:",sum(my_list))
print("----------------11. LIST MANIPULATION-----------")
numbers = []
for i in range(4):
    number = int(input("Enter number: "))
    numbers.append(number)
number = int(input("Enter number to append: "))
numbers.append(number)
numbers.pop(1)
print("Final List:", numbers)
print("---------12. COUNT USING WHILE LOOP ------------")
marks = []
for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)
count = 0
i = 0
while i < len(marks):
    if marks[i] >= 50:
        count += 1
    i += 1
print("Count of marks >= 50:", count)
print("-----------13. GRADE CALCULATION-------------")
mark = int(input("Enter mark: "))
if mark >= 90:
    grade = "A"
elif mark >= 75:
    grade = "B"
elif mark >= 50:
    grade = "C"
else:
    grade = "D"
print("Grade:", grade)
print("--------------14. STRING OPERATIONS-------------")
text = input("Enter a string: ")
print("Reversed:", text[::-1])
vowels = 0
for character in text.lower():
    if character in "aeiouAEIOU":
        vowels += 1
print("Vowels:", vowels)
print("--------------15. SUMMARY REPORT-------------")
student_name = input("Enter student name: ")
age = int(input("Enter age: "))
number_of_subjects = int(input("Enter number of subjects: "))
total_marks = 0
passed = 0
for i in range(number_of_subjects):
    mark = int(input("Enter subject mark: "))
    total_marks += mark
    if mark >= 50:
        passed += 1
average = total_marks / number_of_subjects
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "D"
print("SUMMARY REPORT")
print("Name :", student_name)
print("Age  :", age)
print("Subjects :", number_of_subjects)
print("Total Marks :", total_marks)
print("Average :", format(average, ".2f"))
print("Grade :", grade)
print("Passed (>=50) :", passed)
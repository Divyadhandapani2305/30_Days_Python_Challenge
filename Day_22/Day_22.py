class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:" , self.grade)
        
    def greet(self):
        print(f"Hello! I am {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"My grade is {self.grade}.")

student1 = Student("Abi", 22, "A")
student1.display_details()

s1 = Student("Abi", 22, "A")
s2 = Student("Naveen", 25, "B")

s1.greet()
print()
s2.greet()
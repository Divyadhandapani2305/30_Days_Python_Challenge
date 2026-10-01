class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    # Getter
    def get_name(self):
        return self.__name
    
    # Getter
    def get_age(self):
        return self.__age
    
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        
    def display(self):
        print("Name:", self.get_name())
        print("Age:", self.get_age())
        print("Grade:", self.grade)
student = Student("Kaviya", 27, "A")
student.display()
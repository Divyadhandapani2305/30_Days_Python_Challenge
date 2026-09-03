# Student dictionary
student = {
    "name": "Kaviya",
    "age": 20,
    "grade": "A"
}
# Display original dictionary
print("Original dictionary:")
print(student)

# Add a new student detail
student["city"] = "Chennai"

# Update student's marks
student["grade"] = "A+"

# Delete a student detail
student.pop("age")

# Display all key-value pairs
print("\nStudent details:")
for key, value in student.items():
    print(key, ":", value)

# Display total number of students/details
print("\nTotal students info:", len(student))

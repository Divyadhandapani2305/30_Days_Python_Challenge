file = open("about_me.txt", "w")
file.write("Name: Divi\n")
file.write("Department: Data Science\n")
file.write("About: Learning Python easily!\n")
file.close()

print("--- FIRST TIME READING ---")
file = open("about_me.txt", "r")
print(file.read())
file.close()

file = open("about_me.txt", "a")
file.write("Goal: Becoming a Python expert!\n")
file.close()

print("--- AFTER ADDING NEW LINE ---")
file = open("about_me.txt", "r")
print(file.read())
file.close()
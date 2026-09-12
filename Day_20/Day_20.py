# : List comprehension for squares from 1 to 10
squares = [x**2 for x in range(1, 11)]

# : Dictionary comprehension for numbers (1 to 5) and their cubes
cubes = {x: x**3 for x in range(1, 6)}

# Set comprehension for even numbers from 1 to 20
evens = {x for x in range(1, 21) if x % 2 == 0}

#  Print all outputs
print("Squares List:", squares)
print("Cubes Dict:", cubes)
print("Even Numbers Set:", evens)
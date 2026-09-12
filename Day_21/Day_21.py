#Create an iterator for numbers 1 to 5 and print using next()
numbers = [1, 2, 3, 4, 5]
my_iter = iter(numbers)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#Create a generator to generate the first 10 even numbers
def even_generator():
    for i in range(1, 11):
        yield i * 2

# Use the generator in a for loop
print("\nEven Numbers from Generator:")
for num in even_generator():
    print(num, end=" ")


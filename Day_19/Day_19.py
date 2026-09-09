try:
    user_input = input("Enter numbers separated by space: ").strip()

    if not user_input:
        raise ValueError("Error: The list is empty!")
    numbers = [int(x) for x in user_input.split()]
    first_num = numbers[0]
    second_num = numbers[1]
    result = first_num / second_num

except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except IndexError:
    print("Error: Please enter at least two numbers to perform division!")
else:
    print(f"Result of division: {result}")
finally:
    print("Process finished.")
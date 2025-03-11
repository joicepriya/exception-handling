# example1:
try:
    x = 10 / 0
except ZeroDivisionError:
    print ("Cannot divide by zero!")

# example2:
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# example3:
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division was successful.")

# example4:
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always executes.")

# example 5:
try:
    x = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")

# example 6:
try:
    a = [1, 2, 3]
    print(a[5])
except IndexError:
    print("List index out of range!")
except Exception as e:
    print(f"An error occurred: {e}")

# example7:
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    else:
        print("Age is valid")

try:
    check_age(16)
except ValueError as e:
    print(f"Error: {e}")

# example 8:
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(f"Caught a custom error: {e}")

# example 9:
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# example 10:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("Execution finished.")


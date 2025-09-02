# Day 21 - Error & Exception Handling in Python

# --------------------
# Basic try-except
# --------------------
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

# --------------------
# Multiple except blocks
# --------------------
try:
    a = 10
    b = int(input("Enter a divisor: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid number.")

# --------------------
# Using finally
# --------------------
try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This will always run (like cleanup).")

# --------------------
# Using else with try
# --------------------
try:
    x = int(input("Enter a positive number: "))
    if x < 0:
        raise ValueError("Negative number not allowed.")
except ValueError as e:
    print("Error:", e)
else:
    print("Great! You entered:", x)

# --------------------
# Custom Exceptions
# --------------------
class AgeTooSmallError(Exception):
    """Custom exception for invalid age"""
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError("Age must be at least 18.")
except AgeTooSmallError as e:
    print("Custom Exception:", e)











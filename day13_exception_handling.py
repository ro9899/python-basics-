# Day 13 - Exception Handling in Python

# Example 1: Basic try-except
try:
    x = 10 / 0   # division by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Example 2: Multiple except blocks
try:
    num = int("abc")   # invalid conversion
except ValueError:
    print("Error: Invalid number format.")
except TypeError:
    print("Error: Wrong data type.")

# Example 3: Using else with try-except
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error occurred.")
else:
    print("Division successful, result =", result)

# Example 4: Using finally (always runs)
try:
    f = open("example.txt", "r")
    print("File opened successfully.")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("This block always executes (closing resources).")

# Example 5: Catching all exceptions
try:
    print(unknown_variable)   # variable not defined
except Exception as e:
    print("General error:", e)

# Example 6: Raising an exception manually
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    else:
        print("Access granted.")

try:
    check_age(16)
except ValueError as e:
    print("Custom error:", e)

# Example 7: Creating a custom exception class
class NegativeNumberError(Exception):
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of negative number.")
    return num ** 0.5

try:
    print("Square root:", square_root(-9))
except NegativeNumberError as e:
    print("Custom exception caught:", e)













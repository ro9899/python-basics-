# Day 18 - Modules & Packages in Python

# --------------------
# What is a Module?
# --------------------
# A module is just a Python file (.py) that can be imported and reused.

# Example: math module (built-in)
import math

print("Square root of 16:", math.sqrt(16))
print("Pi value:", math.pi)

# Importing specific functions
from math import factorial, pow
print("Factorial of 5:", factorial(5))
print("2 to the power of 3:", pow(2, 3))

# --------------------
# Creating a custom module
# --------------------
# Step 1: Create a file named mymodule.py with following code:
# def greet(name):
#     return f"Hello, {name}!"
#
# def add(a, b):
#     return a + b

# Step 2: Import and use it
import mymodule

print(mymodule.greet("Alice"))
print("Sum:", mymodule.add(10, 20))

# --------------------
# Packages
# --------------------
# A package is a collection of modules inside a folder with init.py

# Example package structure:
# mypackage/
#     init.py
#     greetings.py
#     calculator.py
#
# greetings.py:
# def say_hello(name):
#     return f"Hello, {name}"
#
# calculator.py:
# def multiply(a, b):
#     return a * b

# Usage:
# from mypackage.greetings import say_hello
# from mypackage.calculator import multiply
#
# print(say_hello("Bob"))
# print("Multiplication:", multiply(4, 5))

# --------------------
# The name variable
# --------------------
# Each module has a built-in variable name.
# If the module is run directly -> name == "main"
# If imported -> name == module name

def main():
    print("This code runs only when executed directly.")

if name == "main":
    main()


  

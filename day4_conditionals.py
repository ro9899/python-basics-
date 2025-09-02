# Day 4 - Conditional Statements in Python

# Example 1: Simple if
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if-else
age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Example 3: if-elif-else
marks = 72
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Example 4: Nested if
num = -3
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")

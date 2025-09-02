# Day 7 - Tuples in Python

# A tuple is similar to a list, but it is immutable (cannot be modified).

# Example 1: Creating a tuple
numbers = (10, 20, 30, 40)
print("Numbers tuple:", numbers)

# Example 2: Single-element tuple
single_element = (5,)   # notice the comma, without it Python treats it as int
print("Single element tuple:", single_element)

# Example 3: Accessing elements
print("First number:", numbers[0])
print("Last number:", numbers[-1])

# Example 4: Slicing a tuple
print("First two numbers:", numbers[:2])
print("Last two numbers:", numbers[-2:])

# Example 5: Immutability
# numbers[0] = 100   # ❌ This will give an error (tuples cannot be changed)

# Example 6: Looping through a tuple
for num in numbers:
    print("Number:", num)

# Example 7: Tuple with different data types
mixed = (1, "hello", 3.5, True)
print("Mixed tuple:", mixed)

# Example 8: Nested tuples
nested = ((1, 2), (3, 4))
print("Nested tuple:", nested)
print("Accessing element:", nested[1][0])  # row 2, col 1

# Example 9: Tuple unpacking
person = ("Alice", 25, "Engineer")
name, age, job = person
print("Name:", name)
print("Age:", age)
print("Job:", job)

# Example 10: Using tuple for swapping
a, b = 5, 10
print("Before swap: a =", a, "b =", b)
a, b = b, a
print("After swap: a =", a, "b =", b)






















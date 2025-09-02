# Day 9 - Dictionaries in Python

# A dictionary stores data as key-value pairs.

# Example 1: Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A"
}
print("Student dictionary:", student)

# Example 2: Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))   # safer way (no error if key missing)

# Example 3: Adding and updating values
student["age"] = 22         # update age
student["city"] = "London"  # add new key
print("Updated student:", student)

# Example 4: Removing items
student.pop("grade")        # remove by key
print("After pop:", student)

del student["city"]         # delete by key
print("After delete:", student)

# Example 5: Looping through dictionary
person = {"name": "Bob", "age": 25, "job": "Engineer"}

for key in person:
    print("Key:", key, "Value:", person[key])

for key, value in person.items():
    print("Key:", key, "Value:", value)

# Example 6: Dictionary methods
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# Example 7: Nested dictionary
students = {
    "s1": {"name": "Tom", "age": 20},
    "s2": {"name": "Emma", "age": 22}
}
print("Nested dictionary:", students)
print("Student s1 name:", students["s1"]["name"])

# Example 8: Using dict() constructor
car = dict(brand="Tesla", model="Model 3", year=2023)
print("Car dictionary:", car)

# Example 9: Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print("Squares dictionary:", squares)


















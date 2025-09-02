# Day 11 - Functions in Detail

# Example 1: Simple function with return value
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

# Example 2: Function with default parameter
def greet(name="Guest"):
    print("Hello,", name)

greet("Alice")
greet()  # uses default value

# Example 3: Function with keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Bob")  # order doesn’t matter when using keywords

# Example 4: Function with variable number of arguments (*args)
def total_sum(*numbers):
    return sum(numbers)

print("Total sum:", total_sum(1, 2, 3, 4, 5))

# Example 5: Function with variable keyword arguments (**kwargs)
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Charlie", age=30, city="New York")

# Example 6: Returning multiple values
def math_operations(a, b):
    return a + b, a - b, a * b, a / b

add_result, sub_result, mul_result, div_result = math_operations(10, 2)
print("Add:", add_result)
print("Subtract:", sub_result)
print("Multiply:", mul_result)
print("Divide:", div_result)

# Example 7: Nested function
def outer_function(text):
    def inner_function():
        print("Inner function says:", text)
    inner_function()

outer_function("Hello from inner function!")

# Example 8: Lambda function (anonymous function)
square = lambda x: x * x
print("Square of 6:", square(6))

# Example 9: Function as an argument
def apply_function(func, value):
    return func(value)












print("Apply square on 7:", apply_function(square, 7))

# Day 2 - Loops in Python

# ----------------------------
# 1. For Loop (Basic Example)
# ----------------------------
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)  # prints 1, 2, 3, 4, 5

print("-" * 30)

# ----------------------------
# 2. For Loop with List
# ----------------------------
fruits = ["apple", "banana", "mango"]
print("Looping through list of fruits:")
for fruit in fruits:
    print(fruit)

print("-" * 30)

# ----------------------------
# 3. While Loop (Basic Example)
# ----------------------------
print("While loop from 1 to 5:")
count = 1
while count <= 5:
    print(count)
    count += 1  # increment

print("-" * 30)

# ----------------------------
# 4. While Loop with Condition
# ----------------------------
print("While loop until user enters 'stop':")
user_input = ""
while user_input != "stop":
    user_input = input("Type something (type 'stop' to end): ")
    print("You typed:", user_input)

print("Loop ended.")



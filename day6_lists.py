# Day 6 - Lists in Python

# A list is an ordered collection of items. It can store different data types.

# Example 1: Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)

# Example 2: Accessing elements
print("First fruit:", fruits[0])     # index starts at 0
print("Last fruit:", fruits[-1])     # negative index accesses from the end

# Example 3: Changing elements
fruits[1] = "blueberry"   # replace "banana" with "blueberry"
print("Updated fruits list:", fruits)

# Example 4: Adding elements
fruits.append("mango")          # add at the end
fruits.insert(1, "orange")      # add at specific position
print("After adding items:", fruits)

# Example 5: Removing elements
fruits.remove("apple")          # remove by value
popped_item = fruits.pop()      # remove last item
print("After removing items:", fruits)
print("Popped item:", popped_item)

# Example 6: Looping through a list
for fruit in fruits:
    print("Fruit:", fruit)

# Example 7: Checking if item exists
if "cherry" in fruits:
    print("Cherry is in the list")

# Example 8: List length
print("Number of fruits:", len(fruits))

# Example 9: List slicing
numbers = [10, 20, 30, 40, 50, 60]
print("First three numbers:", numbers[:3])    # from start to index 2
print("Middle numbers:", numbers[2:5])        # from index 2 to 4
print("Last three numbers:", numbers[-3:])    # last 3 elements

# Example 10: Nested lists (list inside a list)
matrix = [[1, 2], [3, 4], [5, 6]]
print("Matrix:", matrix)
print("Element at row 2, col 1:", matrix[1][0])   # accessing nested list















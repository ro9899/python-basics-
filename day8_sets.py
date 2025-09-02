ay 8 - Sets in Python

# A set is an unordered collection of unique items.

# Example 1: Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # duplicates are ignored
print("Fruits set:", fruits)

# Example 2: Adding elements
fruits.add("mango")
print("After adding mango:", fruits)

# Example 3: Removing elements
fruits.remove("banana")   # removes banana, error if not found
print("After removing banana:", fruits)

fruits.discard("grapes")  # removes if exists, no error if not found
print("After discarding grapes (not present):", fruits)

# Example 4: Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)         # combine elements from both sets
print("Intersection:", A & B)  # common elements
print("Difference:", A - B)    # elements in A but not in B
print("Symmetric Difference:", A ^ B)  # elements in A or B but not both

# Example 5: Checking membership
print("Is 2 in A?", 2 in A)
print("Is 5 not in A?", 5 not in A)

# Example 6: Looping through a set
for item in A:
    print("Set item:", item)

# Example 7: Frozen set (immutable set)
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)
# frozen.add(4)  #  This will cause an error (cannot change frozen set)






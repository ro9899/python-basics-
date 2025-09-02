# Day 10 - Strings in Python

# A string is a sequence of characters inside quotes.

# Example 1: Creating strings
s1 = "Hello"
s2 = 'World'
s3 = """This is 
a multi-line 
string"""
print(s1, s2)
print(s3)

# Example 2: String concatenation
greeting = s1 + " " + s2
print("Concatenated string:", greeting)

# Example 3: Repetition
repeat = "Ha" * 3
print("Repetition:", repeat)

# Example 4: Indexing and slicing
text = "Python"
print("First character:", text[0])     # index 0
print("Last character:", text[-1])    # negative index
print("Slice (0:4):", text[0:4])      # characters from index 0 to 3
print("Slice (2:):", text[2:])        # from index 2 to end
print("Slice (:3):", text[:3])        # from start to index 2

# Example 5: String methods
sample = "  hello world  "
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Title case:", sample.title())
print("Stripped:", sample.strip())        # removes spaces
print("Replace:", sample.replace("world", "Python"))
print("Split:", sample.split())           # splits into list
print("Joined:", "-".join(["a", "b", "c"]))

# Example 6: Checking strings
print("Starts with 'he'?", sample.startswith("he"))
print("Ends with 'ld'?", sample.endswith("ld"))
print("Is alphabetic?", "abc".isalpha())
print("Is digit?", "123".isdigit())

# Example 7: f-strings (string formatting)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Example 8: String immutability
# Strings cannot be changed directly
word = "Python"
# word[0] = "J"   #  Error
new_word = "J" + word[1:]  #  create a new string
print("Updated word:", new_word)




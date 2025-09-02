# Day 12 - File Handling in Python

# Example 1: Writing to a file
with open("example.txt", "w") as f:   # "w" = write mode (overwrites file)
    f.write("Hello, this is the first line.\n")
    f.write("This is the second line.\n")

print("File written successfully.")

# Example 2: Reading a file
with open("example.txt", "r") as f:   # "r" = read mode
    content = f.read()
    print("\nReading entire file content:")
    print(content)

# Example 3: Reading line by line
with open("example.txt", "r") as f:
    print("\nReading file line by line:")
    for line in f:
        print(line.strip())

# Example 4: Appending to a file
with open("example.txt", "a") as f:   # "a" = append mode
    f.write("This line was appended later.\n")

print("\nText appended successfully.")

# Example 5: Reading file after append
with open("example.txt", "r") as f:
    print("\nFile content after append:")
    print(f.read())

# Example 6: Using readlines() to get list of lines
with open("example.txt", "r") as f:
    lines = f.readlines()
    print("\nList of lines:", lines)

# Example 7: Handling file not found error
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\nError: File not found!")




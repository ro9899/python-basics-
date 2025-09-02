# Day 19 - File Handling Basics in Python

# --------------------
# Writing to a file
# --------------------
# mode "w" -> write (creates new file or overwrites existing one)
with open("sample.txt", "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("Python file handling is easy!\n")

print("File written successfully.")

# --------------------
# Reading from a file
# --------------------
# mode "r" -> read
with open("sample.txt", "r") as f:
    content = f.read()   # read entire file
    print("Reading file content:")
    print(content)

# Reading line by line
with open("sample.txt", "r") as f:
    print("Reading line by line:")
    for line in f:
        print(line.strip())

# --------------------
# Appending to a file
# --------------------
# mode "a" -> append (adds content at the end without overwriting)
with open("sample.txt", "a") as f:
    f.write("This line is appended.\n")

print("Content appended successfully.")

# --------------------
# Reading again to confirm
# --------------------
with open("sample.txt", "r") as f:
    print("Final file content after append:")
    print(f.read())

# --------------------
# Common file modes:
# --------------------
# "r"  -> read
# "w"  -> write (overwrite)
# "a"  -> append
# "x"  -> create (error if file exists)
# "b"  -> binary mode (e.g. images, PDFs)
# "t"  -> text mode (default)











  

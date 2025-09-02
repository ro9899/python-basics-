# Day 30 - File Handling (Read, Write, Append, JSON, CSV)

import json
import csv

# --------------------
# Writing to a text file
# --------------------
with open("sample.txt", "w") as file:
    file.write("Hello, this is Day 30 - File Handling!\n")
    file.write("We are learning Python file operations.\n")

print("✅ Text file created and written.")


# --------------------
# Reading from a text file
# --------------------
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)


# --------------------
# Appending to a file
# --------------------
with open("sample.txt", "a") as file:
    file.write("This line was appended later.\n")

print("✅ Data appended successfully.")


# --------------------
# Reading line by line
# --------------------
with open("sample.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())


# --------------------
# JSON File Handling
# --------------------
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "ML", "Data Science"]
}

# Write JSON
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("\n✅ JSON file created.")

# Read JSON
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("Loaded JSON:", loaded_data)


# --------------------
# CSV File Handling
# --------------------
header = ["Name", "Age", "City"]
rows = [
    ["John", 28, "New York"],
    ["Emma", 22, "London"],
    ["Raj", 30, "Delhi"]
]

# Write CSV
with open("people.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerows(rows)

print("\n✅ CSV file created.")

# Read CSV
with open("people.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    print("CSV Data:")
    for row in reader:
        print(row)













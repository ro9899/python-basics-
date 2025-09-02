# Day 20 - File Handling with CSV & JSON

import csv
import json

# --------------------
# Working with CSV
# --------------------
# Writing to CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "London"])
    writer.writerow(["Charlie", 28, "Paris"])

print("CSV file written successfully.")

# Reading from CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    print("Reading CSV file:")
    for row in reader:
        print(row)

# --------------------
# Using DictWriter & DictReader
# --------------------
with open("data_dict.csv", "w", newline="") as file:
    fieldnames = ["id", "name", "score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id": 1, "name": "Alice", "score": 90})
    writer.writerow({"id": 2, "name": "Bob", "score": 85})

print("CSV file with dict written successfully.")

with open("data_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Reading dict-style CSV:")
    for row in reader:
        print(row)

# --------------------
# Working with JSON
# --------------------
data = {
    "employees": [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "London"},
    ]
}

# Writing JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON file written successfully.")

# Reading JSON
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print("Reading JSON file:")
    print(loaded_data)

# --------------------
# Converting between JSON <-> Python
# --------------------
# Python dict to JSON string
json_string = json.dumps(data, indent=2)
print("Python dict converted to JSON string:")
print(json_string)

# JSON string to Python dict
dict_data = json.loads(json_string)
print("JSON string converted back to Python dict:")
print(dict_data)

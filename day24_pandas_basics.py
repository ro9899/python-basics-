# Day 24 - Pandas Basics

import pandas as pd

# --------------------
# Creating Series (1D data)
# --------------------
data = [10, 20, 30, 40]
series = pd.Series(data, index=["a", "b", "c", "d"])
print("Pandas Series:\n", series)

# --------------------
# Creating DataFrame (2D data like Excel)
# --------------------
data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}
df = pd.DataFrame(data_dict)
print("\nDataFrame:\n", df)

# --------------------
# Reading & Writing CSV
# --------------------
# Save DataFrame to CSV
df.to_csv("people.csv", index=False)

# Read DataFrame from CSV
df_csv = pd.read_csv("people.csv")
print("\nDataFrame from CSV:\n", df_csv)

# --------------------
# DataFrame Operations
# --------------------
print("\nColumn 'Name':\n", df["Name"])
print("First 2 rows:\n", df.head(2))
print("Describe Data:\n", df.describe())

# --------------------
# Filtering Data
# --------------------
print("\nPeople older than 28:\n", df[df["Age"] > 28])

# --------------------
# Adding a new column
# --------------------
df["Country"] = ["USA", "UK", "France"]
print("\nDataFrame with new column:\n", df)

# --------------------
# Grouping Data
# --------------------
grouped = df.groupby("City")["Age"].mean()
print("\nGrouped by City (Average Age):\n", grouped)








# Day 25 - Data Visualization with Matplotlib

import matplotlib.pyplot as plt

# --------------------
# Line Plot
# --------------------
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label="Line Plot", marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.legend()
plt.show()

# --------------------
# Bar Chart
# --------------------
categories = ["A", "B", "C", "D"]
values = [10, 24, 36, 18]

plt.bar(categories, values, color="skyblue")
plt.title("Bar Chart Example")
plt.show()

# --------------------
# Pie Chart
# --------------------
sizes = [30, 25, 20, 25]
labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart Example")
plt.show()

# --------------------
# Scatter Plot
# --------------------
x = [5, 7, 8, 7, 6, 9, 5, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y, color="red")
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# --------------------
# Histogram
# --------------------
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

plt.hist(data, bins=5, color="green", alpha=0.7)
plt.title("Histogram Example")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()












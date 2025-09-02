# Day 26 - Data Visualization with Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# --------------------
# Sample Data
# --------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [25, 30, 35, 40, 28, 32],
    "Salary": [50000, 60000, 75000, 80000, 65000, 70000],
    "Department": ["HR", "IT", "IT", "Finance", "Finance", "HR"]
}
df = pd.DataFrame(data)

# --------------------
# Histogram / Distribution Plot
# --------------------
sns.histplot(df["Age"], bins=5, kde=True, color="skyblue")
plt.title("Age Distribution")
plt.show()

# --------------------
# Scatter Plot
# --------------------
sns.scatterplot(x="Age", y="Salary", hue="Department", data=df, s=100)
plt.title("Age vs Salary by Department")
plt.show()

# --------------------
# Box Plot
# --------------------
sns.boxplot(x="Department", y="Salary", data=df, palette="Set2")
plt.title("Salary Distribution by Department")
plt.show()

# --------------------
# Heatmap (Correlation)
# --------------------
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# --------------------
# Pair Plot
# --------------------
sns.pairplot(df, hue="Department")
plt.suptitle("Pair Plot Example", y=1.02)
plt.show()












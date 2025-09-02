# Day 23 - NumPy Basics

import numpy as np

# --------------------
# Creating Arrays
# --------------------
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# --------------------
# Array Properties
# --------------------
print("Shape of arr2:", arr2.shape)
print("Size of arr2:", arr2.size)
print("Data type of arr2:", arr2.dtype)

# --------------------
# Special Arrays
# --------------------
zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
identity = np.eye(4)

print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Identity Matrix:\n", identity)

# --------------------
# Array Operations
# --------------------
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# --------------------
# Matrix Operations
# --------------------
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Matrix Multiplication:\n", np.dot(m1, m2))
print("Transpose:\n", m1.T)

# --------------------
# Useful Functions
# --------------------
rand_arr = np.random.rand(3, 3)  # random numbers between 0 and 1
print("Random Array:\n", rand_arr)

lin_space =

















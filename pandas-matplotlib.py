# Assignment 2: Implementation of Pandas and Matplotlib
# Dept. of Computer Science, S.P. College, Pune

# ============================================
# Import required libraries
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================
# a) Create a Series using pandas and display
# ============================================

print("=== a) Create a Series using pandas ===")
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Pandas Series:")
print(series)
print("\n")

# ============================================
# b) Access the index and the values of our Series
# ============================================

print("=== b) Access index and values ===")
print("Series Index:", series.index)
print("Series Values:", series.values)
print("\n")

# ============================================
# c) Compare an array using NumPy with a Series using pandas
# ============================================

print("=== c) Compare NumPy Array with Pandas Series ===")
np_array = np.array([10, 20, 30, 40, 50])
pd_series = pd.Series([10, 20, 30, 40, 50])
print("NumPy Array:\n", np_array)
print("Pandas Series:\n", pd_series)
print("Are they equal element-wise?", np_array == pd_series.values)
print("\n")

# ============================================
# d) Define Series objects with individual indices
# ============================================

print("=== d) Define Series with custom indices ===")
series_custom = pd.Series([100, 200, 300], index=["A", "B", "C"])
print("Custom Indexed Series:")
print(series_custom)
print("\n")

# ============================================
# e) Access single value of a Series
# ============================================

print("=== e) Access a single value ===")
print("Value at index 'B':", series_custom["B"])
print("Value using integer index [2]:", series_custom.iloc[2])
print("\n")

# ============================================
# f) Load datasets in a DataFrame variable using pandas
# ============================================

print("=== f) Load dataset into DataFrame ===")

# Creating sample dataset manually for demonstration
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "Score": [85, 90, 88, 76, 95]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\n")

# Accessing DataFrame properties
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)
print("Describe():\n", df.describe())
print("\n")

# ============================================
# g) Usage of different methods in Matplotlib
# ============================================

print("=== g) Matplotlib Visualization ===")

# Line plot
plt.figure(figsize=(6, 4))
plt.plot(df["Name"], df["Score"], marker='o', color='blue')
plt.title("Line Plot: Student Scores")
plt.xlabel("Name")
plt.ylabel("Score")
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(6, 4))
plt.bar(df["Name"], df["Age"], color='orange')
plt.title("Bar Plot: Student Ages")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()

# Scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(df["Age"], df["Score"], color='green')
plt.title("Scatter Plot: Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.show()

# Histogram
plt.figure(figsize=(6, 4))
plt.hist(df["Score"], bins=5, color='purple', edgecolor='black')
plt.title("Histogram: Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

# Pie chart
plt.figure(figsize=(5, 5))
plt.pie(df["Score"], labels=df["Name"], autopct='%1.1f%%')
plt.title("Pie Chart: Scores Percentage")
plt.show()

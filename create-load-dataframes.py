# Assignment 3: Creation and Loading Different Types of Datasets
# Dept. of Computer Science, S.P. College, Pune

# ============================================
# i. Dataset Creation using Pandas
# ============================================

import pandas as pd
import numpy as np
from sklearn import datasets

print("=== 1. Creating DataFrame from Dictionary ===")
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'London', 'Paris']
}
df_dict = pd.DataFrame(data_dict)
print(df_dict, "\n")

print("=== 2. Creating DataFrame from List of Lists ===")
data_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 22, 'Paris']
]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print(df_list, "\n")

print("=== 3. Creating DataFrame from List of Dictionaries ===")
data_dict_list = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'London'},
    {'Name': 'Charlie', 'Age': 22, 'City': 'Paris'}
]
df_dict_list = pd.DataFrame(data_dict_list)
print(df_dict_list, "\n")

print("=== 4. Creating DataFrame from NumPy Array ===")
data_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_np = pd.DataFrame(data_np, columns=['ColA', 'ColB', 'ColC'])
print(df_np, "\n")

# ============================================
# ii. Loading CSV Dataset File using Pandas
# ============================================

# Example: Load from CSV (if available in same directory)
# df_csv = pd.read_csv('data.csv')
# print("Loaded CSV File:\n", df_csv.head())

print("=== Example CSV Loading Code ===")
print("df_csv = pd.read_csv('data.csv')\nprint(df_csv.head())\n")

# ============================================
# iii. Loading Datasets using sklearn
# ============================================

print("=== Loading Datasets from sklearn ===")

from sklearn.datasets import load_iris, load_digits, load_diabetes

# Load Iris dataset
iris = load_iris()
X_iris, y_iris = iris.data, iris.target
print("Iris Dataset Shape:", X_iris.shape)

# Load Digits dataset
digits = load_digits()
print("Digits Dataset Shape:", digits.data.shape)

# Load Diabetes dataset
diabetes = load_diabetes()
print("Diabetes Dataset Shape:", diabetes.data.shape, "\n")

# ============================================
# iv. Loading Datasets into Google Colab
# ============================================

print("=== Example Code for Google Colab Upload ===")
print("from google.colab import files\nuploaded = files.upload()\n")

# ============================================
# b) Compute Mean, Median, Mode, Variance, Standard Deviation
# ============================================

print("=== Basic Statistical Computations ===")

# Create sample dataset
data_stats = pd.DataFrame({
    'Scores': [56, 75, 45, 71, 62, 64, 58, 80, 76, 67]
})

mean_value = data_stats['Scores'].mean()
median_value = data_stats['Scores'].median()
mode_value = data_stats['Scores'].mode()[0]
variance_value = data_stats['Scores'].var()
std_dev_value = data_stats['Scores'].std()

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)
print("\n")

# ============================================
# c) Data Pre-processing Techniques
# ============================================

print("=== Data Pre-processing Techniques ===")

# Create sample DataFrame for preprocessing
df_pre = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [25, np.nan, 28, 22, np.nan],
    'Salary': [50000, 54000, np.nan, 58000, 60000],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance']
})

print("Original DataFrame:\n", df_pre, "\n")

# --------------------------------------------
# i. Reshaping the Data
# --------------------------------------------

print("i) Reshaping Data (Melt Example)")
reshaped_df = pd.melt(df_pre, id_vars=['Name'], value_vars=['Age', 'Salary'])
print(reshaped_df, "\n")

# --------------------------------------------
# ii. Filtering the Data
# --------------------------------------------

print("ii) Filtering: Employees with Salary > 55000")
filtered_df = df_pre[df_pre['Salary'] > 55000]
print(filtered_df, "\n")

# --------------------------------------------
# iii. Merging the Data
# --------------------------------------------

print("iii) Merging Two DataFrames")
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Department': ['HR', 'IT', 'Finance']})
merged_df = pd.merge(df1, df2, on='ID')
print(merged_df, "\n")

# --------------------------------------------
# iv. Handling Missing Values
# --------------------------------------------

print("iv) Handling Missing Values")
print("Before:\n", df_pre, "\n")

# Fill missing values with mean or a specific value
df_pre['Age'].fillna(df_pre['Age'].mean(), inplace=True)
df_pre['Salary'].fillna(df_pre['Salary'].median(), inplace=True)
print("After filling missing values:\n", df_pre, "\n")

# --------------------------------------------
# v. Feature Normalization (Min-Max & Standard)
# --------------------------------------------

print("v) Feature Normalization")

# Min-Max Normalization
df_pre['Age_MinMax'] = (df_pre['Age'] - df_pre['Age'].min()) / (df_pre['Age'].max() - df_pre['Age'].min())

# Z-Score (Standard) Normalization
df_pre['Salary_ZScore'] = (df_pre['Salary'] - df_pre['Salary'].mean()) / df_pre['Salary'].std()

print("After Normalization:\n", df_pre)

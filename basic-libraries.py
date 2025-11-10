# Assignment 1: Implementation of Python Basic Libraries
# Dept. of Computer Science, S.P. College, Pune

# ============================================
# a) Usage of Math Library Functions
# ============================================

import math

print("=== Math Library Functions ===")
print("math.floor(3.7):", math.floor(3.7))
print("math.floor(-2.3):", math.floor(-2.3))
print("math.ceil(3.2):", math.ceil(3.2))
print("math.ceil(-2.7):", math.ceil(-2.7))
print("math.sqrt(25):", math.sqrt(25))
print("math.sqrt(2):", math.sqrt(2))
print("math.isqrt(25):", math.isqrt(25))
print("math.isqrt(26):", math.isqrt(26))
print("math.isqrt(0):", math.isqrt(0))
print("math.gcd(48, 18):", math.gcd(48, 18))
print("math.gcd(17, 5):", math.gcd(17, 5))

# Other common math functions
print("math.pow(2, 3):", math.pow(2, 3))
print("math.factorial(5):", math.factorial(5))
print("math.log(10):", math.log(10))
print("math.sin(math.pi/2):", math.sin(math.pi/2))
print("math.cos(0):", math.cos(0))
print("\n")

# ============================================
# b) Usage of NumPy Array Attributes and Methods
# ============================================

import numpy as np

print("=== NumPy Array Attributes and Methods ===")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
print("Dimensions (ndim):", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Sorted array:\n", np.sort(arr))
print("Sine values:\n", np.sin(arr))
print("\n")

# ============================================
# c) Determinant and Eigenvalues using NumPy
# ============================================

print("=== NumPy Linear Algebra Functions ===")
matrix = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(matrix)
print("Matrix:\n", matrix)
print("Determinant:", determinant)

eigenvalues, eigenvectors = np.linalg.eig(np.array([[2, 2], [1, 3]]))
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
print("\n")

# ============================================
# d) Reshaping 1D List into 2D and 3D Matrices
# ============================================

print("=== Reshape Example ===")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
np_array = np.array(my_list)
print("Original 1D Array:", np_array)
print("Shape:", np_array.shape)

matrix_2d = np_array.reshape(3, 4)
print("\n2D Matrix (3x4):\n", matrix_2d)
print("Shape:", matrix_2d.shape)

matrix_3d = np_array.reshape(2, 2, 3)
print("\n3D Matrix (2x2x3):\n", matrix_3d)
print("Shape:", matrix_3d.shape)
print("\n")

# ============================================
# e) NumPy Random Generator and Matrices
# ============================================

print("=== NumPy Random Generator ===")
rng = np.random.default_rng(seed=42)
random_floats = rng.random(size=(2, 3))
random_integers = rng.integers(low=1, high=11, size=(3, 3))
normal_values = rng.normal(loc=0, scale=1, size=(2, 2))

print("Random Floats (2x3):\n", random_floats)
print("Random Integers (3x3):\n", random_integers)
print("Normal Distribution Values (2x2):\n", normal_values)

matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("\nMatrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# Matrix multiplication
product = np.dot(matrix_a, matrix_b)
print("\nMatrix Multiplication Result:\n", product)

# Transpose
print("\nTranspose of A:\n", matrix_a.T)

# Element-wise addition
sum_matrices = matrix_a + matrix_b
print("\nElement-wise Addition:\n", sum_matrices)
print("\n")

# ============================================
# f) Determinant using SciPy
# ============================================

from scipy import linalg

print("=== Determinant using SciPy ===")
matrix_A = np.array([[3, 1, 4],
                     [1, 5, 9],
                     [2, 6, 5]])
determinant_A = linalg.det(matrix_A)
print("Matrix A:\n", matrix_A)
print("Determinant of Matrix A:", determinant_A)
print("\n")

# ============================================
# g) Eigenvalues and Eigenvectors using SciPy
# ============================================

from scipy.linalg import eig

print("=== Eigenvalues and Eigenvectors using SciPy ===")
A = np.array([[2, 1],
              [1, 2]])
eigenvalues, eigenvectors = eig(A)
print("Matrix A:\n", A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

import numpy as np

# a) Third column of a 2D array
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
print("Third Column:", a[:,2])

# b) Reverse a 1D array
arr = np.array(list(map(int, input("Enter numbers: ").split())))
print("Reversed:", arr[::-1])

# c) Matrix multiplication
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9,10],
              [11,12,13,14],
              [15,16,17,18]])
print("Matrix Multiplication:\n", A @ B)

# d) Determinant of a 3x3 matrix
M = np.array(list(map(int, input("Enter 9 elements: ").split()))).reshape(3,3)
print("Determinant:", np.linalg.det(M))
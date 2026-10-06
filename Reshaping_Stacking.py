import numpy as np

# a) Create a 1D array of 10 evenly spaced values between 0 and 1
arr = np.linspace(0, 1, 10)
print("Evenly Spaced Array:")
print(arr)

# b) Generate a 3x3 identity matrix
identity = np.eye(3)
print("\nIdentity Matrix:")
print(identity)

# c) User input for reshaping
print("\nEnter 10 elements:")

array = np.array([int(input()) for i in range(10)])

reshaped = array.reshape(2, 5)

print("\nReshaped Array (2x5):")
print(reshaped)

# d) User input for stacking
print("\nEnter 4 elements for First 2x2 Matrix:")
a = np.array([int(input()) for i in range(4)]).reshape(2, 2)

print("\nEnter 4 elements for Second 2x2 Matrix:")
b = np.array([int(input()) for i in range(4)]).reshape(2, 2)

print("\nFirst Matrix:")
print(a)

print("\nSecond Matrix:")
print(b)

vertical = np.vstack((a, b))
horizontal = np.hstack((a, b))

print("\nVertical Stack:")
print(vertical)

print("\nHorizontal Stack:")
print(horizontal)
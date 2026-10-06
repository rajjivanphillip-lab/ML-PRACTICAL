import numpy as np

# a) Create a 1D array with elements from 0 to 9
arr1 = np.arange(10)
print("1D Array:")
print(arr1)

# b) Create a 2D array with shape (3,4) filled with random numbers
arr2 = np.random.rand(3, 4)
print("\n2D Random Array:")
print(arr2)

# c) User input array
n = int(input("\nEnter the number of elements: "))

print("Enter the elements:")
arr = np.array([float(input()) for i in range(n)])

print("\nArray:", arr)

mean = np.mean(arr)
std = np.std(arr)

print("Mean =", mean)
print("Standard Deviation =", std)

# d) Normalize the array
normalized = (arr - mean) / std

print("Normalized Array:")
print(normalized)
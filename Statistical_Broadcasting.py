import numpy as np

# a) Mean of rows and columns
arr = np.random.randint(1, 100, (3, 4))
print("Array:\n", arr)
print("Row Mean:", np.mean(arr, axis=1))
print("Column Mean:", np.mean(arr, axis=0))

# b) Minimum and Maximum
a = np.array(list(map(int, input("Enter elements: ").split())))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))

# c) Add a constant to every element
c = int(input("Enter constant: "))
print("Result:", a + c)

# d) Row-wise multiplication
r, col = map(int, input("Enter rows and columns: ").split())
m = np.array([list(map(int, input().split())) for i in range(r)])
k = np.array(list(map(int, input("Enter row constants: ").split())))
print("Result:\n", m * k.reshape(r, 1))
import numpy as np

# Dataset
data = np.array([12.5,12.5,12.5,12.5,12.5,
                 17.5,17.5,17.5,17.5,17.5,17.5,
                 22.5,22.5,22.5,22.5,22.5,22.5,22.5,22.5,22.5,
                 27.5,27.5,27.5,27.5,27.5,27.5,27.5,27.5,
                 32.5,32.5])

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Mode
values, counts = np.unique(data, return_counts=True)
mode = values[np.argmax(counts)]

# Variance
variance = np.var(data)

# Standard Deviation
std = np.std(data)

# Display Results
print("Dataset:")
print(data)

print("\nMean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std)
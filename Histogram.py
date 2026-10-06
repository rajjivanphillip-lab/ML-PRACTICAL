import numpy as np
import matplotlib.pyplot as plt

# Dataset
data = np.array([12.5,12.5,12.5,12.5,12.5,
                 17.5,17.5,17.5,17.5,17.5,17.5,
                 22.5,22.5,22.5,22.5,22.5,22.5,22.5,22.5,22.5,
                 27.5,27.5,27.5,27.5,27.5,27.5,27.5,27.5,
                 32.5,32.5])

# Plot Histogram
plt.hist(data,
         bins=[10,15,20,25,30,35],
         edgecolor='black')

plt.title("Histogram")
plt.xlabel("Class Interval")
plt.ylabel("Frequency")

plt.show()
import matplotlib.pyplot as plt

# Dataset
data = [3, 7, 8, 5, 12, 14, 21, 13, 18]

# Draw Box-and-Whisker Plot
plt.boxplot(data)

# Add title and label
plt.title("Box-and-Whisker Plot")
plt.ylabel("Values")

# Display the plot
plt.show()
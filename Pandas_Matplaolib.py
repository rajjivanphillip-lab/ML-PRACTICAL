# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create Dataset
data = {
    "Name": ["John", "Mary", "Alex", "David", "Sophia"],
    "Marks": [85, 92, 78, 88, 95],
    "Age": [20, 21, 19, 22, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Dataset")
print(df)

# Basic Analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# Plot Bar Graph
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.show()
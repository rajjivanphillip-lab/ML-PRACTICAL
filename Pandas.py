# Import the pandas library
import pandas as pd

# Create a list containing student data
data = [
    ["John", 20, 85],
    ["Mary", 21, 92],
    ["Alex", 19, 78],
    ["David", 22, 88]
]

# Create a DataFrame from the list
df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])

# Display the DataFrame
print("Student DataFrame")
print(df)
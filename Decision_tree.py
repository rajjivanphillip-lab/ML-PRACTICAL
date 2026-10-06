import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    "Outlook": ["Sunny", "Sunny", "Rainy", "Rainy", "Overcast"],
    "Temperature": ["Hot", "Mild", "Cool", "Mild", "Hot"],
    "Play": ["No", "No", "Yes", "Yes", "Yes"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert text to numbers
le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

# Input and Output
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Create and train Decision Tree using Entropy (ID3)
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# New sample
sample = pd.DataFrame([[2, 1]], columns=["Outlook", "Temperature"])

# Prediction
prediction = model.predict(sample)

print("Prediction:", prediction)

# Display Decision Tree
plt.figure(figsize=(10, 6))

plot_tree(
    model,
    feature_names=["Outlook", "Temperature"],
    class_names=["No", "Yes"],
    filled=True,
    rounded=True
)

plt.title("Decision Tree using Entropy (ID3)")
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Read Iris dataset from CSV
data = pd.read_csv("iris.csv")

# Input features
X = data.iloc[:, :-1]

# Output class
y = data.iloc[:, -1]

# Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

correct = 0
wrong = 0

# Print predictions
for actual, predicted in zip(y_test, y_pred):

    if actual == predicted:
        print("Correct Prediction:", actual, "->", predicted)
        correct += 1

    else:
        print("Wrong Prediction:", actual, "->", predicted)
        wrong += 1

# Print results
print("\nCorrect Predictions:", correct)
print("Wrong Predictions:", wrong)

# Accuracy
accuracy = correct / len(y_test) * 100
print("Accuracy:", accuracy, "%")
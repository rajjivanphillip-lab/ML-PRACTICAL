import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

# Read CSV
data = pd.read_csv("naive_bayes_data.csv")

# Input and output
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Convert text data to numbers
for col in X.columns:
    X[col] = LabelEncoder().fit_transform(X[col])

y = LabelEncoder().fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = CategoricalNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Actual:", y_test)
print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")
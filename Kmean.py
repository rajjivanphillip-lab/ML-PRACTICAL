import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read CSV
data = pd.read_csv("kmeans_data.csv")

# Select data
X = data[["X", "Y"]]

# Create K-Means model
model = KMeans(n_clusters=2, random_state=42)

# Train and predict clusters
data["Cluster"] = model.fit_predict(X)

# Print result
print(data)

# Plot clusters
plt.scatter(data["X"], data["Y"], c=data["Cluster"])

plt.xlabel("X")
plt.ylabel("Y")
plt.title("K-Means Clustering")

plt.show()
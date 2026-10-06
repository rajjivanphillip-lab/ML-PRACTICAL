import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

data = pd.read_csv("data.csv")

D = squareform(pdist(data, metric="euclidean"))
print("Distance matrix:\n", pd.DataFrame(D), "\n")

model = AgglomerativeClustering(n_clusters=2, linkage="single")
data["cluster"] = model.fit_predict(data)

print("Data with assigned clusters:\n", data)

Z = linkage(data.drop(columns="cluster"), method="single")

plt.figure()
dendrogram(Z, labels=[f"P{i}" for i in data.index])
plt.title("Dendrogram (Single Linkage)")
plt.xlabel("Data points")
plt.ylabel("Distance")
plt.show()
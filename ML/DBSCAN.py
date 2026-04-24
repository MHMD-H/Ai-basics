import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score, davies_bouldin_score

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/r-maSj5Yegvw2sJraT15FA/ODCAF-v1-0.csv"
df = pd.read_csv(url, encoding="ISO-8859-1")

# تنظيف
df = df[df["ODCAF_Facility_Type"] == "gallery"]
df = df[df["Latitude"] != ".."]

df["Latitude"] = df["Latitude"].astype(float)
df["Longitude"] = df["Longitude"].astype(float)

# features
X = df[["Latitude", "Longitude"]]

# scaling مهم جدًا مع DBSCAN
from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(X)

# model
model = DBSCAN(eps=0.3, min_samples=5)
labels = model.fit_predict(X_scaled)

df["cluster"] = labels

# remove noise (-1) for evaluation
mask = labels != -1

# evaluation (internal metrics)
sil = silhouette_score(X_scaled[mask], labels[mask])
db = davies_bouldin_score(X_scaled[mask], labels[mask])

print("Silhouette Score:", sil)
print("Davies-Bouldin Score:", db)
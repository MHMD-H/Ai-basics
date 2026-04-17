import numpy as np 
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%204/data/Cust_Segmentation.csv")

df = df.drop("Address", axis=1)
df = df.dropna()

x = df.iloc[:, 1:]

# Scaling
norm = StandardScaler()
x_norm = norm.fit_transform(x)

k_n = [2,3,4,5,6,]
k_accu = []

for k in k_n :
    k_mean = KMeans(init="k-means++", n_clusters=k, n_init=200, random_state=42)
    k_mean.fit(x_norm)

    label = k_mean.labels_
    score = silhouette_score(x_norm, label)

    k_accu.append(score)
best_k = k_n[np.argmax(k_accu)]
print(f"Best Silhouette Score: {np.max(k_accu)} with no. k is : {best_k} ")
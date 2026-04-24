import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

np.random.seed(42)
n = 200
df = pd.DataFrame({
    'electricity_kwh':  np.random.normal(500, 100, n),
    'water_liters':     np.random.normal(300,  60, n),
    'temperature_c':    np.random.normal( 22,   5, n),
    'humidity_pct':     np.random.normal( 55,  10, n),
    'gas_usage':        np.random.normal(150,  30, n),
})
#print(df)




x= df.drop("electricity_kwh",axis=1)

norm = StandardScaler()
x_SCaled = norm.fit_transform(x)

#pca 

pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_SCaled) #x_pca1 , x_pca1
print(x_pca)

component = pca.components_ #wieghts(w)
#[[-0.48877532  0.300636    0.58348522  0.57468398] x_pca1 = w1.x1 + w2.x2 +w3.X3 + w4.x4
#[ 0.36342014  0.85807258  0.17522428 -0.31770066]] 
print(component)


x_Pca_proj=np.dot(x_SCaled,component.T)#=x_pca = pca.fit_transform(x_SCaled) 
print(x_Pca_proj)


k_n=list(range(2,8))
best_k = np.zeros(len(k_n))

for i,k in enumerate(k_n) :
    k_mean =KMeans(init = "k-means++" ,n_clusters=k,random_state=42)
    k_mean.fit(x_pca) 
    label =k_mean.labels_
    score =silhouette_score(x_pca,label)
    best_k[i] = score
best_k_n = k_n[np.argmax(best_k)]
best_model = KMeans(init="k-means++",n_clusters=best_k_n,random_state=42)
print(best_model)

best_model.fit(x_pca)
df["cluster"] = best_model.predict(x_pca)


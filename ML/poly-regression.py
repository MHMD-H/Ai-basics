import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

file = r"C:\Users\moham_f78sqay\Downloads\Advertising.csv"
df = pd.read_csv(file)

print(df.corr())
df = df.drop(["Unnamed: 0","newspaper"],axis=1)
print(df)

x = df[["TV","radio"]]
y = df["sales"]
#manual model
from sklearn.preprocessing import StandardScaler,PolynomialFeatures

norm = StandardScaler()
x_std = norm.fit_transform(x)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x_std)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x_train,x_test,y_train,y_test = train_test_split(x_poly,y,test_size=.2,random_state=42)

reg = LinearRegression()
reg.fit(x_train,y_train)
y_pred = reg.predict(x_test)
print(y_pred)

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_std[:,0], x_std[:,1], y, color='red')

# surface
import numpy as np
x_surf, y_surf = np.meshgrid(np.linspace(x_std[:,0].min(), x_std[:,0].max(), 20), np.linspace(x_std[:,1].min(), x_std[:,1].max(), 20))
xy = np.column_stack([x_surf.ravel(), y_surf.ravel()])
xy_poly = poly.transform(xy)
z_surf = reg.predict(xy_poly).reshape(x_surf.shape)

ax.plot_surface(x_surf, y_surf, z_surf, alpha=0.3, color='blue')
ax.set_xlabel("TV")
ax.set_ylabel("Radio")
ax.set_zlabel("Sales")
plt.show()


#by grid search & pipeline
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV,cross_val_predict,cross_val_score

liner_pipe = Pipeline([
    ("poly",PolynomialFeatures()),
    ("linear",LinearRegression()),
    ("norm",StandardScaler())
])

score_cv = cross_val_predict(liner_pipe,x,y,cv=5)
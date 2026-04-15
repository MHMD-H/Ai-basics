import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures , StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

path = r"C:\Users\moham_f78sqay\Downloads\experience_salary.csv"
df = pd.read_csv(path)
print(df)

#1. choose data 
x=df[["Experience"]]
y=df["Salary"]
# ____________________________________________________

#first way
#1.transform data to polynomial regression
poly = PolynomialFeatures(degree=3) #define the class 
x_poly = poly.fit_transform(x) #transform data

#2.normalization
norm=StandardScaler()#define the class
x_poly_norm = norm.fit_transform(x_poly)

#3.train model
model = LinearRegression()#define the class
model.fit(x_poly_norm,y)#set the values

#4.make prediction
y_predicted = model.predict(x_poly_norm)

#5.plot the gragh
X_fit = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
X_fit_poly = poly.transform(X_fit)#transform to polynomial
X_fit_poly_norm = norm.transform(X_fit_poly)#normalization
y_fit = model.predict(X_fit_poly_norm)

plt.plot(X_fit, y_fit, color="blue", label="Polynomial Regression")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()
#________________________________________________________________________
#second way(Pipe line) :

Pipe = Pipeline([
    ("Poly",PolynomialFeatures(degree=3)), #transform to poly
    ("Scale",StandardScaler()),#Normalization
    ("model",LinearRegression()),#Train model
])

Pipe.fit(x,y)
y_predicted=Pipe.predict(x)
plt.scatter(x=x,y=y,color="black")
plt.plot(x,y_predicted)
plt.show()

#additional information 
#to select the best degree:
from sklearn.model_selection import cross_val_score
degrees = [1, 2, 3, 5, 10]
for d in degrees:
    model = Pipeline([
        ("poly", PolynomialFeatures(degree=d)),
        ("reg", LinearRegression())
    ])
    scores = cross_val_score(model, x, y, cv=5, scoring="r2")
    print(f"الدرجة = {d}, متوسط R² = {scores.mean():.3f}")
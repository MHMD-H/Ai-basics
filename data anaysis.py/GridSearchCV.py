import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import cross_val_score,cross_val_predict,train_test_split,GridSearchCV
from sklearn.linear_model import LinearRegression,Ridge

path = "employee_data.csv"
df = pd.read_csv(path)
print(df)
print("_"*50)

#organise data
df_encoded = pd.get_dummies(df,columns=["Gender","Department"],drop_first=True).astype("int")
print(df_encoded)
print("_"*50)

#select data
x= df_encoded.drop("Salary",axis=1)
y=df["Salary"]

#select model
#1.linear model
linear_pipe = Pipeline([
    ("poly",PolynomialFeatures(degree=5)),
    ("scaling",StandardScaler()),
    ("model",LinearRegression())
])
score_linar=cross_val_score(linear_pipe,x,y,cv=5,scoring="r2")
print(f"the average R^2 is {score_linar.mean()}")
y_pred_linear = cross_val_predict(linear_pipe,x,y,cv=5)
print(f"the average prdiction is {y_pred_linear.mean()}")

#2.ridge- --> decrease noise

ridge_pipe = Pipeline([
    ("poly",PolynomialFeatures()),
    ("scaling",StandardScaler()),
    ("Ridge",Ridge())
])
score_ridge=cross_val_score(ridge_pipe,x,y,cv=5,scoring="r2")

print(f"the average R^2 is {score_ridge.mean()}")
y_pred_ridge = cross_val_predict(ridge_pipe,x,y,cv=5)
print(f"the average prdiction is {y_pred_ridge.mean()}")
ridge_pipe.fit(x,y)
# GridSearchCV --> select best hyper parameter
hyper_p = {
    "poly__degree": [2,3,4,5,6,7,8,9],   # درجات polynomial 
    "Ridge__alpha": [0.001,0.01,1,10,100]  # قيم alpha
}

grid = GridSearchCV(ridge_pipe, hyper_p, cv=5, scoring="r2")
grid.fit(x, y)


print("Best Parameters:", grid.best_params_)
print("Best R^2 Score:", grid.best_score_)


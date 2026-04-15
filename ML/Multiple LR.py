import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression



df = pd.read_csv(r"C:\Users\moham_f78sqay\Downloads\supermarket_dataset.csv")
print(df)

corr = df.select_dtypes(include=["int64","float64"])
print(corr.corr())

if df["Revenue"].isna().all():
    df["Revenue"] = df["Price"] * df["QuantitySold"]

x= df.drop(["Revenue"],axis=1)

y=df["Revenue"]

scale = StandardScaler()
x_norm = scale.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x_norm,y,test_size=.2,random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)

y_predicted = model.predict(x_test)

coff1 = model.coef_[0]
coff2 = model.coef_[1]
interc = model.intercept_

print(f"the equation is ")

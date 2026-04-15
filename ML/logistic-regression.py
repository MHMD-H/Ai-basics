import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file =r"C:\Users\moham_f78sqay\Downloads\titanic_mini_50.csv"

df = pd.read_csv(file)

df = pd.get_dummies(data=df,columns=["Survived","Sex"],drop_first=True)
df["Survived_Yes"] = df["Survived_Yes"].astype("int")
df["Sex_male"] = df["Sex_male"].astype("int")
df.rename(columns= {"Survived_Yes" : "Survived"},inplace=True)
print(df.head(5))

x = df.iloc[:,:-1]
y = df["Survived"]
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
x_norm = scale.fit_transform(x)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

x_train,x_test,y_train,y_test = train_test_split(x_norm,y,test_size=.2,random_state=40)

lr = LogisticRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict(x_test)

print(x_test)

y_prop = lr.predict_proba(x_test)
print(y_prop)
x_age = x_test[:,1]
print(x_age)
plt.scatter(x_age, y_prop[:,1])
plt.scatter(x_age, y_prop[:,0],marker="x",color = "red")
plt.xlabel("Age (standardized)")
plt.ylabel("Probability of Survived")
plt.show()

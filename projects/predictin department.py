import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.linear_model import LinearRegression

path = r"C:\Users\moham_f78sqay\Downloads\departments.csv"
df = pd.read_csv(path)
print(df)
print("_"*50)

df_encoded = pd.get_dummies(df,columns=["City"],drop_first=True).astype("int")
print(df_encoded)
print("_"*50)


x = df_encoded.drop("Price",axis=1)
y=df_encoded["Price"]

model = LinearRegression()

model.fit(x,y)

prediction = model.predict(x)

sns.regplot(x=x,y=y)
plt.show()
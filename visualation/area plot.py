import pandas as pd
import numpy as bp
import matplotlib.pyplot as plt
file = r"C:\Users\moham_f78sqay\Downloads\sales_data (1).csv"
df = pd.read_csv(file)
print(df.dtypes)
print(df.columns)
print(df)
df.set_index(["Company"],inplace=True)
df.index.name=None
print(df)
df["total"] = df.loc[:, "2010":"2020"].sum(axis=1)
#axis = 0 --> sum columns
#axis = 1 --> sum rows
print(df)
df_sorted = df.sort_values(by="total",ascending=False,axis=0)
df_3 = df_sorted.head(3).transpose()

df_3.plot(kind="area",alpha=.3)
plt.xlabel("years")
plt.ylabel("company")
plt.show()
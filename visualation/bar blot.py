import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = r"C:\Users\moham_f78sqay\Downloads\sales_quarters.csv"

df = pd.read_csv(file)

print(df)



#1.df.plot ----> many values for one catogrie


df_com =df.set_index("Company")
df_com.index.name = None
print(df_com)
df_t=df_com.transpose()


df_t.plot(kind="bar")
plt.xlabel("company")
plt.ylabel("sales")
plt.show()

#2.plt -----> one value for one catogrie

plt.bar(df["Company"],df["Q1"],color="red",label = "Q1")
plt.bar(df["Company"],df["Q2"],color="blue",label = "Q2")
plt.bar(df["Company"],df["Q3"],color="orange",label = "Q3")
plt.bar(df["Company"],df["Q4"],color="purple",label = "Q4")
plt.tight_layout()

plt.xlabel("Company")
plt.ylabel("Sales")
plt.title("Sales by Company Across Years")
plt.legend()
plt.show()

#3. stacked plt --- > layers on each of them

df_com["total"] = df_com.sum(axis=1)
print(df_com)
df_com.plot(kind="bar",stacked=True)
plt.xlabel("company")
plt.ylabel("sales")
plt.show()

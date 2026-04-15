
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path = r"C:\Users\moham_f78sqay\Downloads\products.csv"
df = pd.read_csv(path)
print(df)
print("_"*50)
print(df.describe())
print("_"*50)
print(df["Category"].value_counts())

plt.boxplot(df["Price"])
plt.title("price distribution")
plt.xlabel("price")
#plt.show()


sns.boxplot(y=df["Price"])
plt.title("price distrubution")
#plt.show()


plt.scatter(df["Quantity_Sold"],df["Price"],color="red")
plt.title("relation between price and Quantity")
plt.xlabel("quantity")
plt.ylabel("price")
plt.show()
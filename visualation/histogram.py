import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

#x-axis --> data 
#y_axis ---> frequancy(by defult)

file = r"C:\Users\moham_f78sqay\Downloads\sales_data (1).csv"
df = pd.read_csv(file)
print(df)
df.set_index("Company",inplace=True)
print(df)


#1.plt.hist 
plt.hist(df["2020"],bins=20,edgecolor="black")
plt.show()

#2.plt.hist + np.histogram(data )
count,bins1 = np.histogram(df["2020"],bins=40)
#count--> the highet
#bins --> the lengh
plt.hist(bins1[:-1],bins=bins1,weights=count,edgecolor = "black")
plt.show()

#3.plt + nb.lenspace()
bins2 = np.linspace(df["2020"].min(),df["2020"].max(),10)
plt.hist(df["2020"],bins=bins2,color = "green",edgecolor = "black",alpha = .6)
plt.show()


#data.plt
df["2020"].plot(kind="hist",bins = 20)
plt.show()


#5.seaborn
bins3 = np.linspace(df["2020"].min(),df["2020"].max(),10)
sns.histplot(data=df["2020"],bins=bins3,kde=True)
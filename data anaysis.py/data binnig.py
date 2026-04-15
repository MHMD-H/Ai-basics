# Binning is a data preprocessing method where continuous numerical values are grouped into intervals (bins). This helps simplify data, reduce noise, and sometimes improve the accuracy of predictive models.

# Example:

# Instead of having many unique values of "price" (e.g., 201 unique values from 5,188 to 45,400), we can divide them into 3 bins:

# Low price

# Medium price

# High price

# Steps in Python:

# Use NumPy linspace to create evenly spaced intervals (bin edges).

# Define bin labels (e.g., ["Low", "Medium", "High"]).

# Use Pandas cut to categorize the data into bins.

# Optionally, use histograms to visualize the distribution.

# Result: You reduce complexity, and the visualization shows that most cars fall in the low-price bin, while few are in the high-price bin.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = r"C:\Users\moham_f78sqay\Downloads\sample_age.csv"
df = pd.read_csv(path)
print(df)

#Use NumPy linspace --> to create bin edges np.linspace(df["column"].min(),df["column"].max,interval+1)
bins = np.linspace(df["Age"].min(),df["Age"].max(),5)

#bins can be manualed -->[intr1,intr2,intr3,intr4,df["column"].max]
bins1 = [0,7,18,30,df["Age"].max()]
## Define bin labels --> interval's name = [list of names]
interval_name = ["child","teenger","young","old"]

#Use Pandas cut to categorize the data into bins.--> df["new column"] = pd.cut(df["column"],bins,label = label name,include_lowest = True)
df["range Age"] = pd.cut(df["Age"],bins1,labels=interval_name,include_lowest=True)
print(df)
plt.hist(df["Age"],bins)

plt.xlabel("Age")
plt.ylabel("range")
plt.show()

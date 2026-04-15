import pandas as pd
import numpy as np
path = r"C:\Users\moham_f78sqay\Downloads\sample_data.csv"
df = pd.read_csv(path)
print(df)

print("_"*50)
#normalization between 0,1
#1.Simple Feature Scaling ---> value/ max value
df["Age"] = round(df["Age"]/df["Age"].max(),2)
df["Income"] = round(df["Income"]/df["Income"].max(),2)
print(df)
print("_"*50)

#2.Min-Max Normalization  --> (value-min) / (value-max)
df["Length"] = round((df["Length"]-df["Length"].min())/(df["Length"].max() -df["Length"].min()),2)
df["Width"] = round((df["Width"]-df["Width"].min())/(df["Width"].max() -df["Width"].min()),2)
print(df)
print("_"*50)

#normalivation about  +,-
#Z-Score --> (value - mean value / std value)
df["Height"] = round((df["Height"] - df["Height"].mean())/df["Height"].std(),2)
print(df)
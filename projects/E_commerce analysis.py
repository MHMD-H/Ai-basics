import pandas as pd

file = r"C:\Users\moham_f78sqay\Downloads\sales_data.csv"
df=pd.read_csv(file)
print(df)
print(df.columns.isnull())
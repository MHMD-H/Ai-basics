import pandas as pd
import numpy as np
import random
# Dealing with Missing Data 

# Definition: A missing value occurs when no data is recorded for a feature in a dataset
#  (often shown as NaN, N/A, ?, 0, or a blank cell).

# Ways to Handle Missing Data:

# Recover the data → Ask the data collector to fill in the missing values if possible.

# Remove the data : 

# Drop the whole variable (column).axis=1

# Drop only the affected observation (row).axis=0

# Best if only a small number of records are missing.
#___________________________________________________________________________
# Replace (Impute) the data :

# Numeric values: Replace with the mean (or sometimes median). 

# Categorical values: Replace with the mode (most common value).

# Smarter guesses: Use additional knowledge (e.g., older cars may have higher losses).
#____________________________________________________________________________________
#Leave missing as missing → Sometimes useful for analysis.

path = r"C:\Users\moham_f78sqay\Desktop\missing_data_example.csv"
fl = pd.read_csv(path)
missing_data = fl.isnull() #values = NAN

print(missing_data)
print(fl)
print('-' *50)

print('-' *50)
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

print(fl.dropna(subset=["Name"],axis=0,)) #inplace  False --> edit on original file\#inplace = True --> Make a copy
# print(fl)
print('-' *50)


mean_data = fl["Age"].mean()

fl["Age"].replace(np.nan,round(mean_data),inplace=True)
fl["Name"].replace(np.nan,random.choice(fl["Name"]),inplace=True)
print(fl)
print('-' *50)
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

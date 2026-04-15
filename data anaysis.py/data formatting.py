import pandas as pd

# Why formatting is needed:

# Data often comes from different sources → with different formats, units, and conventions.

# Formatting means standardizing the data so it’s consistent and comparable.

# Example: “New York” might appear as NY, N.Y., Ny, New York.

# Sometimes variety is useful (e.g., fraud detection).

# But usually, we want to unify them into one format for analysis.

# Example – Unit conversion:

# Dataset column: city-miles per gallon (mpg).

# In metric systems, fuel efficiency is expressed as liters per 100 km.

path = r"C:\Users\moham_f78sqay\Downloads\data_formatting_example.csv"
df = pd.read_csv(path)
print(df)
print("_"*50)

#convert from MPG --> l/km
df["City-MPG"] = 235/df["City-MPG"]

#rename the column name --> rename(columns = {old name : new name})
df.rename(columns={"City-MPG" : "L/km"},inplace=True)
print(df)

print("_"*50)
#formatting dataset
df["City"] = "New York"
print(df)
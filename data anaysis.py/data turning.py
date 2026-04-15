import pandas as pd

# بيانات مثال
data = {
    "Car": ["A", "B", "C", "D", "E"],
    "Fuel": ["gas", "diesel", "gas", "diesel", "gas"],
    "Color": ["red", "blue", "green", "blue", "red"],
    "Mileage": [10000, 20000, 15000, 30000, 12000]
}

df = pd.DataFrame(data)
print("البيانات الأصلية:")
print(df)
print("_"*50)

# تطبيق One Hot Encoding على الأعمدة التصنيفية
df_encoded = pd.get_dummies(df, columns=["Fuel", "Color"], drop_first=True)
print("بعد تطبيق One Hot Encoding مع drop_first=True:")
df_encoded["Fuel_gas"] = df_encoded["Fuel_gas"].astype("int")
print(df_encoded)

import numpy as np 
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

# Load dataset
file_LR = r"C:\Users\moham_f78sqay\Downloads\experience_salary.csv"
df = pd.read_csv(file_LR)
print(df.head())

# Features and target
x = df[["Experience"]]
y = df["Salary"]

# Split data: 60% train, 20% CV, 20% test
x_train, x_temp, y_train, y_temp = train_test_split(x, y, test_size=0.4, random_state=42)
x_cv, x_test, y_cv, y_test = train_test_split(x_temp, y_temp, test_size=0.5, random_state=42)

degrees = range(1, 5)
model_select = []
cv_mse_select = []

# Train on training set and evaluate on CV set
for d in degrees:
    poly = PolynomialFeatures(degree=d, include_bias=False)
    x_train_poly = poly.fit_transform(x_train)
    x_cv_poly = poly.transform(x_cv)
    
    model = LinearRegression()
    model.fit(x_train_poly, y_train)
    
    y_cv_pred = model.predict(x_cv_poly)
    mse_cv = mean_squared_error(y_cv, y_cv_pred)
    
    model_select.append((model, poly))
    cv_mse_select.append(mse_cv)
    
    print(f"MSE on CV set for degree {d}: {mse_cv}")

# Select the best model based on CV MSE
best_idx = np.argmin(cv_mse_select)
best_degree = degrees[best_idx]
best_model, best_poly = model_select[best_idx]

print(f"\nBest degree based on CV: {best_degree}")

# Evaluate the best model on test set
x_test_poly = best_poly.transform(x_test)
y_test_pred = best_model.predict(x_test_poly)
mse_test = mean_squared_error(y_test, y_test_pred)

print(f"MSE on Test set: {mse_test}")

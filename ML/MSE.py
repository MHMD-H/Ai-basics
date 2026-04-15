# 🎯 Mean Squared Error (MSE)

# Purpose: Measures the average size of errors between actual and predicted values.

# Interpretation: The smaller the MSE, the closer the predictions are to the real values.

# Python module:
from sklearn.metrics import mean_squared_error


# 🎯 Coefficient of Determination (R²)

# Purpose: Measures how much of the variance in the data is explained by the model compared to using just the mean.

# Values:

# 1 → Perfect fit.

# 0 → Same as just using the mean.

# Negative → Likely due to overfitting or a bad model.

# Python module:
from sklearn.metrics  import r2_score

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Experience": [1, 2, 3, 4, 5, 6],
    "Salary": [2500, 3000, 3500, 4000, 4500, 5000]
}
df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

# تدريب نموذج انحدار خطي
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

MSE = mean_squared_error(y,y_pred)
print(MSE)
print(y_pred)


R_2 = model.score(X,y)



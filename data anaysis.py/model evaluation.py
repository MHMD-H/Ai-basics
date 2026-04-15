# 1) Purpose of Model Evaluation

# Training data: used to build the model (learn the relationships).

# Test data: used to measure the model’s ability to generalize to new, unseen data.

# Problem: A single Train/Test split can give unstable results depending on how the sample is divided.

# Solution: Cross-validation → splits the data into K-folds and repeats training + testing multiple times.

# 2) Key Tools in Scikit-learn

# train_test_split → performs a single train/test split.

# cross_val_score → evaluates the model multiple times and returns evaluation metrics (e.g., R², MSE).

# cross_val_predict → returns the actual predictions for each sample after performing cross-validation.

# 3) Difference Between SLR and MLR

# SLR (Simple Linear Regression): one independent variable (X → y).

# MLR (Multiple Linear Regression): multiple independent variables (X1, X2, … → y).

# Relation to MSE: MLR or Polynomial Regression usually lowers the MSE compared to SLR because they capture more information → but beware of overfitting.

# 4) Scoring

# scoring="r2" → means the evaluation metric is the coefficient of determination (R²).

# You can also use:

# "neg_mean_squared_error"

# "neg_mean_absolute_error"

# and others depending on what you want to measure.


import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split,cross_val_predict,cross_val_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "engine_size": [1000, 1600, 2000, 2400, 3000, 3500, 4000, 4500, 5000, 5500],
    "horsepower": [70, 110, 150, 180, 220, 250, 280, 300, 330, 360],
    "doors": [4, 4, 2, 4, 4, 2, 2, 4, 2, 4],
    "price": [8000, 12000, 15000, 18000, 22000, 26000, 30000, 34000, 38000, 42000]
}
df = pd.DataFrame(data)
print(df)

#linear regression
model = LinearRegression()

#select data 
x=df[["engine_size"]]
y=df["price"]


#train and test faatures & target
x_train,x_test , y_train,y_test=train_test_split(x,y,test_size=.3,random_state=0) #train_test_split(feature,target,test_size=size,random_state=0) 

#train model & prediction
model.fit(x_train,y_train)
y_predicted = model.predict(x_test)

for i in y_predicted :
    print(f"The predicted data is {i:.2f} \n")

#evaluate data  
MSE = mean_squared_error(y_test,y_predicted)
print(f"the MSE is {MSE}")

R = model.score(x_test,y_test)
print(f"the R^2 is {R}")

residual = y_test - y_predicted



#Cross valid score
score = cross_val_score(model,x,y,cv=5,scoring="r2")#cross_val_score(model name,features,target,cv=5(1 test : 4 train),scoring="method to measure")
print(f"The R score is {score}")
print(f"The mean  R score is {np.mean(score)}")

#cross valid predict
y_pred = cross_val_predict(model,x,y,cv = 5)
print(f"the predicted data is {y_pred}")

sns.residplot(x=y_predicted,y=residual)
plt.show()

#sns.scatterplot(x=y,y=y_test)
sns.regplot(x=x_test,y=y_test)
plt.show()

sns.kdeplot(x_train,color="red",label ="train data")
sns.kdeplot(x_test,color="blue",label ="test data")
plt.legend()
plt.show()

sns.kdeplot(y_test,color="red",label ="target data")
sns.kdeplot(y_predicted,color="blue",label ="predicted data")
plt.legend()
plt.show()

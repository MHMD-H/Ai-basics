import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge,Lasso
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error , mean_squared_error,r2_score

data = {
    "Hours": [1,2,3,4,5,6,7,8,9,10],
    "Score": [52,56,61,65,71,76,79,84,88,93]
}

df = pd.DataFrame(data)

def evaluation(y_true,y_predict,model):
    r2 = r2_score(y_true,y_predict)
    mse = mean_squared_error(y_true,y_predict)
    mae =mean_absolute_error(y_true,y_predict)

#chooose data
x = df[["Hours"]] #2D
y = df["Score"]


#create model
model_reg = LinearRegression()
model_ridge = Ridge(alpha=.1)
model_lasso = Lasso(alpha=.1)


#train 
model_reg.fit(x,y)
model_ridge.fit(x,y)
model_lasso.fit(x,y)

#print perameters
print(f"intercept(b0) = {model_reg.intercept_} \n slope(b1) = {model_reg.coef_}")

#make predict
y_pred_reg= model_reg.predict(x)
y_pred_ridg= model_ridge.predict(x)
y_pred_lass= model_lasso.predict(x)


for c,i in zip(df["Hours"].values,y_pred_reg) :
    print(f"the predicted score for {c} is : {i:.2f} \n")

risudal = y - y_pred_reg 
sns.regplot(x=x , y=y ,color="red")
plt.show()

sns.residplot(x=y_pred_reg , y=risudal)
plt.show()

# Distribution Plot
plt.figure(figsize=(8,5))
sns.kdeplot(y, color="red", label="Actual Data")
sns.kdeplot(y_pred_reg, color="blue", label="Fitted Data")
plt.legend()
plt.show()

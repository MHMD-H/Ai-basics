import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours": [1,2,3,4,5,6,7,8,9,10],
    "Score": [52,56,61,65,71,76,79,84,88,93]
}

df = pd.DataFrame(data)


#chooose data
x = df[["Hours"]] #2D
y = df["Score"]


#create model
model = LinearRegression()

#train model
model.fit(x,y)

#print perameters
print(f"intercept(b0) = {model.intercept_} \n slope(b1) = {model.coef_}")

#make predict
y_pred = model.predict(x)
for c,i in zip(df["Hours"].values,y_pred) :
    print(f"the predicted score for {c} is : {i:.2f} \n")

risudal = y - y_pred 
sns.regplot(x=x , y=y ,color="red")
plt.show()

sns.residplot(x=y_pred , y=risudal)
plt.show()

# Distribution Plot
plt.figure(figsize=(8,5))
sns.kdeplot(y, color="red", label="Actual Data")
sns.kdeplot(y_pred, color="blue", label="Fitted Data")
plt.legend()
plt.show()

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split,cross_val_predict,cross_val_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\moham_f78sqay\Downloads\experience_salary.csv"
df = pd.read_csv(path)
print(df)
print("_"*50)

x = df[["Experience"]]
y=df["Salary"]


#1.test_train method :

#split data to test,train:
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.3,random_state=0)

#select best degree :
r2_1 =[]

degrees =range(1,10)
for d in degrees :
    poly = PolynomialFeatures(degree=d) 
    x_train_poly = poly.fit_transform(x_train) #transform x train to polynomial 
    x_test_poly = poly.fit_transform(x_test) ##transform x test to polynomial 

    norm = StandardScaler()
    x_train_poly_norm = norm.fit_transform(x_train_poly)#normalization
    x_test_poly_norm = norm.fit_transform(x_test_poly)

    model = LinearRegression()
    model.fit(x_train_poly_norm,y_train) #train the model
    y_pred_1 = model.predict(x_test_poly_norm) #make prediction
    R_1 = r2_score(y_test,y_pred_1) #calculate the R^2
    r2_1.append(R_1)



    print(f"The R^2 score to {d} degree is : {R_1} \n")
best_degree1 = degrees[np.argmax(r2_1)] #select the best degree
print(f"The best degree is {best_degree1} ")

#plot 
plt.plot(degrees,r2_1)
plt.show()
#__________________________________________________________________________________________________

#2.cross validation
r2_2 =[]

degrees =range(1,10)
for d in degrees :
    poly = PolynomialFeatures(degree=d) 
    x_poly = poly.fit_transform(x) #transform x  to polynomial 
    
    norm = StandardScaler()
    x_poly_norm = norm.fit_transform(x_poly)#normalization

    model = LinearRegression()
    scores = cross_val_score(model,x_poly_norm,y,cv=4,scoring="r2")
    r2_2.append(scores.mean())
    print(f"The R^2 score to {d} degree is : {scores.mean()} \n")
best_degree2 = degrees[np.argmax(r2_2)] #select the best degree
print(f"The best degree is {best_degree2} ")
plt.plot(degrees,r2_2)
plt.show()

#compare between methods 
if best_degree1 == best_degree2 :
    print("The two methods is work")



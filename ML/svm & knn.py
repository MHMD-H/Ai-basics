import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier

link = r"https://huggingface.co/datasets/scikit-learn/breast-cancer-wisconsin/resolve/main/breast_cancer.csv"

df = pd.read_csv(link)
print(df)

missing_data = df.isna()
for column in missing_data.columns.values.tolist():
    print(missing_data[column].value_counts())
    print(" ")

df = df.drop("Unnamed: 32",axis=1)
lb = LabelEncoder()
df["diagnosis_encoder"] = lb.fit_transform(df["diagnosis"])
print(df)


column_count = df["diagnosis"].value_counts()
print(column_count)
color = ["red","blue"]

plt.pie(column_count,colors = color,shadow = True,pctdistance=1.12,startangle=90,autopct='%1.1f%%')
plt.legend(labels=df["diagnosis"], loc='upper left', fontsize=7)
plt.show()


x = df.drop(["diagnosis","diagnosis_encoder"],axis = 1)
y = df["diagnosis"]

std = StandardScaler()
x_norm = std.fit_transform(x)
x_train,x_,y_train,y_ = train_test_split(x,y,test_size=.4,random_state=42)
x_test,x_grid,y_test,y_grid = train_test_split(x_,y_,test_size=.5,random_state=42)

#SVM model 
svm = LinearSVC(class_weight="balanced")
svm.fit(x_train,y_train)
svm_predicted = svm.predict(x_test)
svm_accu = accuracy_score(y_test,svm_predicted)
print(f"the acuuracy of SVM model is{svm_accu}")


#knn model

ks =10
km = np.zeros(ks)
for k in range(1,10) :
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    kn_grid = knn.predict(x_grid)
    knn_acc = accuracy_score(y_grid,kn_grid)
    km[k-1] = knn_acc
best_k=km.argmax()+1
best_kaccu=km.max()


print(f"the acuuracy of best knn testing model is{best_kaccu}")
print(f"the k is : {best_k}")


knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(x_train,y_train)
kn_pred = knn.predict(x_test)
knn_acc1 = accuracy_score(y_test,kn_pred)
print(f"the acuuracy of best knn model is{knn_acc1}")

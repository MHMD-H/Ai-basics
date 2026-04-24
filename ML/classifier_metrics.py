import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.tree import ExtraTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score , classification_report

path= 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv'
my_data = pd.read_csv(path)
print(my_data)

columns=["BP","Cholesterol","Sex"]
encode = LabelEncoder()
for column in columns :

    my_data[column]=encode.fit_transform(my_data[column])

my_data["drug_num"] = encode.fit_transform(my_data["Drug"])
print(my_data.drop("Drug",axis=1).corr())
print(my_data)
x = my_data.drop(["Drug","drug_num"],axis=1)
y = my_data["Drug"]
x_train,x_,y_train,y_ = train_test_split(x,y,test_size=.4,random_state=42)

x_test,x_grid,y_test,y_grid = train_test_split(x_,y_,test_size=.5,random_state=42)

min_sample = [2,5,10,15,6]
sample_accu = []
models = []

for s in min_sample:
    tree = ExtraTreeClassifier(min_samples_split=s, random_state=42)
    tree.fit(x_train,y_train)

    y_grid_pred = tree.predict(x_grid)
    acc = accuracy_score(y_grid,y_grid_pred)

    sample_accu.append(acc)
    models.append(tree)

best_index = np.argmax(sample_accu)
best_sample = min_sample[best_index]

print("best min_samples_split =", best_sample)

# تجربة max_depth
max_depth = [1,2,3,4,5]
depth_acc = []
depth_models = []

for d in max_depth:
    tree = ExtraTreeClassifier(
        max_depth=d,
        min_samples_split=best_sample,
        random_state=42
    )

    tree.fit(x_train,y_train)

    y_grid_pred = tree.predict(x_grid)
    acc = accuracy_score(y_grid,y_grid_pred)

    depth_acc.append(acc)
    depth_models.append(tree)

best_index = np.argmax(depth_acc)
best_depth = max_depth[best_index]

print("best max_depth =", best_depth)

best_model = depth_models[best_index]

# اختبار النهائي
y_pred = best_model.predict(x_test)

print("Test Accuracy:", accuracy_score(y_test,y_pred))

report = classification_report(y_test,y_pred)
print(report)
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.tree import ExtraTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# load data
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv'
df = pd.read_csv(path)

# preprocessing
df = pd.get_dummies(df, columns=["Sex","BP","Cholesterol"])

le = LabelEncoder()
y = le.fit_transform(df["Drug"])
X = df.drop("Drug", axis=1)

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("tree", ExtraTreeClassifier())
])

# params
params = {
    "tree__max_depth": [4,5,6,7],
    "tree__min_samples_split": [3,4,5]
}

# CV
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# grid search
grid = GridSearchCV(pipe, param_grid=params, cv=cv, scoring="f1_macro")

grid.fit(X_train, y_train)

best_model = grid.best_estimator_

# test
y_pred = best_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Best Params:", grid.best_params_)
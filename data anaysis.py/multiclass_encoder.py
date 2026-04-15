# مثال dataset صغير
y = ["healthy", "sick", "recovered", "healthy", "sick"]

# ===== 1. Label Encoding =====used for big dta samples

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y_label_encoded = le.fit_transform(y)
print("Label Encoded:", y_label_encoded)
# الناتج: [0 1 2 0 1]

# ===== 2. One-Hot Encoding ===== used for vector repesntaation
from keras.utils import to_categorical

y_onehot = to_categorical(y_label_encoded)
print("One-Hot Encoded:\n", y_onehot)
# الناتج:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]
#  [0. 1. 0.]]

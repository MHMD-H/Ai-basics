# Correlation --> measures how two variables are related (interdependent).

# Example: Smoking ↔ Lung cancer (positive correlation).

# Example: Rain ↔ Umbrella (correlated, but not causal).

# Correlation ≠ Causation(السبب): Just because two things move together doesn’t mean one causes the other.

# Scatter plot + regression line:

# Engine size ↑ → Price ↑ (positive correlation). --> near to +-1

# Highway MPG ↑ → Price ↓ (negative correlation).---> far from +-1

# RPM ↔ Price (weak correlation, no clear relation).

# Pearson Correlation:

# Outputs correlation coefficient (r) and p-value.

# r close to +1 → strong positive correlation.

# r close to -1 → strong negative correlation.

# r close to 0 → no correlation.

# p-value tells us certainty:

# <0.001 → strong certainty.

# 0.001–0.05 → moderate certainty.

# 0.05–0.1 → weak certainty.

# 0.1 → no certainty.

# Example: Horsepower vs Price → r ≈ 0.8 (strong positive), p-value < 0.001 (high certainty).

# Heatmap:

# Shows correlations between many variables.

# Diagonal is always 1 (a variable with itself).

# Helps identify which variables are strongly related to Price.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats as st

# البيانات
data = {
    "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Advertising": [2000, 2500, 1800, 3000, 2200, 2700, 2600, 2300, 2400, 2800],
    "Price": [50, 48, 52, 47, 49, 46, 45, 48, 47, 44],
    "Units_Sold": [300, 320, 280, 350, 310, 360, 370, 330, 340, 380],
    "Customer_Satisfaction": [4.2, 4.5, 4.0, 4.7, 4.3, 4.6, 4.8, 4.4, 4.5, 4.9]
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)
print(df)
print('_'*50)

# 1) Scatter plot مع خط الانحدار بين Advertising و Price
sns.regplot(x="Advertising", y="Price", data=df)
plt.title("Relation between Advertising & Price")
plt.xlabel("Advertising Budget")
plt.ylabel("Price")
plt.show()

# 2) حساب معامل الارتباط بيرسون و p-value
corr_coff, p = st.pearsonr(df["Advertising"], df["Price"])
print(f"Correlation coefficient: {round(corr_coff, 2)}")
print(f"P-value: {p:.5f}")

# تفسير قوة الارتباط
if abs(corr_coff) >= 0.5:
    print("Strong correlation")
elif abs(corr_coff) == 0:
    print("No correlation")
else:
    print("Weak correlation")

# تفسير قيمة الاحتمال p-value
if p < 0.001:
    print("Strong certainty")
elif 0.001 <= p < 0.05:
    print("Moderate certainty")
elif 0.05 <= p < 0.1:
    print("Weak certainty")
else:
    print("No certainty")

# 3) رسم heatmap لكل الارتباطات في المتغيرين
sns.heatmap(df[["Advertising", "Price"]].corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

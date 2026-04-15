import numpy as np
import pandas as pd
import plotly.express as px  # ✅ مش ex
import matplotlib.pyplot as plt
# تحميل الملف
file = r"c:\Users\moham_f78sqay\Downloads\sales.csv"
df = pd.read_csv(file)
print(df.head())

# ----------------------------------------------------
# 1️⃣ Treemap visualization
# ----------------------------------------------------

# بنستخدم plotly.express.treemap
fig = px.treemap(
    df,
    path=['Region', 'Country'],   # المستويات (المنطقة ← الدولة)
    values='Sales',               # القيم اللي تتعرض في المربعات
    color='Profit',               # (اختياري) يلون حسب الأرباح
    title='Sales and Profit by Region and Country'
)
fig.show()

# ----------------------------------------------------
# 2️⃣ Pivot Table
# ----------------------------------------------------

# بنجّمع القيم لكل منطقة ودولة
df_group = df.groupby(["Region", "Country"]).sum(numeric_only=True).reset_index()
print(df_group)

# بنحوّل الجدول لـ pivot عشان نشوف توزيع المبيعات حسب المنطقة والدولة
piv = df_group.pivot(index="Region", columns="Country", values="Sales",#aggfunc=np.sum
)
print(piv)
piv.plot(kind='bar', figsize=(8,5))
plt.title('Quarterly Sales by Category')
plt.xlabel('Quarter')
plt.ylabel('Total Sales')
plt.grid(False)
plt.show()
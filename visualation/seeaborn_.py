import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# تحميل البيانات الجاهزة
data = sns.load_dataset("tips")

# عرض أول 5 صفوف
print(data.head())

# 1. رسم علاقة بين total_bill و tip
sns.regplot(x="total_bill", y="tip", marker="+", data=data)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Relationship between Total Bill and Tip")
plt.show()

# 2. Bar Plot
sns.barplot(x="day", y="tip", data=data)
plt.xlabel("Day")
plt.ylabel("Tip")
plt.title("Average Tip by Day")
plt.show()

# 3. Count Plot
sns.countplot(x="day", data=data)
plt.title("Count of Customers by Day")
plt.show()

# 4. Box Plot
sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Total Bill Distribution by Day")
plt.show()

# 5. Heatmap
# الخطأ كان هنا 👇
# لازم نستخدم data.select_dtypes(include=["int", "float"])
df = data.select_dtypes(include=["int", "float"])

# وبعدين نحسب الارتباط
corr = df.corr()

# الخطأ التاني: 'colormap' المفروض تبقى 'cmap' واسم الخريطة 'coolwarm'
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

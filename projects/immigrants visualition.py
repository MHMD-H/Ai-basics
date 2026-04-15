import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ قراءة البيانات
file = r"C:\Users\moham_f78sqay\Downloads\immigrants.csv"
df = pd.read_csv(file)
print(df.head())

# 2️⃣ تحديد الأعمدة
x = df["Year"]
y = df["CountryA"]

# 3️⃣ إنشاء الشكل - 3 رسومات جنب بعض
fig, ax = plt.subplots(1, 3, sharey=True, figsize=(15, 5))

# 🎨 ألوان متناسقة
main_color = "navy"
accent_color = "red"

# 4️⃣ Line Plot
ax[0].plot(x, y, linestyle="--", marker="s", markersize=5, color=main_color)
ax[0].set_title("Line Plot", fontsize=12, fontweight='bold')
ax[0].set_xlabel("Years")
ax[0].set_ylabel("Immigrants")
ax[0].grid(True, linestyle="--", alpha=0.6)

# 5️⃣ Scatter Plot
ax[1].scatter(x, y, marker="x", color=accent_color)
ax[1].set_title("Scatter Plot", fontsize=12, fontweight='bold')
ax[1].set_xlabel("Years")
ax[1].grid(True, linestyle="--", alpha=0.6)

# 6️⃣ Bar Plot
ax[2].bar(x, y, color="skyblue",width=2, edgecolor="black")
ax[2].set_title("Bar Plot", fontsize=12, fontweight='bold')
ax[2].set_xlabel("Years")
ax[2].grid(True, linestyle="--", alpha=0.6)

# 7️⃣ ضبط الشكل العام
fig.suptitle("Immigrants Distribution Across Years", fontsize=14, fontweight='bold', color="darkblue")
plt.tight_layout(rect=[0, 0, 1, 0.95])  # يزبط المسافات بين الرسومات والعنوان
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# | البراميتر           | الشرح                                                            | مثال عملي                                    |
# | ------------------- | ---------------------------------------------------------------- | -------------------------------------------- |
# | **`x` / `y`**       | الأعمدة أو القيم اللي هترسمها (لو بتستخدم `df.plot(kind="pie")`) | `df.plot(kind="pie", y="Sales")`             |
# | **`labels`**        | أسماء الشرائح (لو مش محددة من الأعمدة)                           | `plt.pie(values, labels=["A","B","C"])`      |
# | **`autopct`**       | تنسيق النسبة المئوية اللي بتظهر على كل شريحة                     | `autopct='%1.1f%%'` ⟶ يظهر 1 رقم عشري        |
# | **`startangle`**    | الزاوية اللي يبدأ منها الرسم (افتراضي 0°)                        | `startangle=90` ⟶ يبدأ من الأعلى             |
# | **`explode`**       | يبعد شريحة أو أكثر عن المركز علشان تبرزها                        | `explode=[0, 0.1, 0]` ⟶ يبعد الشريحة التانية |
# | **`colors`**        | تحدد ألوان الشرائح يدويًا                                        | `colors=['red','blue','green']`              |
# | **`shadow`**        | تضيف ظل خفيف للرسم                                               | `shadow=True`                                |
# | **`pctdistance`**   | تتحكم في مكان النسبة داخل أو خارج الشريحة                        | `pctdistance=0.85`                           |
# | **`labeldistance`** | تتحكم في مكان اللابل (اسم الشريحة)                               | `labeldistance=1.1`                          |
# | **`counterclock`**  | ترسم عكس عقارب الساعة (True افتراضيًا)                           | `counterclock=False`                         |
# | **`figsize`**       | حجم الشكل العام (لو بتستخدم `df.plot`)                           | `figsize=(6,6)`                              |


#y---> data that you want to accsses on it
file = r"C:\Users\moham_f78sqay\Downloads\sales_quarters.csv"

df = pd.read_csv(file)

print(df)

x=df["Company"] #labels
y= df.drop(["Company"],axis=1).sum(axis=1) #data in percentage
print(y)
colors_list = ['gold', 'yellowgreen', 'lightcoral']
explode_list = [0.1, 0, 0.1] 

plt.pie(y,colors = colors_list,explode=explode_list,shadow = True,pctdistance=1.12,startangle=90,autopct='%1.1f%%')
plt.legend(labels=x, loc='upper left', fontsize=7)
plt.show()




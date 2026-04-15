import pandas as pd
import numpy as np

# reproducibility
np.random.seed(42)

# عدد الصفوف
n = 200

# توليد البيانات
experience = np.random.randint(0, 30, n)
age = experience + np.random.randint(22, 35, n)
salary = 3000 + experience * 700 + age * 50 + np.random.randint(-2000, 2000, n)
gender = np.random.choice(["Male", "Female"], n)
hours_worked = np.random.randint(30, 60, n)
department = np.random.choice(["IT", "HR", "Finance", "Marketing", "Sales"], n)

# إنشاء DataFrame
df = pd.DataFrame({
    "Experience": experience,
    "Salary": salary,
    "Age": age,
    "Gender": gender,
    "Hours_Worked": hours_worked,
    "Department": department
})

# حفظ الملف CSV
df.to_csv("employee_data.csv", index=False)

print("تم إنشاء الملف: employee_data.csv")

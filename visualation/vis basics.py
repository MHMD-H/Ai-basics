# استيراد المكتبات المطلوبة
import pandas as pd 
import matplotlib.pyplot as plt
from pywaffle import Waffle  # مكتبة رسم مخططات الوافل

# تحديد مسار ملف البيانات
path = r"C:\Users\moham_f78sqay\Downloads\language_popularity.csv"

# قراءة البيانات من ملف CSV
df = pd.read_csv(path)

# إنشاء الشكل الرئيسي للمخطط
fig = plt.figure(
    FigureClass=Waffle,  # تحديد أن الشكل من نوع Waffle chart
    rows=15,             # عدد الصفوف في المخطط (عدد المربعات العمودية)
    
    # تحويل البيانات من أعمدة إلى قاموس {اللغة: النسبة}
    values=dict(zip(df["Language"], df["Popularity (%)"])),  
    
    # تحديد الألوان لكل لغة برمجية
    colors=["red","blue","green","black","navy","purple","grey","darkred","pink","brown"],
    
    # عنوان المخطط وموقعه
    title={"label": "The Languages Distribution", "loc": "center"},
    
    # إعدادات مفتاح الألوان (الليجند)
    legend={
        "loc": "lower left",          # مكان الليجند أسفل اليسار
        "bbox_to_anchor": (0, -0.4),  # المسافة بين الشكل والليجند
        "ncol": 3                     # عرض الليجند في 3 أعمدة
    },
    
    # # إعدادات الأيقونات بدل المربعات العادية
    # icons='code',         # نوع الأيقونة (من مكتبة Font Awesome)
    # icon_size=15,         # حجم الأيقونات داخل المخطط
    # icon_legend=True      # يربط الأيقونات بالليجند تلقائيًا
)

# عرض المخطط على الشاشة
plt.show()

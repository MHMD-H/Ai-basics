import requests
import time
import random

# رابط الفورم (formResponse مش viewform)
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc05MpbzTTbrLTpy33ivFhOnhvRW-jZRcIDkOb46nZTug13ww/formResponse"

# تعريف الحقول
FIELDS = {
    "وظيفة": "entry.699562254",   # تأكد إنه فعلاً للوظيفة
    "نوع": "entry.978923220",
    "خبرة": "entry.1811705237",
    "مرحلة": "entry.769408626",
    "مدرسة": "entry.509646506"
}

# الإعدادات المطلوبة
job = "مشرف نربوي"
gender = "أنثى"
school_type = "حكومي"
experience = ["أقل من 5 سنوات", "من 5 إلى 10 سنوات", "أكثر من 10 سنوات"]
stages = ["ابتدائي", "متوسط", "ثانوي"]
answers = ["محايد", "أوافق", "أوافق بشدة"]

# باقي الأسئلة (كلها نفس النطاق)
other_entries = [
    "entry.139434975","entry.664840918","entry.1990579364","entry.992367620",
    "entry.1352725299","entry.458709692","entry.1009577945","entry.167839004",
    "entry.503678952","entry.771696525","entry.1789039383","entry.860427136",
    "entry.460809185","entry.668641559","entry.1295221944","entry.1857046238",
    "entry.764308760","entry.82592161","entry.26333349","entry.536863600",
    "entry.100504974","entry.1251402408","entry.691635001","entry.1637138204",
    "entry.1989251072","entry.1409888465","entry.861863684","entry.166141687",
    "entry.1052735627","entry.1748845138","entry.899822291","entry.956814526",
    "entry.52243923","entry.925101461","entry.1121991267","entry.149111117",
    "entry.880903520","entry.1911972456","entry.625525601","entry.2005869500",
    "entry.656986889","entry.541138212","entry.570865666","entry.1908800287",
    "entry.929941530","entry.199500287","entry.1257948567"
]

# إرسال رد
def send_response():
    data = {
        FIELDS["وظيفة"]: job,
        FIELDS["نوع"]: gender,
        FIELDS["خبرة"]: random.choice(experience),
        FIELDS["مرحلة"]: random.choice(stages),
        FIELDS["مدرسة"]: school_type,
    }
    # باقي الأسئلة بنفس النطاق
    for e in other_entries:
        data[e] = random.choice(answers)

    res = requests.post(FORM_URL, data=data)
    return res.status_code

# تنفيذ 7 مرات
for i in range(1, 8):
    status = send_response()
    print(f"{i}- {job} -> {status}")
    time.sleep(2)  # استراحة لتفادي الحظر

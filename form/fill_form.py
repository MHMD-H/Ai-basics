import requests
import time
import random

# رابط الفورم (استخدم رابط formResponse بدل viewform)
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc05MpbzTTbrLTpy33ivFhOnhvRW-jZRcIDkOb46nZTug13ww/formResponse"

# تعريف الحقول المهمة
FIELDS = {
    "وظيفة": "entry.699562254",
    "نوع": "entry.978923220",
    "خبرة": "entry.1811705237",
    "مرحلة": "entry.769408626",
    "مدرسة": "entry.509646506"
}

# خيارات أساسية
وظائف = {
    "معلم": 6,
    "مشرف": 2,
    "وكيل": 1,
    "مدير": 1
}
النوع = "ذكر"
المدرسة = "أهلي"
الخبرة = ["أقل من 5 سنوات", "من 5 إلى 10 سنوات", "أكثر من 10 سنوات"]
المرحلة = ["ابتدائي", "متوسط", "ثانوي"]
الإجابات = ["لا أوافق بشدة", "لا أوافق", "محايد", "أوافق", "أوافق بشدة"]

# باقي الأسئلة (نفس الإجابة الافتراضية مثلاً "أوافق")
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

# إرسال رد واحد
def send_response(job):
    data = {
        FIELDS["وظيفة"]: job,
        FIELDS["نوع"]: النوع,
        FIELDS["خبرة"]: random.choice(الخبرة),
        FIELDS["مرحلة"]: random.choice(المرحلة),
        FIELDS["مدرسة"]: المدرسة,
    }
    # باقي الأسئلة
    for e in other_entries:
        data[e] = random.choice(الإجابات)

    res = requests.post(FORM_URL, data=data)
    return res.status_code

# تنفيذ
count = 1
for job, num in وظائف.items():
    for _ in range(num):
        status = send_response(job)
        print(f"{count}- {job} -> {status}")
        count += 1
        time.sleep(2)  # استراحة لتفادي الحظر

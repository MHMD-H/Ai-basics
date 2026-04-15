import requests
import re

# حط هنا رابط الـ viewform (مش formResponse)
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc05MpbzTTbrLTpy33ivFhOnhvRW-jZRcIDkOb46nZTug13ww/viewform"

# اجلب الـ HTML
resp = requests.get(FORM_URL)
html = resp.text

# دور على كل entry.xxx
entries = re.findall(r'entry\.\d+', html)
entries = list(dict.fromkeys(entries))  # إزالة التكرار مع الحفاظ على الترتيب

print("تم استخراج الـ entry IDs:")
for e in entries:
    print(e)
import requests
import re
from bs4 import BeautifulSoup

FORM_URL ="https://docs.google.com/forms/d/e/1FAIpQLSc05MpbzTTbrLTpy33ivFhOnhvRW-jZRcIDkOb46nZTug13ww/viewform"

html = resp.text

entries = list(dict.fromkeys(re.findall(r'entry\.\d+', html)))

for e in entries:
    idx = html.find(e)
    snippet = html[max(0, idx-500): idx+500]  # ناخد مقطع حوالين entry
    soup = BeautifulSoup(snippet, "lxml")
    text = " | ".join(t.strip() for t in soup.stripped_strings if len(t.strip()) > 1)
    print(f"{e} --> {text[:200]}")

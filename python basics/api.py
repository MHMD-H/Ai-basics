import requests
import json

# إدخال الإحداثيات
start_lat = input("Enter start latitude: ")
start_lon = input("Enter start longitude: ")
end_lat = input("Enter end latitude: ")
end_lon = input("Enter end longitude: ")

# مفتاح الـ API (تحصل عليه مجانًا من موقع Geoapify)
api_key = "31f55858d92f4950892f93a38d213380"

# رابط الطلب
url = f"https://api.geoapify.com/v1/routing?waypoints={start_lat},{start_lon}|{end_lat},{end_lon}&mode=drive&apiKey={api_key}"

# تنفيذ الطلب
response = requests.get(url)
data = response.json()

# عرض البيانات بشكل منظم
print(json.dumps(data, indent=4))

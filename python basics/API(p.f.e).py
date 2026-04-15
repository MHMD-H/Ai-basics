import urllib.request, urllib.parse
import ssl, json

api = "http://py4e-data.dr-chuck.net/opengeo?"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter address:  ")
    if len(address) < 1:
        break

    params = {'q': address}
    url = api + urllib.parse.urlencode(params)

    print("Retrieving", url)
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print("Retrieved", len(data), "characters")

    js = json.loads(data)
    plus_code = js["features"][0]["properties"]["plus_code"]
    print(plus_code) 
    print("Plus code:", plus_code)

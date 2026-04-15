import urllib.request,urllib.parse
import json,ssl

url = "https://api.geoapify.com/v1/mapmatching?"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("enter your addriss")
params ={}
params["apikey"]=address

furl = url + urllib.parse.urlencode(params)
data = urllib.request.urlopen(furl,context=ctx).read().decode()

js = json.loads(data)
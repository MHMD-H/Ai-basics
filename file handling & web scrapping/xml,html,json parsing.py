import xml.etree.ElementTree as ET
import urllib.parse,urllib.request

url = "https://www.w3schools.com/xml/simple.xml"

fhand = urllib.request.urlopen(url).read()
data =ET.fromstring(fhand)
informs =data.findall(".//food")
for inform in informs :
    print(inform.find("price").text)


from bs4 import BeautifulSoup
url = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic_link"

fhand = urllib.request.urlopen(url)
bs = BeautifulSoup(fhand,"html.parser")
tags = bs('a')
for tag in tags :
    tagg = tag.get("href",None)
    print(tagg)


import urllib.request
import json 

url = "https://jsonplaceholder.typicode.com/users"
response = urllib.request.urlopen(url)
fhand = response.read().decode("utf-8")
data = json.loads(fhand)
for d in data:
    print(d["name"])

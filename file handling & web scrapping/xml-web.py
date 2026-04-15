import urllib.request,urllib.error,urllib.parse
import xml.etree.ElementTree as ES

inp = input("enter : ")
data = urllib.request.urlopen(inp).read() #TO read the link 

form = ES.fromstring(data)
comments = form.findall(".//comment")

sum = 0
count = 0
for comment in comments :
    num = comment.find('count').text
    num = int(num)
    sum = num + sum
    count = count +1
print("sum=",sum)
print("count = ",count)

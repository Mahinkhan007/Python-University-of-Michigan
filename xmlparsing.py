
import urllib.request
import urllib.response
import urllib.error

import xml.etree.ElementTree as ET

url = input("Enter the url")

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2155932.xml'
    
    
print("Retrieving url,", url )    
x = urllib.request.urlopen(url)
data = x.read()

    
print("Retrieving number of characters:", len(data))

et = ET.fromstring(data)

counts = et.findall('.//count')
nums = list()

for results in counts:
    print(results.text)
    nums.append(int(results.text))
    
    
print("Counts:", len(nums))
print("Sum:", sum(nums))



import urllib.request , urllib.error , urllib.parse
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


count= 0
sum =0
url = input("Enter - url: ")
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')
for span in spans:
    print("Contents:", span.contents[0])
    count += 1
    sum = sum + int(span.contents[0])
    
    
print("Sum:", sum)    
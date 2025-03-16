import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read() #read converts everything to a single string with next lines

soup = BeautifulSoup(html, 'html.parser')


#Retrive all a tags

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    


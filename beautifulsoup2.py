import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname =  False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL: ' ) 

for _ in range(7):
   
    html= urllib.request.urlopen( url, context= ctx).read()

    soup = BeautifulSoup(html, 'html.parser')

    tags= soup('a')

    third_link = tags[17].get('href', None)
    
    print('The current link is: ' + third_link)
    
    url = urllib.parse.urljoin(url, third_link)


print('The last name in sequence: ', third_link.split('_')[-1].split('.')[0])
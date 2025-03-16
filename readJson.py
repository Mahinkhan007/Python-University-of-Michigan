import urllib.request
import urllib.error
import ssl
import json

url = input('url:')

ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_2155933.json'
    
data = urllib.request.urlopen(url, context= ctx).read()

load = json.loads(data)
counts =[]
info = load['comments']

for i in info:
    count = i['count']
    counts.append(count)
    
    #counts = [i['count'] for i in load['comments']]
    
print("total count:", len(counts))   
print("sum", sum(counts))
 

import urllib.request
import urllib.parse
import urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
    location = input("Location: ")
    
    if len(location) < 1: break

    location = location.strip()
    parms =dict()
    parms['q']= location
    
    url = serviceurl + urllib.parse.urlencode(parms)
    
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'features' not in js:
        print("Download error")
        print(data)
        break
    if len(js['features']) ==0:
        print("Object not found")
        print(data)
        break
    
    # print(json.dumps(js, indent=4))
    
    pluscode = js['features'][0]['properties']['plus_code']
    
    print("Plus code is ", pluscode)
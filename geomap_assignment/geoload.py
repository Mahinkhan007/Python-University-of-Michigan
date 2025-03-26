import http
import urllib.request, urllib.parse, urllib.error
import sqlite3
import json
import ssl
import time

con = sqlite3.connect('opengeo.sqlite')
cur = con.cursor()

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

cur.execute('''CREATE TABLE IF NOT EXISTS Location (address TEXT, geodata TEXT)''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh= open("where.data")
count = 0
notfound = 0
for line in fh:
    if count> 50: 
        print("Retrieved 50 locations. Restart to retrieve more")
        break
    
    address = line.strip()
    
    print("--------------------------------")
    
    cur.execute('''SELECT geodata FROM Location WHERE address=?''', (memoryview(address.encode()),))
    
    try:
        data = cur.fetchone()[0]
        print('Found in database', address)
        continue
    except:
        print("This address", address, "is still not stored in the database")
        pass
    
    parms = dict()
    parms['q'] =address
    
    url = serviceurl + urllib.parse.urlencode(parms)
    
    print("Retreiving location")
    uh = urllib.request.urlopen(url, context= ctx)
    
    data = uh.read().decode()
    print("Recieved data : ", len(data) , 'characters' , data[:20].replace('\n', '') )
    count = count +1
    print(count)
    
    
    try:
        js = json.loads(data)
    except:
        print(data)
        continue
    
    if not js or "features" not in js:
        print('Download error -')
        print(data)
        break
    
    if len(js['features']) == 0:
        print('Object not found')
        notfound += 1
        continue
        
        
    cur.execute('INSERT INTO Location(address,geodata) VALUES(?,?)', (memoryview(address.encode()), memoryview(data.encode()))   )
    print("This address", address, "has been stored in the database")
    
    
    con.commit()
    
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(2)
        
if notfound >0:
        print("Number of features for which location not found : " , notfound)
        
print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
    
    
    

import sqlite3

conn = sqlite3.connect('example.db')
cur =  conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts(org TEXT, count INTEGER)''')

file1 = input("Enter file name: ")

if len(file1) < 1: file1 = 'mbox.txt'
fh = open(file1)

for line in fh:
    if not line.startswith('From: '): continue
    words = line.split()
    email = words[1].split('@')
    org =email[1]
    cur.execute('''SELECT count FROM Counts WHERE org = ? ''', [org])
    row = cur.fetchone()
    if row is None: 
        cur.execute('''INSERT INTO Counts(org, count) VALUES(?, 1)''', [org])
    else:
        cur.execute('''UPDATE Counts SET count= count+1 WHERE org=?''', [org])   
    conn.commit()
    

# sqlStr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
sqlStr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlStr):
    print(( str(row[0]),row[1])) 
    
    
cur.close()
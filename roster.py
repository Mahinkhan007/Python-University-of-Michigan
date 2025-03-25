import sqlite3
import json

conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

cur.executescript(
'''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE
);


CREATE TABLE Course (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);

'''
    
)

fname = input("Enter File Name:")
if len(fname)<1:
    fname = 'roster_data.json'

strdata = open(fname) 
jsonread = json.load(strdata)



for entry in jsonread:
    
    name = entry[0]
    title = entry[1]
    role = entry[2]
    
    cur.execute('''INSERT OR IGNORE INTO User(name) VALUES (?) ''', [name])
    cur.execute('''SELECT id FROM User WHERE name = ?''', [name])
    user_id= cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Course(title) VALUES (?) ''', [title])
    cur.execute('''SELECT id FROM Course WHERE title = ?''', [title])
    course_id = cur.fetchone()[0]
    

    
    cur.execute('''INSERT OR REPLACE INTO Member(user_id, course_id, role) VALUES ( ?, ?, ? )''', ( user_id, course_id, role ) )
    
    conn.commit()
    

inputforsql = cur.execute('''SELECT User.name AS username, Course.title as title, Member.role AS role FROM User JOIN Course JOIN Member ON User.id = Member.user_id AND Course.id = Member.course_id ORDER BY User.name DESC , Member.role LIMIT 2''')


print(cur.fetchall())


input2= cur.execute('''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1;''')

print(input2.fetchall())

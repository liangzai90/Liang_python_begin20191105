#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe

import logging
logging.basicConfig(level=logging.INFO, filename="mylog.log")

print('Content-type: text/html \n')
import cgitb; cgitb.enable()
import sqlite3
conn =sqlite3.connect('myweb.db')
curs = conn.cursor()

curs.execute('select * from messages')
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]

logging.info("names:{}".format(names))
logging.info("rows:{}".format(rows))


print("""
<html>
  <head>
     <title>The FooBar Bulletin Board</title>
  </head>
     <body>
       <h1>The FooBar Bulletin Board</h1>
       """)

toplevel = []
children = {}

for row in rows:
    parent_id = row['reply_to']
    if parent_id is None:
        toplevel.append(row)
    else:
        children.setdefault(parent_id, []).append(row)

def format(row):
    print('<p><a href="view.cgi?id={id}i">{subject}</a></p>'.format(row))
    try: kids = children[row['id']]
    except KeyError: pass
    else:
        print('<blockquote>')
        for kid in kids:
            format(kid)
        print('</blockquote>')
    print('<p>')

for row in toplevel:
    format(row)

print("""
     </p>
     <hr />
     <p><a href="edit.cgi">Post message</a></p>
  </body>
</html>
""")








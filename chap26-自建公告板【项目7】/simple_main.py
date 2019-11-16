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


print("""
<html>
    <head>
      <title>The Qiuzhi Board</title>
    </head>
    
    <body>
     <h1>The QiuZhi Board</h1>""")


toplevel = []
children = {}

for row in rows:
    parent_id = row['reply_to']

    logging.info("222parent_id:{}".format(parent_id))
    logging.info("222 row..'reply_to':{}".format(row['reply_to']))

    if parent_id is None:
        toplevel.append(row)

        logging.info("333row:{}".format(row))
        logging.info("444toplevel:{}".format(toplevel))
    else:
        children.setdefault(parent_id, []).append(row)
        logging.info("555children:{}".format(children))


    def format(row):
        logging.info("666format-------------start")
        logging.info("777:{}".format(row['subject']))

        print(row['subject'])
        try:kids=children[row['id']]
        except KeyError:pass
        else:
            print('<blockquote>')
            for kid in kids:
                format(kid)
            print('</blockquote>')

    print('<p>')

    logging.info("101010toplevel2:{} ".format(toplevel))

    for temp in toplevel:
        format(temp)


print("""
    </p>    
    </body>
</html>
""")


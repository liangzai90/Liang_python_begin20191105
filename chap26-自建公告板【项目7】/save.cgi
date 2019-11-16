#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe


import logging
logging.basicConfig(level=logging.INFO, filename="mylog.log")

print('Content-type: text/html \n')

import cgitb; cgitb.enable()
import sqlite3
conn =sqlite3.connect('myweb.db')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()

sender = form.getvalue('sender')
subject = form.getvalue('subject')
text = form.getvalue('text')
reply_to = form.getvalue('reply_to')

logging.info("save.cgi.sender:{}".format(sender))
logging.info("save.cgi.subject:{}".format(subject))
logging.info("save.cgi.text:{}".format(text))
logging.info("save.cgi.reply_to:{}".format(reply_to))

if not (sender and subject and text):
    print('Please supply sender, subject, and text')
    sys.exit()

if reply_to is not None:
    query = ("""
    INSERT INTO messages(reply_to, sender, subject, text)
    VALUES({}, '{}', '{}', '{}')""".format(int(reply_to), sender, subject, text))
else:
    query = ("""
    INSERT INTO messages(sender, subject, text)
    VALUES('{}', '{}', '{}')""".format(sender, subject, text))

curs.execute(query)
conn.commit()

print("""
<html>

<head>
  <title>Message Saved</title>
</head>
<body>
  <h1>Message Saved</h1>
  <hr />
  <a href='main.cgi'>Back to the main page</a>
</body>
</html>s
""")











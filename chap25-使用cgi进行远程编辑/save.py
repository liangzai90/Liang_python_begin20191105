#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe

import cgitb
cgitb.enable()
print('Content-type:text/html\n')

from os.path  import join, abspath
from hashlib import sha1
import cgi, sys

BASE_DIR = abspath('data')
form = cgi.FieldStorage()
text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password')

if not (filename and text and password):
    print('Invalid parameters.')
    sys.exit()

if sha1(password.encode()).hexdigest != 'e11cf310a9d0dcb61ed62c71cbd290fda26a5ccc'
    print('Invalid password')
    sys.exit()
f = open(join(BASE_DIR, filename), 'w')
f.write(text)
f.close()
print("the file has been saved.")

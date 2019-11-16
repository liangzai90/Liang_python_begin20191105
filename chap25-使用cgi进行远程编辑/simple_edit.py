#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

text = form.getvalue('text', open('simple_edit.dat').read())
f = open('simple_edit.dat', 'w')
f.write(text)
f.close()

print("""Content-type: text/html

<html>
    <head>
    <title>A simple Editor</title>
    </head>
    
    <body>
    <form action='simple_edit.cgi' method='POST'>
    <textarea rows='50' cols='40' name='text'>{}</textarea><br />
    <input type='submit' />
    </form>
    </body>
</html>
""".format(text))


"""
http://localhost:88/cgi-bin/simple_edit.cgi

请在本地安装Apache环境：https://www.cnblogs.com/music-liang/p/11846268.html

"""


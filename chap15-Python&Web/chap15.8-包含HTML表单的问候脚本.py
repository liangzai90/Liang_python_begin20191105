#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
form = cgi.FieldStorage()
name = form.getvalue('name', 'world')

print("""Content-type:text/html

<html>
    <head>
        <title>Greeting Page</title>
    </head>
    
    <body>
        <h1>Hello, {}!</h1>       
        
        <form action='chap15.8.cgi'>
        Change name <input type='text' name='name' />
        <input type='submit' />
        </form>
    </body>
</html>
""".format(name))
print()
print("-----包含HTML表单的问候脚本-----")

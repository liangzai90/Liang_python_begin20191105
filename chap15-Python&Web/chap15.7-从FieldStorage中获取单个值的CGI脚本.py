#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe
import cgi
form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print('Content-type:text/plain\n')

print("-----从FieldStorage中获取单个值的CGI脚本-----")
# 支持在后面追加参数
# http://localhost:88/cgi-bin/chap15.7.cgi?name=abcde
print()
print("Hello, {}!".format(name))

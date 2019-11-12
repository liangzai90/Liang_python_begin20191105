#!/usr/bin/env python
print("Content-type:text/plain")
print()
print("-------使用CGI创建动态网页--------")

"""
python -m http.server --cgi
如果是在Linux下面，则第1行 应该像下面这么写
#!/usr/bin/env python
如果是在windows下面，则应该明确指出 python.exe的路径
#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe
"""

print("Hello, world!")
print()
print("CGI")

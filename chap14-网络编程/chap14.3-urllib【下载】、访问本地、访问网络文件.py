print("---------------访问 网络 文件-------------------")
import re
from urllib.request import urlopen
webpage = urlopen("http://www.python.org")
text = webpage.read()
print(text.decode())  # 解码获取到的文件  urlopen('https://www.python.org/jobs/').read().decode()
m = re.search(b'<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
print(m.group())
print(m.group(0))
print(m.group(1))


print("---------------访问 本地 文件-------------------")
# 访问本地文件
localPage = urlopen(r'file:F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap14\chap14.1.py')
# urlopen返回的类似于文件的对象支持方法close, read, readline,readlines还支持迭代
print(localPage.readline())
print(localPage.readline())
print(localPage.readline())
print(localPage.readline())


print("----------- 获取 远程文件【下载】 -----------")
import urllib
import urllib.request
urllib.request.urlretrieve('http://www.python.org', r'F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap14\python_webpage.html')
urllib.request.urlcleanup()

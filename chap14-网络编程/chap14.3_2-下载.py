print("----------- 获取 远程文件 -----------")
import urllib
import urllib.request
urllib.request.urlretrieve('http://www.python.org', r'F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap14\python_webpage.html')
urllib.request.urlcleanup()


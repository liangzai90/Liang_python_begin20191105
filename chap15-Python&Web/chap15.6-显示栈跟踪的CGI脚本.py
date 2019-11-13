#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe
import cgitb
cgitb.enable()
# 结尾不能缺少 \n ，否则会报错.Internal Server Error
print("Content-type:text/html\n")

print("-------显示栈跟踪的CGI脚本---使用cgitb进行调试----")
print()

print(3/0)
print("Hello,world!  -- cgitb debug --")


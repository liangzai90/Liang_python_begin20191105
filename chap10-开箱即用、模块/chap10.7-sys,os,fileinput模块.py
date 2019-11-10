print("============= 一些深受欢迎的标准库 =============")
# 1.sys
print("--------- sys 访问与python解释器紧密相关的变量和函数 --------")

import sys, pprint
pprint.pprint(dir(sys))  # 打印所有的变量和方法
pprint.pprint(sys.path)  # 一个字符串列表，包含导入模块的目录
print(sys.platform)  # 平台类型

print("----------- 反转并打印命令行参数 ------------")
import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))
# 要导入这个模块 并传入参数，才能看到效果。win32不知道如何传入参数给模块
# python -m progname args 将使用命令行参数args来执行程序progname


# 2.os
print("------------- os 访问多个操作系统服务--------------")
import os
print(os.environ)
system(command)  在子shell中执行操作系统命令.
os.system()用于运行外部程序。还有其他用于执行外部程序的函数，如 execv, popen

# 打开Xshell，请注意，这里用引号将Program Files和 Xshell 5括起来。否则底层shell将受阻于空白处
print("打开xshell，请注意，这里用引号将Program Files和 Xshell 5括起来。否则底层shell将受阻于空白处")
os.system(r'C:\"Program Files (x86)"\NetSarang\"Xshell 5"\Xshell.exe')

print("----启动浏览器-----")
os.system("C:\\Users\\heliang\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
os.system("C:\\Users\\heliang\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe  www.python.org")

import webbrowser
webbrowser.open("www.python.org")


# 3.fileinput
print("------------- fileinput --------------")



print("---------文件的打开、读、写-------")

print("在当前目录写入一个文件")
f = open("test.txt", 'w')
print(f.write("Hello, "))
f.write("\n")
print(f.write("wrold!"))
f.close()


print("在当前目录，读取一个文件")
f = open("test.txt", 'r')
print(f.read(4))  # Hell
print(f.read())  # o, wrold!
f.close()

print("----在指定目录，写入一个文件---")
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test.txt", "w")
print(f.write("01234567890123456789"))  # 写入字符串，返回字符串个数
print("------- seek 移动文件指针读取的位置 --------")
print(f.seek(5))  # 5
print(f.write("Hello, world!"))  # 13
f.close()

f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test.txt")
print(f.read())  # 01234Hello, world!89
f.close()


print("------ tell 返回当前位于文件的什么位置-------------")
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test.txt")
print(f.read(3))  # 012
print(f.read(2))  # 34
print(f.tell())  # 5
f.close()

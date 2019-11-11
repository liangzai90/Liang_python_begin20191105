print("=========== 使用文件的基本方法 ===========")

print("------- read(n) -----")
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test2.txt")
print(f.read(7))
print(f.read(4))
f.close()


print("------- read() -----")
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test2.txt")
print(f.read())
f.close()


print("------- readline() -----")
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test2.txt")
for i in range(3):
    print(str(i) + ': ' + f.readline(), end="")
f.close()

print("------- readlines() -----")
import pprint
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test2.txt")
pprint.pprint(f.readlines())
f.close()


print("------ write() ---------")
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test2.txt", "w")
f.write("this \n is no \n haiku.")
f.close()


print("------ writelines() -------")
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test2.txt")
lines = f.readlines()
f.close()
lines[1] = "isn't a \n"
f = open(r"F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap11\test2.txt", "w")
f.writelines(lines)
f.close()



print("--------迭代文件内容------")

"""
# 在这里打开文件
try:
    # 将数据写入到文件
    pass 
finally:
    file.close()

实际上有一条专门为此设计的语句，那就是 with 语句 
    
with open("testfile.txt") as somefile:
    do_something(somefile)
"""

def process(string):
    print("Processing:", string)

filename="test.txt"

print("------- read(n) 每次 一个 字符 ---------")
with open(filename) as f:
    while True:
        char = f.read(1)
        if not char: break
        process(char)


print("------- readline() 每次 一行 ---------")
with open(filename) as f:
    while True:
        line = f.readline()
        if not line: break
        process(line)


print("------ readlines() 读取所有的内容 ---------")
with open(filename) as f:
    for line in f.readlines():
        process(line)



print("----------延迟行迭代. fileinput迭代行 -------")
import fileinput
for line in fileinput.input(filename):
    process(line)


print("-------- 文件 迭代器 【最常见】---------")
print("----- 迭代文件------")
with open(filename) as f:
    for line in f:
        process(line)


print("-------- 在不将文件对象赋给变量的情况下迭代文件 ------")
for line in open(filename):
    process(line)

import sys
for line in sys.stdin:
    process(line)


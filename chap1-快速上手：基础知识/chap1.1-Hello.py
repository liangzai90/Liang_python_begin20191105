# -*- coding: utf-8 -*-

import math
import cmath
import turtle

# 海龟制图，绘制一个三角形
# 参阅python的库参考手册，可以找到turtle相关介绍

print("Hello world!")
print("-----------floor向下取整（x轴的负方向）-------------------")
print(math.floor(1))  # 1
print(math.floor(1.1))  # 1
print(math.floor(1.5))  # 1
print(math.floor(-1))  # -1
print(math.floor(-1.1))  # -2
print(math.floor(-1.5))  # -2
print("-----------ceil向上取整（x轴的正方向）-------------------")
print(math.ceil(1))  # 1
print(math.ceil(1.1))  # 2
print(math.ceil(1.5))  # 2
print(math.ceil(-1))  # -1
print(math.ceil(-1.1))  # -1
print(math.ceil(-1.5))  # -1
print("-----------round四舍五入 取整-------------------")
print(round(1))  # 1
print(round(1.1))  # 1
print(round(1.5))  # 2
print(round(-1))  # -1
print(round(-1.1))  # -1
print(round(-1.5))  # -2  舍入到偶数
print("------------------end-------------------")

# 以字符串方式获取用户输入
name = input("Please input you Name:")
print("Your name is:" + name)

x = input("input x:")
y = input("input y:")
print(int(x) * int(y))
print("------------------end-------------------")


# 海龟绘图法，绘制三角形
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

print(repr("Hello, \n world!"))  # 会打印 \n
print(str("Hello, \n world!"))  # 不会打印 \n

# 输入多行字符
print('''This is a very long string.It continues here.  
  And it's not over yet. "Hello, world!"
Still here.''')

# 利用转义字符实现多行字符串输入
print("hello, \
World!")

# 不能以\作为字符串结尾，如果一定要输出，则把\作为一个单独在字符输出
print(r"C:\Program Files\foo\bar"  '\\')


# 编码问题,默认编码都是 utf-8
print("Hello, world".encode("ASCII"))
print("Hello, world".encode("UTF-8"))  # ASCII 和UTF-8输出相同
print("Hello, world".encode("UTF-32"))

# print("Hello, 何亮".encode("ASCII")) # 编译器会报错
print("Hello, 何亮".encode("UTF-8"))
print("Hello, 何亮".encode("UTF-32")) # utf-32输出的编码更多一些
# encode是将字符串编码为bytes,所以输出的前面都有一个b

# 将byte字节流解码为字符串
print(b'Hello, \xe4\xbd\x95\xe4\xba\xae'.decode("UTF-8"))

# 除了decode(),encode()方法，还可以创建 bytes,str对象
print(bytes("Hello, 何亮", encoding="utf-8"))
print(str(b"Hello, \xe4\xbd\x95\xe4\xba\xae", encoding="utf-8"))

# 修改字符串，ord()用来获取单次的索引
x = bytearray(b"Hello!")
x[1] = ord(b"u")
print(x)



# 避免窗口立即关闭
input("Press <enter>")


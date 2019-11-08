# print
print("---------------函数 print-----------------")
# 1.打印多个参数. 用逗号分隔参数
print("Age:", 42)  # Age: 42

name = "Gumby"
salutation = "Mr."
greeting = "Hello"
print(greeting, salutation, name)  # Hello Mr. Gumby
print(greeting, ",", salutation, name)  # Hello , Mr. Gumby
# 请注意逗号前面的空格没有了...这里用了 +
print(greeting + ",", salutation, name)  # Hello, Mr. Gumby
print("----------自定义 分隔符------------")
print("I", "wish", "to", "register", "a", "complaint", sep="_")  # I_wish_to_register_a_complaint
print("----------自定义 结束字符串------------")
print("Hello,", end="")
print("world!")  # Hello,world!


print("---------------导入模块重命名------------------")
# 语句末尾添加as子句并指定别名
import math as foobar
print(foobar.sqrt(4))  # 2.0

from math import sqrt as foobar
print(foobar(4))  # 2.0


print("=====================赋值魔法=====================")
print("------------------序列解包-------------------")
# 1.序列解包
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# 序列解包（可迭代对象解包）
x, y = y, x
print(x, y, z)  # 2 1 3

values = 1, 2, 3
print(values)  # (1, 2, 3)
x1, y1, z1 = values
print(x1)  # 1
print(y1)  # 2
print(z1)  # 3

# 这让函数可以返回被打包成元组的多个值，然后通过一条赋值语句轻松地访问这些值
scoundrel = {"name": "Robin", "girlfriend": "Marion"}
key, value = scoundrel.popitem()
print(key)
print(value)

print("--------运算符*收集多余值--------")
a, b, *rest = [1, 2, 3, 4, 5, 6, 7]
print(a)  # 1
print(b)  # 2
print(rest)  # [3, 4, 5, 6, 7]

a, *middle, b = [1, 2, 3, 4, 5, 6, 7]
print(a)  # 1
print(middle)  # [2, 3, 4, 5, 6]
print(b)  # 7

name = "Albus  Percival  Wulfric  Brian  Dumbledore"
first, *middle, last = name.split()
print(first)  # Albus
print(middle)  # ['Percival', 'Wulfric', 'Brian']
print(last)  # Dumbledore

a, *b, c = "abc"
print(a)  # a
# 输出的是一个序列
print(b)  # ['b']
print(c)  # c
b = "666"
print(b)  # 666


print("-------------------- 链 式 赋 值 ----------------------")
x = y = 123
x = 2
y = 3
print(x)
print(y)

print("--------------- 增 强 赋 值 --------------")
x = 2
x += 1
print(x)  # 3
x *=2
print(x)  # 6

fnord = "foo"
fnord +="bar"
print(fnord)  # foobar
fnord *= 2
print(fnord)  # foobarfoobar


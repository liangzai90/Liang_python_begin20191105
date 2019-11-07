# 转换标志
# 三个标志（s,r,a）指定分别使用str,repr,ascii进行转换
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))  # π 'π' '\u03c0'
# 函数 str 通常创建外观普通的字符串版本（这里没有对输入字符串做任何处理）
# 函数 repr 尝试创建给定值的Python表示（这里是一个字符串字面量）
# 函数 ascii 创建只包含 ASCII 字符的表示

res1 = "The number is {num}".format(num=42)
res2 = "The number is {num:f}".format(num=42)
res3 = "The number is {num:.2f}".format(num=42)
res4 = "The number is {num:.2f}".format(num=42.153456)
print(res1)  # The number is 42
print(res2)  # The number is 42.000000
print(res3)  # The number is 42.00
print(res4)  # The number is 42.15

# 转为二进制
res5 = "The number is {num:b}".format(num=42)
print(res5)  # The number is 101010

res6 = "The number is {num:.0%}".format(num=0.6666)
res7 = "The number is {num:.1%}".format(num=0.6666)
print(res6)  # The number is 67%
print(res7)  # The number is 66.7%



"""
字符串格式设置中的类型说明
b  将整数表示为二进制数
c  将整数解读为Unicode码点
d  将整数视为十进制数进行处理，这是整数默认使用的说明符
e  使用科学表示法来表示小数（用e来表示指数）
E  与e相同，但使用E来表示指数
f  将小数表示为定点数
F  与f相同，但对于特殊值（nan和inf），使用大写表示
g  自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数
G  与g相同，但使用大写来表示指数和特殊值
n  与g相同，但插入随区域而异的数字分隔符
o  将整数表示为八进制
s  保持字符串的格式不变，这是默认用于字符串的说明符
x  将整数表示为十六进制数并使用小写字母
X  与x相同，但使用大写字母
%  将数表示为百分比值（乘以100，按说明符f设置格式，然后再在后面加上%）

"""

# 宽度、精度和千分位分隔符
print("===============宽度、精度和千分位分隔符=====================")
res1 = "{num:10}".format(num=3)
print(res1)  # '         3'
res2 = "{name:10}".format(name="liang")
print(res2)  # 'liang     '

res3 = "Pi day is {pi:.2f}".format(pi=3.141592654)
print(res3)  # Pi day is 3.14
# 同时指定宽度和精度
res4 = "Pi day is {pi:10.2f}".format(pi=3.141592654)
print(res4)  # Pi day is       3.14

res5 = "{:.5}".format("Guido van Rossum")
print(res5)  # Guido
# 用逗号指出添加 千位分隔符
res6 = "One googol is {:,}".format(10**100)
print(res6)



print("===============符号、对齐和用0填充=====================")
# 用0填充，总共10位，保留2位小数
res1 = "{:010.2f}".format(3.141592654)
print(res1)  # 0000003.14

# 使用左对齐、右对齐、居中，可分别使用<,>,^
res2 = "{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(3.141592654)
# 宽度为10，保留2位小数，居左、居中、居右对其
print(res2)

# 使用填充字符来扩充对其说明符...使用指定的字符填充
res3 = "{:$^15}".format(" WIN BIG ")
print(res3)  # $$$ WIN BIG $$$

# 具体说明符=,它将填充字符放在符号和数字之间
from math import pi
res4 = "{0:10.2f}\n{1:10.2f}".format(pi, -pi)
print(res4)  # '      3.14'
# 这里将指定的填充字符（空格），放在了符号（负号）和数字之间
res5 = "{0:10.2f}\n{1:=10.2f}".format(pi, -pi)
print(res5)  # '-     3.14'

print("------------令人崩溃的格式控制----------------")
# 默认设置
res6 = "{0:-.2}\n{1:-.2}".format(pi, -pi)
print(res6)
res7 = "{0:+.2}\n{1:+.2}".format(pi, -pi)
print(res7)
res8 = "{0: .2}\n{1: .2}".format(pi, -pi)
print(res8)

# '#'的特殊用法
res9 = "{:b}".format(42)
print(res9)  # 101010
res10 = "{:#b}".format(42)
print(res10)  # 0b101010

res11 = "{:g}".format(42)
print(res11)  # 42
res12 = "{:#g}".format(42)
print(res12)  # 42.0000




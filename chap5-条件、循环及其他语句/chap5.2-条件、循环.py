print("=============条件和条件语句=================")
# 用作布尔表达式（如用作if语句中的条件）时，下面的值豆浆解释为假
# False   None  0  ""  ()  []  {}
print("False   None  0  ""  ()  []  {}")
print(bool("I think, therefore I am"))  # True
print(bool(42))  # True
print(bool(''))  # False
print(bool(0))  # False
# 虽然都是False,他两并不相等的
print([] != False)  # True

name = input("What is your name?")
if name.endswith("Heliang"):
    print("Hello, Mr. He")
else:
    print("Who are you?", name)

print("-----------类似C语言的 三目运算符--------------")
status = "friend" if name.endswith("Heliang") else "stranger"
print(status)


num = int(input("Enter a number:"))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")


name = input("What is your name? ")
if name.endswith("Heliang"):
    if name.startswith("Mr."):
        print("Hello, Mr. He")
    elif name.startswith("Mrs."):
        print("Hello, Mrs. He")
    else:
        print("Hello, He")
else:
    print("Hello, stranger")

print("-------------- is ---------------")
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)  # True
print(x == z)  # True
print(x is y)  # True
# 虽然相等，但并不是同一对象
print(x is z)  # False

print("-------------- in ---------------")
name = input("What is your name?")
if 's' in name:
    print("Your name contains the letter 's'.")
else:
    print("Your name does not contain the letter 's'.")



print("--------------字符串和序列的比较-----------------")
print("alpha" < "beta")  # True
print("何" < "亮")  # False
# ord 获悉字母的序列值
print(ord("何"))  # 20309
print(ord("亮"))  # 20142
# chr 将序列值转为 字符
print(chr(20309))  # 何
print(chr(20142))  # 亮

print("a" < "A")  # False
print(ord("a"))  # 97
print(ord("A"))  # 65
print(ord("0"))  # 48
print(ord("9"))  # 57

print("a".lower() < "B".lower())  # True

print([1, 2] < [2, 1])  # True

print("--------------- 布 尔 运 算 符 and,or,not-------------------")
number = int(input("Enter a number between 1 and 10: "))
if number <=10 and number >=1:
    print("Great!")
else:
    print("Wrong!")

name = input("Please enter your name: ") or "<unknown>"
print(name)
print("----------------- inner peace --------------------")


print("------------------- assert -------------------------")
age = 10
assert 0 < age < 100
age = -1
# 此处会出发断言
assert 0 < age < 100  # AssertionError

# 对断言做说明
age = -1
assert 0 < age < 100, "The age must be realistic"
# AssertionError: The age must be realistic


print("-------------- while 循环 --------------------")
x = 1
while x <= 10:
    print(x)
    x += 1


name = ""
while not name:
    name = input("Please enter your name:")
print("Hello, {}!".format(name))


words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for numb in numbers:
    print(numb)

# 包含起始位置，不包含结束
ret1 = list(range(0, 10))
print(ret1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ret2 = range(10)
print(ret2)  # range(0, 10)

# 打印1~15
for number in range(1, 15+1):
    print(number)


print("-------------------- 迭 代 字 典 -----------------------")
dict_1 = {'x': 1, 'y': 2, 'z': 3}
for key in dict_1:
    print(key, 'corresponds to', dict_1[key])

print(dict_1.keys())  # dict_keys(['x', 'y', 'z'])
print(dict_1.values())  # dict_values([1, 2, 3])

# 序列解包
for key, value in dict_1.items():
    print(key, 'corresponds to', value)



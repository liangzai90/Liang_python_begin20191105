
# 字符串方法
print("=====================字符串方法=========================")
# 1.center
print("------------------ 方法 center ----------------------")
res1 = 'The Middle by Jimmy Eat World'.center(39)
res2 = 'The Middle by Jimmy Eat World'.center(39,"*")
print(res1)
print(res2)

# 2.find
print("------------------ 方法 find ----------------------")
res3 = "with a moo-moo here, and a moo-moo there".find("moo")
print(res3)  # 7
# find 是大小写敏感的
title = "Monty Python's Flying Circus"
print(title.find("Monty"))  # 0
print(title.find("Python"))  # 6
print(title.find("Flying"))  # 15
print(title.find("Zirquss"))  # -1

subject = "$$$ Get rich now!!! $$$"
print(subject.find("$$$"))  # 0
# 只指定起点
print(subject.find("$$$", 1))  # 20
print(subject.find("!!!"))  # 16
# 同时指定了起点和终点
print(subject.find("!!!", 0, 16))  # -1


# 3.join
print("------------------ 方法 join ----------------------")
seq = ['1', '2', '3', '4', '5']
temp1 = '+'
# 合并一个字符串列表
res = temp1.join(seq)
print(res)  # 1+2+3+4+5

dirs = '', 'usr', 'bin', 'env'
res2 = "/".join(dirs)
print(res2)  # /usr/bin/env
print("C:" + '\\'.join(dirs))  # C:\usr\bin\env


# 4.lower
print("------------------ 方法 lower ----------------------")
res1 = "Trondheim Hammer Dance".lower()
print(res1)

name = "Gumby"
names = ["gumby", "smith", "jones"]
if name.lower() in names: print("Found it!")

# 5.replace
print("------------------ 方法 replace ----------------------")
res1 = "This is a test".replace("is", "eez")
print(res1)  # Theez eez a test

# 6.split，
print("------------------ 方法 split 分割字符串，功能和join相反----------------------")
res1 = "1+2+3+4+5".split("+")
print(res1)  # ['1', '2', '3', '4', '5']

res2 = '/usr/bin/env'.split('/')
print(res2)  # ['', 'usr', 'bin', 'env']
res22 = "/".join(res2)
print(res22)  # /usr/bin/env

res3 = "Using the default".split()
print(res3)  # ['Using', 'the', 'default']


# 7.strip
print("------------------ 方法 strip 将字符串开头和末尾的空白删除--------------------")
res1 = "  internal whitespace is kept    ".strip()
print(res1)

names = ["gumby", "smith", "jones"]
name = 'Gumby '
if name in names: print('Found it!AAA')
if name.strip() in names: print('Found it!BBB')
if name.strip().lower() in names: print('Found it!CCC')

# 删除开头和末尾的 指定字符串
res = "*** SPAM * for * everyone!!! ***".strip(" *!")
print(res)  # SPAM * for * everyone


# 8.translate
print("------------------ 方法 translate 替换字符串的特定部分，只能单字替换--------------------")
table = str.maketrans('cs', 'kz')
print(table)  # {99: 107, 115: 122}
res1 = "this is an incredible test".translate(table)
print(res1)  # thiz iz an inkredible tezt

# 第3个可选的参数，可以指定要将哪些字母删除
table = str.maketrans('cs', 'kz', ' ')
res2 = "this is an incredible test".translate(table)
print(res2)  # thizizaninkredibletezt

# 9.判断字符串是否满足条件
print("===============判断字符串是否满足条件==================")
"""
很多字符串方法都以 is 大头，如 isspace、isdigit和isupper，
它们判断字符串是否具有特定的性质（如包含的字符全为空白、数字或大写）。
如果字符串具备特定的性质，这些方法就返回True，否则返回False

附录B:
isalnum, isalpha, isdecimal, isdigit, isidentifier, 
islower, isnumeric, isprintable, isspace, istitle, 
isupper

"""

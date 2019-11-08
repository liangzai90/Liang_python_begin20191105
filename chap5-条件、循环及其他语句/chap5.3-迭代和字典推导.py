print("------------------ 迭 代 工 具 -------------------")
print("----------------并行迭代----------------")
names = ["anne", "beth", "george", "damon"]
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], "is", ages[i], "years old.")

ret = list(zip(names, ages))
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')

# zip缝合，在最短的序列用完后结束
ret2 = list(zip(range(5), range(50)))
print(ret2)  # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

print("-------------------迭代时获取索引----------------")
index = 0
strings = ["a", "b", "c", "d", "e", "f", "g", "h"]
for string in strings:
    if 'f' in string:
        strings[index] = '[sore]'
    index += 1
print(strings)  # ['a', 'b', 'c', 'd', 'e', '[sore]', 'g', 'h']


for index, string in enumerate(strings):
    if 'c' in string:
        strings[index] = '[censored]'
print(strings)  # ['a', 'b', '[censored]', 'd', 'e', '[sore]', 'g', 'h']


print("---------------- 反向迭代和排序后再迭代 -------------------")
ret1 = sorted([4, 3, 6, 8, 3])
print(ret1)  # [3, 3, 4, 6, 8]
ret2 = sorted("Hello, world!")
print(ret2)  # [' ', '!', ',', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
ret3 = list(reversed("Hello, world!"))
print(ret3)  # ['!', 'd', 'l', 'r', 'o', 'w', ' ', ',', 'o', 'l', 'l', 'e', 'H']
ret4 = ''.join(reversed("Hello, world!"))
print(ret4)  # !dlrow ,olleH


print("----------------------跳出循环 break, continue, ------------------------")
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

# 不停输入字符，为空则退出循环
while True:
    word = input("Please enter a word: ")
    if not word: break
    # do something
    print("The word was ", word)


print("----------- 循环中的 else -------------")
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print("Find {}.".format(n))
        break
    else:
        print("did't find it!")


print("---------------简单推导-------------------")
ret = [x * x for x in range(10)]
print(ret)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("-------------打印能被3整除的平方值--------------------")
ret = [x * x for x in range(10) if x % 3 == 0]
print(ret)  # [0, 9, 36, 81]

ret = [(x, y) for x in range(2) for y in range(3)]
print(ret)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

result = []
for x in range(2):
    for y in range(3):
        result.append((x, y))
print(result)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

girls = ["alice", "bernice", "clarice"]
boys = ["chris", "arnold", "bob"]
ret = [b + "+" + g for b in boys for g in girls if b[0] == g[0]]
print(ret)  # ['chris+clarice', 'arnold+alice', 'bob+bernice']

# 相比上面的2层循环，下面有更优解决方案
girls = ["alice", "bernice", "clarice"]
boys = ["chris", "arnold", "bob"]
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b + "+" + g for b in boys for g in letterGirls[b[0]]])
# ['chris+clarice', 'arnold+alice', 'bob+bernice']
print(letterGirls)  # {'a': ['alice'], 'b': ['bernice'], 'c': ['clarice']}


print("---------------使用花括号来执行 字典推导--------------------")
squares = {i: "{} squared is {}.".format(i, i**2) for i in range(3)}
print(squares)  # {0: '0 squared is 0.', 1: '1 squared is 1.', 2: '2 squared is 4.'}


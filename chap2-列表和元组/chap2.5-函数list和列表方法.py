# 函数list
print(list("hello"))

# 1.修改列表：给元素赋值
print("---------------修改列表：给元素赋值--------------")
x = [1, 1, 1]
x[1] = 2
print(x)  # [1, 2, 1]

# 2.删除元素
print("---------------删除元素--------------")
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)  # ['Alice', 'Beth', 'Dee-Dee', 'Earl']

# 3.给切片赋值
print("---------------给切片赋值--------------")
name = list("Perl")
print(name)  # ['P', 'e', 'r', 'l']
name[2:] = list('ar')
print(name)  # ['P', 'e', 'a', 'r']

name = list("Perl")
name[1:] = list('ython')
print(name)  # ['P', 'y', 't', 'h', 'o', 'n']

# 在不替换原有元素的情况下，插入新元素
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)  # [1, 2, 3, 4, 5]
# 空切片
numbers[1:4] = []
print(numbers)  # [1, 5]

numbers[:] = []
print(numbers)  # []

# 设置切片步长
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numbers[1:6:2]
print(numbers)  # [0, 2, 4, 6, 7, 8, 9, 10]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numbers[8:1:-2]
print(numbers)  # [0, 1, 3, 5, 7, 9, 10]


# 列表方法 .[方法] 是与 对象（列表，数、字符串等）联系紧密的 [函数]。通常像这样调用方法： object.method(argument)
print("==================列表方法 object.method(argument)==================")
# 1.append
print("--------------- 方法append 将一个对象附加到对象末尾--------------")
alst = [1, 2, 3]
alst.append(4)
print(alst)  # [1, 2, 3, 4]
alst.append([7, 8, 9])
print(alst)  # [1, 2, 3, 4, [7, 8, 9]]

# 2.clear
print("--------------- 方法clear 就地清空列表的内容--------------")
lst = [1, 2, 3]
lst.clear()
# 清空列表，类似于 lst[:] = []
print(lst)  # []

# 3.copy
# 常规赋值，只是将另一个名称关联到列表
print("--------------- 方法copy 复制列表--------------")
a = [1, 2, 3]
b = a
b[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 4, 3]

# 要让a,b指向不同的列表，需要将b关联到a的副本
a1 = [1, 2, 3]
b1 = a1.copy()
b2 = list(a1)
b3 = a1[:]
b1[1] = 4
b2[1] = 4
b3[1] = 4
print(a1)  # [1, 2, 3]
print(b1)  # [1, 4, 3]
print(b2)  # [1, 4, 3]
print(b3)  # [1, 4, 3]

# 4.count
print("--------------- 方法count 计算指定的元素在列表中出现了多少次--------------")
result = ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
print(result)  # 2

# 5.extend
print("--------------- 方法extend 同时将多个值附加到列表末尾--------------")
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
# a[len(a):] = b  # 赋值给切片，也可以实现拼接效果（可读性不高）
print(a)  # [1, 2, 3, 4, 5, 6]
print(b)  # [4, 5, 6]

# 6.index
print("--------------- 方法index 在列表中查找指定值第一次出现的索引--------------")
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
index = knights.index('who')
print(index)  # 4

# 7.insert
print("--------------- 方法insert 用于将一个[对象]插入列表--------------")
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.insert(3, "four")
# 通过切片的方式插入 [对象]
# numbers[3:3] = 'four'  # [1, 2, 3, 'f', 'o', 'u', 'r', 4, 5, 6, 7]
# numbers[3:3] = ['four']  # [1, 2, 3, 'four', 4, 5, 6, 7]
print(numbers)  # [1, 2, 3, 'four', 4, 5, 6, 7]


# 8.pop
print("--------------- 方法pop 从列表中删除一个元素（末尾为最后一个元素），并返回这一元素--------------")
print("pop 是唯一既修改列表，又返回一个非None值的 列表方法")
x = [1, 2, 3]
# 默认删除最末尾元素
print(x.pop())  # 3
print(x)  # [1, 2]
# 通过参数，指定某个索引的元素被删除
print(x.pop(0))  # 0

# 9.remove
print("--------------- 方法remove 用于删除第一个为指定的元素--------------")
print("remove是就地修改且不返回值的方法之一")
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')  # 第2个'be'还在
print(x)  # ['to', 'or', 'not', 'to', 'be']

# 10.reverse
print("--------------- 方法reverse 按相反的顺序排列列表中的元素--------------")
x = [1, 2, 3, 4, 'a', 'bcd', 100, 99]
x.reverse()
print(x)  # [99, 100, 'bcd', 'a', 4, 3, 2, 1]

# 11.sort
print("--------------- 方法sort 对列表进行就地排序--------------")
x = [1, 3, 5, 9, 4, 2, 0, 8, 7, 6]
y = x.copy()
y.sort()
z = sorted(x)  # sorted() 方法，返回排序后的副本
print(x)  # [1, 3, 5, 9, 4, 2, 0, 8, 7, 6]
print(y)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(z)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sorted("3Python12"))  # ['1', '2', '3', 'P', 'h', 'n', 'o', 't', 'y']

# 12.高级排序
# sort()接受2个可选参数，key和reverse
# 在很多情况下，将key设置为一个自定义函数很有用
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate', 'efg']
x.sort(key=len)
print(x)  # ['add', 'efg', 'acme', 'aerate', 'abalone', 'aardvark']

x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)  # [9, 7, 6, 4, 2, 1]


# 元组：不可修改的序列
print("=================元组：不可修改的序列================")
a = (1, 2, 3)
b = (42)  # 这个不是元组
c = (42,)  # 表示只有一个值的元组，后面的 [逗号] 是必须的
print(a)
print(b)
print(c)

d = 3 * (40 + 2)
e = 3 * (40 + 2,)
print(d)  # 126
print(e)  # (42, 42, 42)

# 1.tuple,工作原理与list很像：它将一个序列作为参数，并将其转换为元组。
print("================= 函数tuple ====================")
result1 = tuple([1, 2, 3, 4])
result2 = tuple('1a2b3c4e5f6g')
result3 = tuple((1, 2, 3))
print(result1)  # (1, 2, 3, 4)
print(result2)  # ('1', 'a', '2', 'b', '3', 'c', '4', 'e', '5', 'f', '6', 'g')
print(result3)  # (1, 2, 3)

print("-----------tuple(元组) to list")
yuanzuA = (1, 2, 3, 4)
listb = list(yuanzuA)
print(yuanzuA)  # (1, 2, 3, 4)
print(listb)  # [1, 2, 3, 4]
# yuanzuA[1] = 7   # 对元组的修改会报错
listb[1] = 7  # 对列表修改是ok的

# 元组的切片也是元组。元组存在的意义
# 1.它们用作映射中的键（以及集合的成员），而列表不行。
# 2.有些内置函数和方法返回元组

# python计算斐波拉契数列
print("----------- python计算斐波拉契数 ------------------")
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


print("============================= 自定义函数 =============================")
# callable
print("---------- callable 判断某个对象是否可调用 -------")
import math
x = 1
y = math.sqrt
print(callable(x))  # False
print(callable(y))  # True

print("---------- 自定义函数 hello() ---------")
def hello(name):
    return "Hello, " + name + "!"
# 调用函数
print(hello("world"))  # Hello, world!

print("----------自定义函数 fibs() ------------")
def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

print(fibs(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


print("-------------- 给函数添加文档字符串 ------------------")
def square(x):
    'Calculates the square of the number x.'
    return x * x

print(square.__doc__)  # Calculates the square of the number x.
print("--------------利用 help 获取函数信息--------------")
help(square)  # 输出了一大堆内容...


print("-----------函数内参数的改变-------------")
def change(n):
    n[0] = "Mr. Gumby"
names = ["Mrs. Entity", "Mrs. Thing"]
# 传递一个副本过去，函数内修改，不会影响传入参数的值
change(names[:])
print(names)  # ['Mrs. Entity', 'Mrs. Thing']
# 参数作为可变的数据结构，函数内修改会影响实参的值。如果参数只是普通变量，函数内修改是不会影响实参的值。
print("参数作为可变的数据结构，函数内修改会影响实参的值。")
print("如果参数只是普通变量，函数内修改是不会影响实参的值。")
change(names)
print(names)  # ['Mr. Gumby', 'Mrs. Thing']


print("----------------- init() --------------------")
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
storange = {}
init(storange)
print(storange)  # {'first': {}, 'middle': {}, 'last': {}}
me = "Magnus Lie Hetland"
storange['first']['Mangus'] = [me]
storange['middle']['Lie'] = [me]
storange['last']['Hetland'] = [me]
print(storange)  # {'first': {'Mangus': ['Magnus Lie Hetland']}, 'middle': {'Lie': ['Magnus Lie Hetland']}, 'last': {'Hetland': ['Magnus Lie Hetland']}}


print("--------------- lookup() ---------------")
def lookup(data, label, name):
    return data[label].get(name)
# 返回的是列表
print(lookup(storange, 'middle', 'Lie'))  # ['Magnus Lie Hetland']


print("----------------- store() 将人员存储到数据结构中.-----------------------")
def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, "666")
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        print("-----for: ", label, name)
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, "MMM AAA BBB")
ret = lookup(MyNames, 'middle', 'AAA')
print(ret)
print(MyNames)

store(MyNames, "Robin Hood")
store(MyNames, "Robin Locksley")
store(MyNames, "Mr. Gumby")
print(lookup(MyNames, 'first', 'Robin'))  # ['Robin Hood', 'Robin Locksley']
print(lookup(MyNames, 'middle', '_N_'))  # ['Robin Hood', 'Robin Locksley', 'Mr. Gumby']
print(MyNames)


print("-----------修改参数----------------")
# 方法1，通过返回值修改
def inc(x):
    return x + 1
foo = 10
foo = inc(foo)
print(foo)  # 11

# 方法2，将值放在列表中，传入列表
def inc2(x):
    x[0] = x[0] + 1
foo2 = [10]
inc2(foo2)
print(foo2)  # [11]


print("======================== 关键字参数 ==========================")
def hello_1(greeting, name):
    print('{}, {}!'.format(greeting, name))

def hello_2(name, greeting):
    print('{}, {}!'.format(name, greeting))
hello_1("Hello", "world")  # Hello, world!
hello_2("Hello", "world")  # Hello, world!

print("------使用名称指定的参数，称为 【关键字参数】， 最大的优点是可以指定默认值----------")
# 参数顺序无关紧要
hello_1(greeting="Hello", name="world")
hello_1(name="world", greeting="Hello")

# 名称很重要
hello_2(greeting="Hello", name="world")  # world, Hello!

def hello_3(greeting="Hello", name="world"):
    print("{}, {}!".format(greeting, name))
hello_3()
hello_3("Greetings")  # Greetings, world!
hello_3("Greetings", "universe")  # Greetings, universe!
# 第1个参数用默认值
hello_3(name="Gumby")  # Hello, Gumby!

print("------混用关键字参数和位置参数----------")
def hello_4(name, greeting = "Hello", punctuation = "!"):
    print("{}, {}{}".format(greeting, name, punctuation))
hello_4("Mars")  # Hello, Mars!
# 混用...
hello_4("Mars", "Howdy")  # Howdy, Mars!
hello_4("Mars", "Howdy", "...")  # Howdy, Mars...
hello_4("Mars", punctuation=".")  # Hello, Mars.
hello_4("Mars", greeting="Top of the morning to ya")  # Top of the morning to ya, Mars!


print("---------------- 收 集 参 数 --------------------")
def print_params(*params):
    print(params)
# 输出的是一个元组
print_params()  # ()
print_params("Test")  # ('Test',)
print_params("Test1", "Test2")  # ('Test1', 'Test2')
print_params("Test1", 2, 3)  # ('Test1', 2, 3)
print_params(1, 2, 3, 4)  # (1, 2, 3, 4)

def print_para2(title, *params):
    print(title)
    print(params)
print_para2("Params:", 1, 2, 3)

def in_the_middle(x, *y, z):
    print(x, y, z)
print("-----需要使用名称来指定后续参数，否则会报错")
in_the_middle(1, 2, 3, 4, 5, 6, z=7)

print("-----如果要收集关键字参数，必须用 ** ")
def print_params_3(**params):
    print(params)
print_params_3(x=1, y=2, z=3)  # {'x': 1, 'y': 2, 'z': 3}


print("--------各种技术结合-----")
def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)

print_params_4(1, 2, 3, 666, 777, 888, foo=1, bar=2)
# 1 2 3
# (666, 777, 888)
# {'foo': 1, 'bar': 2}

print_params_4(1, 2)
# 1 2 3
# ()
# {}


print("----------在姓名存储中使用这些技术-----------")
def store_3(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, "")
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]
data_3 = {}
init(data_3)
store_3(data_3, "Han Solo")
store_3(data_3, "Luke Skywalker", 'Anakin Skywalker')
print(lookup(data_3, 'last', 'Skywalker'))  # ['Luke Skywalker', 'Anakin Skywalker']
print(data_3)  # {'first': {'Han': ['Han Solo'], 'Luke': ['Luke Skywalker'], 'Anakin': ['Anakin Skywalker']}, 'middle': {'': ['Han Solo', 'Luke Skywalker', 'Anakin Skywalker']}, 'last': {'Solo': ['Han Solo'], 'Skywalker': ['Luke Skywalker', 'Anakin Skywalker']}}


print("-----------------分配参数：把参数打包传入函数------------------")
def add(x, y):
    return x + y
# 我们打包的2个参数
params = (1, 2)
# 调用函数，传入打包的参数
print("----调用函数时，使用 * 分配参数----")
ret = add(*params)
print(ret)  # 3

print("-----将字典的值分配给参数，使用 ** ---")
params = {'name': "Sir Robin", 'greeting': "Well met"}
hello_3(**params)  # Well met, Sir Robin!


def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')

def without_stars(kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')

args = {'name': "Mr. Gumby", "age": 42}
with_stars(**args)  # Mr. Gumby is 42 years old
without_stars(args)  # Mr. Gumby is 42 years old


print("-------------- 使用拆分运算符传递参数 ------------")
def foo(x, y, z, m=0, n=0):
    print(x, y, z, m, n)
def call_foo(*args, **kwds):
    print("Calling foo!")
    foo(*args, **kwds)


print("---------------三条语句：pass, del, exec ---------------------")
print("------------------ pass -------------------")
name = "Bill Gates"
if name == "Ralph Auldus Melish":
    print("Welcome!")
elif name == "Enid":
    # 还未完成...
    pass
elif name == "Bill Gates":
    print("Access Denied")


print("----------------- del -------------------")
scoundrel = {'age': 42, "first name": "Robin", "last name": "of Locksley"}
robin = scoundrel
print(scoundrel)  # {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
print(robin)  # {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
scoundrel = None
print(scoundrel)  # None
print(robin)  # {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}

x = ["Hello", "world"]
y = x
print(x)  # ['Hello', 'world']
print(y)  # ['Hello', 'world']
print("del 删除的是这个变量")
del x
print(y)  # ['Hello', 'world']
# print(x)  # NameError: name 'x' is not defined


print("------------- exec ,eval ------------------")
# 1.exec
exec("print('Hello, wrold!')")  # Hello, wrold!

from math import sqrt
scope = {}
exec('sqrt = 1', scope)  # 执行了赋值语句，但是变量放在了 scope当中，所以这里不会有 【变量名冲突】
print(sqrt(4))  # 2.0
ret = scope['sqrt']
print(ret)  # 1
# print(scope)  # 包含很多内容.
print(len(scope))  # 2
print(scope.keys())  # dict_keys(['__builtins__', 'sqrt'])

dict_1 = {}
dict_1.setdefault("age", 123)
print(dict_1)  # {'age': 123}  # {'age': 123}

print("------------ eval 计算用字符串表示的Python值（计算器的作用）---------------")
ret = eval(input("Enter an arithmetic expression: "))
print(ret)  # 类似计算器的功能

scope = {}
scope['x'] = 2
scope['y'] = 3
ret = eval('x * y', scope)
print(ret)  # 6

scope = {}
exec('x = 2', scope)
ret = eval('x * x', scope)
print(ret)  # 4

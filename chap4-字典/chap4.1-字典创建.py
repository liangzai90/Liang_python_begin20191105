# 字典
print("----------------- 字典 --------------------")
names = ["alice", "Beth", "Cecil", "Dee-Dee", "Earl"]
numbers = ['2341', '9102', '3158', '0142', '5551']
res = numbers[names.index("Cecil")]
print(res)


phonebook = {"Alice": '2341', "Beth": "9102", "Cecil": "3258"}
print(phonebook)

# 函数 dict
print("-------------- 函数 dict -------------------")
items = [('name', 'Gumby'), ('age', 42)]
res = dict(items)
print(res)  # {'name': 'Gumby', 'age': 42}
print(res['name'])  # Gumby

res2 = dict(name="Gumby", age=42)
print(res2)  # {'name': 'Gumby', 'age': 42}

# 基本的字典操作
"""

len(d)  返回字典d包含的项（键-值对）数。
d[k]  返回与键k相关联的值
d[k] = v  将值v关联到键k
del d[k]  删除键为k的项
k in d  检查字典d是否包含键为k的项

字典和列表的不同之处：
1.键的类型
2.自动添加
3.成员资格

"""

dict1 = {}
dict1[42] = "Foobar"
print(dict1)  # {42: 'Foobar'}

# 将字符串格式设置功能用于字典
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
res1 = "Ceil's phone number is {Cecil}.".format_map(phonebook)
print(res1)


print("--------------------------------------------------")
template = '''<html>
<head>
<title>{title}</title>
</head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>
'''

data = {"title": "My Home Page", "text": "Welcome to my home page!"}
print(template.format_map(data))


# 字典方法
print("================ 字 典 方 法 ================")
print("---------------- 方法 clear --------------------")
# 1.clear
dict_1 = {}
dict_1["name"] = "Gumby"
dict_1["age"] = 42
print(dict_1)  # {'name': 'Gumby', 'age': 42}
return_v = dict_1.clear()
print(dict_1)  # {}
print(return_v)  # None

x1 = {}
y1 = x1
x1["key"] = "value"
print(x1)  # {'key': 'value'}
print(y1)  # {'key': 'value'}
x1 = {}
print(x1)  # {}
print(y1)  # {'key': 'value'}

x2 = {}
y2 = x2
x2["key"] = "value"
print(x2)  # {'key': 'value'}
print(y2)  # {'key': 'value'}
x2.clear()
print(x2)  # {}
print(y2)  # {}


print("---------------- 方法 copy --------------------")
x3 = {"username": "admin", "machines": ['foo', 'bar', 'baz']}
y3 = x3.copy()
# 替换值的时候，原件x3不受影响
y3["username"] = "mlh"
y3["machines"].remove("bar")
# 修改副本中的值的时候，原件也会受影响。 bar 在x3,y3中都没有了
print(x3)  # {'username': 'admin', 'machines': ['foo', 'baz']}
print(y3)  # {'username': 'mlh', 'machines': ['foo', 'baz']}

print("--------------- 深 复 制 -----------------")
from copy import deepcopy
dict_1 = {}
dict_1["names"] = ["Alfred", "Bertrand"]
dict_2 = dict_1.copy()
dict_3 = deepcopy(dict_1)
dict_1["names"].append("Clive")
print(dict_1)  # {'names': ['Alfred', 'Bertrand', 'Clive']}
print(dict_2)  # {'names': ['Alfred', 'Bertrand', 'Clive']}
print(dict_3)  # {'names': ['Alfred', 'Bertrand']}


# 3.fromkeys
print("------------------ 方法 fromkeys -----------------------")
dict_1 = {}.fromkeys(['name', 'age'])
print(dict_1)  # {'name': None, 'age': None}

dict_2 = dict.fromkeys(["name", "age"])
print(dict_2)  # {'name': None, 'age': None}

dict_3 = dict.fromkeys(["name", "age"], '(unknown)')
print(dict_3)  # {'name': '(unknown)', 'age': '(unknown)'}

# 4.get
print("------------------ 方法 get -----------------------")
# 访问字典中没有的项会引发错误，如果使用了 get ，会返回None
dict_1 = {}
print(dict_1.get("name"))  # None

# 给访问指定默认值，这样将返回你指定的默认值，而不是None
dict_1 = {}
print(dict_1.get("name", "N/A"))  # N/A

# 5.items
print("------------------ 方法 items -----------------------")
dict_1 = {'title': "Python Web Site", "url": "http://www.python.org", "spam": 0}
# 返回一个包含所有字典项的列表
print(dict_1.items())  # dict_items([('title', 'Python Web Site'), ('url', 'http://www.python.org'), ('spam', 0)])
it = dict_1.items()
print(len(it))  # 3
print(('spam', 0) in it)  # True
# 将字典项复制到列表中
oneList = list(dict_1.items())
print(oneList)  # [('title', 'Python Web Site'), ('url', 'http://www.python.org'), ('spam', 0)]

# 6.keys
print("------------------ 方法 keys -----------------------")
print("----方法key返回一个字典试图，其中包含指定字典中的键----")
ketRet = dict_1.keys()
print(ketRet)  # dict_keys(['title', 'url', 'spam'])

# 7.pop
print("------------------ 方法 pop.弹出指定key键的元素 -----------------------")
dict_1 = {'x': 1, 'y': 2}
res1 = dict_1.pop('x')
print(res1)  # 1
print(dict_1)  # {'y': 2}

# 8.popitem
print("------------------ 方法 popitem ，随即弹出元素-----------------------")
dict_1 = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
ret1 = dict_1.popitem()
# 返回的ret1是一个元组，不可修改
print(ret1)  # ('title', 'Python Web Site')
print(dict_1)  # {'url': 'http://www.python.org', 'spam': 0}

# 9.setdefault
print("------------------ 方法 setdefault -----------------------")
# 如果键值存在，则修改；如果不存在，则插入数据。第2个参数默认为None
dict_1 = {}
ret1 = dict_1.setdefault('name', 'N/A')
print(ret1)  # N/A
print(dict_1)  # {'name': 'N/A'}

dict_1['name'] = 'heliang'
ret2 = dict_1.setdefault('name', 'N/A')
print(ret2)  # heliang
print(dict_1)  # {'name': 'heliang'}

# 10.update
print("------------------ 方法 update -----------------------")
dict_1 = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}

x = {'title': "Python Language Website"}
# 通过参数提供的字典，如果当前字典包含相同键，则替换，否则插入
dict_1.update(x)
print(dict_1)  # {'title': 'Python Language Website', 'url': 'http://www.python.org', 'changed': 'Mar 14 22:09:15 MET 2016'}

# 11.values
print("------------------ 方法 values ---------------------")
# 返回值组成的字典试图，可包含重复的值
dict_1 = {}
dict_1[1] = 1
dict_1[2] = 2
dict_1[3] = 3
dict_1[4] = 1
ret = dict_1.values()
print(ret)  # dict_values([1, 2, 3, 1])


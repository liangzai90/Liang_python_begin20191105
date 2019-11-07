# 设置字符串格式

# %s 转换说明符
print("------------------ %s 转换说明符 -----------------------")
trans_str = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(trans_str % values)  # Hello, world. Hot enough for ya?

# 模板字符串
print("------------------ $ 模板字符串 -----------------------")
from string import Template
tmpl = Template("Hello, $who! $what enough for ya?")
res = tmpl.substitute(who="Mars", what="Dusty")
print(res)  # Hello, Mars! Dusty enough for ya?


# format .字符串方法 format
print("------------------ format 字符串方法 -----------------------")
res1 = "{},{} and {}".format("first", "second", "third")
print(res1)  # first,second and third
res2 = "{0},{1} and {2}".format("first", "second", "third")
print(res2)  # first,second and third
# object.format("index_0", "index_1", "index_2")
res3 = "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")
print(res3)  # to be or not to be

# 关键字参数的排列顺序无关紧要。这里还指定了格式说明符 .2f
from math import pi
res4 = "{name} is approximately {value:.2f}.".format(value=pi, name="π")
print(res4)  # π is approximately 3.14.

print("------------------ f字符串，在字符串前面加f -----------------------")
# python 3.6中，如果变量与替换字段同名，可以这样简写
from math import e
res5 = f"Euler's constant is roughly {e}."
res6 = f"Euler's constant is roughly {e}.".format(e=e)
print(res5)  # Euler's constant is roughly 2.718281828459045.
print(res6)  # Euler's constant is roughly 2.718281828459045.

testName = "heliang"
res7 = f"abcde,{testName}"
print(res7)  # abcde,heliang


print("---------------完整版----------------------")
res8 = "{{ceci n'est pas une replacement field}}".format()
print(res8)  # {ceci n'est pas une replacement field}

res9 = "{foo} {} {bar} {}".format(6, 666, bar=4, foo=3)
print(res9)  # 3 6 4 666

res10 = "{foo} {1} {bar} {0}".format(7, 777, bar=4, foo=3)
print(res10)  # 3 777 4 7

fullname = ["Alfred", "Smoketoomuch"]
res11 = "Mr {name[1]}".format(name=fullname)
print(res11)  # Mr Smoketoomuch

import math
tmpl = "the {mod.__name__} module defines the value {mod.pi} for π."
res12 = tmpl.format(mod = math)
print(res12)  # the math module defines the value 3.141592653589793 for π.





print("---------多态和方法----------")

print("-------- 方法 count 的多态--------")
ret1 = "abcdea".count('a')
ret2 = [1, 2, 3, 'a', 'a', 4, 'a', 'b'].count('a')
print(ret1)  # 2
print(ret2)  # 3

print("-----通过打印一条消息来指出对象的长度----")
def length_message(x):
    print("The length of", repr(x), "is", len(x))

length_message("Fnord")  # The length of 'Fnord' is 5
length_message([1, 2, 3, 4])  # The length of [1, 2, 3, 4] is 4


print("----------- 封 装 --------------")

print("----------创建 自定义类---------------")
__metaclass__ = type  # 如果你使用python 2，请包涵这行代码

class Person:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))

foo = Person()
bar = Person()
foo.set_name("Luke Skywalker")
bar.set_name("Anakin Skywalker")
foo.greet()  # Hello, world! I'm Luke Skywalker.
bar.greet()  # Hello, world! I'm Anakin Skywalker.
print(foo.name)  # Luke Skywalker
print(bar.name)  # Anakin Skywalker


print("--------属性、函数、方法--------")
class Class:
    def method(self):
        print("I have a self!")
def function():
    print("I don't...")
instance = Class()
instance.method()  # I have a self!
instance.method = function
instance.method()  # I don't...


print("-----另一个变量指向同一个方法-----")
class Bird:
    song = "Squaawk!"
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()  #
birdsong = bird.sing
birdsong()


print("---------- 私有属性，让名称已两个下划线打头 ----------")
class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me...")
    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()

sec = Secretive()
# 外部访问会报错
# sec.__inaccessible()  #  'Secretive' object has no attribute '__inaccessible'
sec.accessible()

# 奇异的访问
sec._Secretive__inaccessible()  # Bet you can't see me...


print("---------------- 类的命名空间 --------------")
class C:
    print("Class C being defined...")

# 只定以了类，但是没有定义实例，也会输出一行语句.


class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1

m1 = MemberCounter()
m1.init()
print(MemberCounter.members)  # 1
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)  # 2

m1.members = 'Two'
print(m1.members)  # Two
print(m2.members)  # 2


print("----------- 指定超类 ---------")
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

# 在Class语句中的类名后加上超类名，并用圆括号括起
class SPAMFilter(Filter):  # SPAMFilter是Filter的子类
    def init(self):  # 重写超类Filter的方法init
        self.blocked = ['SPAM']

f = Filter()
f.init()
ret1 = f.filter([1, 2, 3])
print(ret1)  # [1, 2, 3]

s = SPAMFilter()
s.init()
ret2 = s.filter(["SPAM", "SPAM", "SPAM", "egg", "SPAM", "bacon", "SPAM", "SPAM"])
print(ret2)  # ['egg', 'bacon']


print("-------深入探讨 继承 -----------")
print("------ issubclass() ------")
print(issubclass(SPAMFilter, Filter))  # True
print(issubclass(Filter, SPAMFilter))  # False

print("------类的基类 __bases__ -------")
ret1 = SPAMFilter.__bases__
ret2 = Filter.__bases__
print(ret1)  # (<class '__main__.Filter'>,)
print(ret2)  # (<class 'object'>,)


print("-------对象是否是特定类的实例 isinstance ------")
ret1 = isinstance(s, SPAMFilter)
ret2 = isinstance(s, Filter)
ret3 = isinstance(s, str)
ret4 = isinstance(f, SPAMFilter)
print(ret1)  # True
print(ret2)  # True
print(ret3)  # False
print(ret4)  # False


print("------对象属于哪个类 __class__ 属性-------")
ret5 = s.__class__
ret6 = f.__class__
print(ret5)  # <class '__main__.SPAMFilter'>
print(ret6)  # <class '__main__.Filter'>

print("------ type(s) 获悉对象所属的类---------")
ret7 = type(s)
print(ret7)  # <class '__main__.SPAMFilter'>


print("============= 多个 超 类 =============")
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print("Hi, my value is ", self.value)

class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk()  # Hi, my value is  7



print("============== 接口和内省 ===============")
print("------- hasattr() -------")
ret1 = hasattr(tc, 'talk')
ret2 = hasattr(tc, 'fnord')
print(ret1)  # True
print(ret2)  # False

print("-------对返回的对象调用 callable(), getattr()指定默认参数 ")
ret3 = callable(getattr(tc, 'talk', None))
ret4 = callable(getattr(tc, 'fnord', None))
print(ret3)  # True
print(ret4)  # False

print("------ setattr() 设置对象的属性---------")
setattr(tc, 'name', "Mr. Gumby")
print(tc.name)  # Mr. Gumby

print("------- __dict__属性，查看对象中存储的所有值 ----")
print(tc.__dict__)  # {'value': 7, 'name': 'Mr. Gumby'}

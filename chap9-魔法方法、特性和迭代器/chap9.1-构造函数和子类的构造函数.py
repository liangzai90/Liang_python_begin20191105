__metaclass__ = type  # python 2.x 旧版本需要声明这个

print("------------- 构造函数 ------------")
class FooBar:
    def __init__(self):
        self.somevar = 42

f = FooBar()
print(f.somevar)

class FooBar2:
    def __init__(self, value=42):
        self.somevar = value

f2 = FooBar2("This is a constructor argument.")
print(f2.somevar)

print("__inin__()构造函数， __del__()析构函数")

print("-------重写普通方法和特殊的构造函数-------")
class A:
    def hello(self):
        print("Hello, I'm A")

class B(A):
    def hello(self):
        print("Hello, I'm B")

b = B()
b.hello()  # Hello, I'm B

print("---------Bird类--------------")
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Aaaah ...")
            self.hungry = False
        else:
            print("No, thanks!")
b = Bird()
b.eat()
b.eat()  # 进食后就不再饥饿了

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = "Squawk!"
    def sing(self):
        print(self.sound)
sb = SongBird()
sb.sing()
sb.eat()
print("----调用未关联的超类构造函数。在子类代码中添加超类的构造函数 Bird.__init__(self) -----")
# 通过这个未关联方法的self参数设置当前实例，将使用超类的构造函数来初始化SongBird对象。这意味着将设置其属性hungry。

print("python3.子类构造函数中如此调用 super().__init__()")
class NewSongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = "NEW_Squawk!"
    def sing(self):
        print(self.sound)

nsb = NewSongBird()
nsb.sing()  # NEW_Squawk!

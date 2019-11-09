print("--------- 抽象基类 -----------")
from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

class Knigget(Talker):
    def talk(self):
        print("Ni!")

k = Knigget()
ret1 = isinstance(k, Talker)
k.talk()  # Ni!
print(ret1)  # True

print("--------- 注册 类 ---------")
class Herring:
    def talk(self):
        print("Blub.")

class Clam:
    pass

Talker.register(Herring)
Talker.register(Clam)

h = Herring()
c = Clam()
ret1 = isinstance(h, Talker)
ret2 = issubclass(Herring, Talker)
ret3 = isinstance(c, Talker)
ret4 = issubclass(Clam, Talker)
print(ret1)  # True
print(ret2)  # True
print(ret3)  # True
print(ret4)  # True

# 注册过来的类，没有继承 抽象基类的抽象方法
# c.talk()  # 'Clam' object has no attribute 'talk'

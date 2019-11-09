
print("-------- __getattr__, __setattr__ ---------")
"""
__getattribute__(self, name)
__getattr__(self ,name)
__setattr__(self, name, value)
__delattr__(self, name)
"""
class Rectangele:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, key, value):
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value
    def __getattr__(self, item):
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError()

rt2 = Rectangele()
rt2.width = 10
rt2.height = 20



print("----------- 迭代器 ----------")
print("------找出 第一个 大于1000 的斐波拉契数-----")
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)  # 1597
        break

it = iter([1, 3, 66, 77])
print(next(it))  # 1
print(next(it))  # 3
print(next(it))  # 66
print(next(it))  # 777
# print(next(it))  # 越界会触发这个异常 StopIteration



print("---------从 迭代器 创建序列 ---------")
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti = TestIterator()
print(list(ti))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

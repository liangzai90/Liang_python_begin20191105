print("----------从 list, dict, str 派生-----------")
print("-------一个带访问计数器的列表-------")
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

cl = CounterList(range(10))
print(cl)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cl.reverse()
print(cl)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

del cl[3:6]
print(cl)  # [9, 8, 7, 3, 2, 1, 0]

print(cl.counter)  # 0
cl[4] + cl[2]
print(cl.counter)  # 2


print("---------- 封装 状态变量 --------------")
class Rectange:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height

rt = Rectange()
rt.width = 10
rt.height = 5
print(rt.get_size())  # (10, 5)
# 这里传入一个元组
rt.set_size((150, 100))
print(rt.width)  # 150



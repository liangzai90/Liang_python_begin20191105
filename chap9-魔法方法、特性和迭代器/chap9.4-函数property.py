print("------- 函数 property --------")
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)
rt1 = Rectangle()
rt1.width = 10
rt1.height = 5
print(rt1.size)  # (10, 5)
rt1.size = 150, 100  # 这里像使用属性一样在调用函数
print(rt1.width)  # 150

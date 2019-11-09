print("-----基本的序列和映射协议------")
"""
__len__(self)

__getitem__(self, key)

__setitem__(self, key, value)

__delitem__(self, key)

"""



def check_index(key):
    """
    指定的键是否是可接受的索引？
    键必须是非负整数，才是可接受的。
    如果不是整数，将引发TypeError异常；
    如果是负数，将引发IndexError异常（因为这个序列的长度是无穷的）
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError

print("---------- 创建一个 无穷序列 -----------")
class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        初始化这个算数序列
        start  序列中的第一个值
        step  两个相邻值的差
        changed  一个字典，包含用户修改后的值
        """
        self.start = start  # 存储起始值
        self.step = step  # 存储步长值
        self.changed = {}  # 没有任何元素被修改

    def __getitem__(self, key):
        """
        从算术序列中获取一个元素
        """
        check_index(key)

        try:
            return self.changed[key]  # 修改过？
        except KeyError:
            return self.start + key * self.step  # 如果没有修改过，就计算元素的值

    def __setitem__(self, key, value):
        """
        修改算术序列中的元素
        """
        check_index(key)
        self.changed[key] = value  # 存储修改后的值

s = ArithmeticSequence(1, 2)
for i in range(10):
    print(s[i])
# print(s[0])

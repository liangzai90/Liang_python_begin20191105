print("----------- 阶乘 和 幂 ----------")

print("-------计算阶乘 n*(n-1)*...*3*2*1------")
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
ret1 = factorial(5)
print(ret1)  # 120

print("-------递归实现 阶乘------")
def factorial_dg(n):
    if n == 1:
        return 1
    else:
        return n * factorial_dg(n-1)
ret2 = factorial_dg(5)
print(ret2)  # 120


print("--------------计算 幂----------------")
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

def power_dg(x, n):
    if n == 0:
        return 1
    else:
        return x * power_dg(x, n-1)


print("------------ 二 分 查 找 . 模块bitsect提供了标准的二分查找 -----------------")
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper)//2
        print("-------else-----")
        print(number)
        print(sequence[middle])
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)  # [4, 8, 34, 67, 95, 100, 123]
ret1 = search(seq, 34)
print(ret1)  # 2


print("----------- 函数式编程 map,filter,reduce-----------")
print("------ map -------")
ret1 = list(map(str, range(10)))
ret2 = [str(i) for i in range(10)]
print(ret1)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(ret2)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("------ filter 根据布尔函数返回值对元素进行过滤 -------")
def func(x):
    return x.isalnum()
seq = ["foo", "x41", "?!", "***"]
ret3 = list(filter(func, seq))
print(ret3)  # ['foo', 'x41']
# 使用列表推导
ret4 = [x for x in seq if x.isalnum()]
print(ret4)  # ['foo', 'x41']

ret5 = list(filter(lambda x: x.isalnum(), seq))
print(ret5)  # ['foo', 'x41']


print("------ reduce -------")
print("-----将序列中的所有数相加-----")
numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
ret6 = reduce(lambda x, y: x+y, numbers)
print(ret6)  # 1161

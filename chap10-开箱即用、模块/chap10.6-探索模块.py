import pprint
import copy

print("=================== 探索模块 ================")


print("------- dir() 列出对象所有属性（对于模块，它列出所有的函数、类、变量等）--------------")
# dir()
pprint.pprint(dir(copy))
print("------列表推导，过滤有‘_'的字符-----")
ret1 = [n for n in dir(copy) if not n.startswith('_')]
print(ret1)  # ['Error', 'copy', 'deepcopy', 'dispatch_table', 'error']


print("-------变量__all__ 定义模块的公共接口-------")
# 以下划线开头的函数和变量，不在__all__ 里面
print(copy.__all__)  # ['Error', 'copy', 'deepcopy']


print("------- help() ---------")
help(copy.copy)
print(copy.copy.__doc__)
# help(copy)

print("--------文档是模块信息的来源---------")
print(range.__doc__)
"""
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
"""

print("----- __file__ 查看源码----")
print(copy.__file__)



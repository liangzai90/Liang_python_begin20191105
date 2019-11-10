print("-------集合、堆、双端队列------")
print("--------集合 内置类 set -------")
set1 = set(range(10))
print(set1)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print("------ 集合set没有重复元素，元素排列顺序是不确定的 ------")
set2 = {0, 1, 2, 3, 4, 1, 2, 3}
print(set2)  # {0, 1, 2, 3, 4}

set3 = {"fee", "file", "foe"}
print(set3)  # {'file', 'fee', 'foe'}

a = {1, 2, 3}
b = {3, 4, 2, 5}
print("-------- | -----------")
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
print(a)  # {1, 2, 3}
print(b)  # {2, 3, 4, 5}

c = a & b
print(c)  # {2, 3}
print("-------- <= -----------")
print(c.issubset(a))  # True
print(c <= a)  # True
print("--------- >= ----------")
print(c.issuperset(a))  # False
print(c >= a)  # False
print("-------- & -----------")
print(a.intersection(b))  #{2, 3}
print(a&b)  # {2, 3}
print("-------- - -----------")
print(a.difference(b))  # {1}
print(a - b)  # {1}
print("-------- ^ -----------")
print(a.symmetric_difference(b))  # {1, 4, 5}
print(a ^ b)  # {1, 4, 5}

print("-------------------")
print(a.copy())  # {1, 2, 3}
print(a.copy() is a)  # False


my_test = []
for i in range(10):
    my_test.append(set(range(i, i+5)))
#print(my_test)
#print(reduce(set.union, my_test))

a1 = {1, 2, 3}
b1 = {3, 4, 5}
print(a1.add(frozenset(b1)))  # None
print(a1)  # {1, 2, 3, frozenset({3, 4, 5})}
print(b1)  # {3, 4, 5}



print("--------------- 堆 heapq 模块 --------------")
"""
# heappush(heap, x)  将x压入堆中
# heappop(heap)  从堆中弹出最小的元素
# heapify(heap)  让列表具备堆特征
# heapreplace(heap, x)  弹出最小的元素，并将x压入堆中
# nlargest(n, iter)  返回iter中n个最大的元素
# nsmallest(n, iter)  返回iter中n个最小的元素
"""

from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)

print("------- 默认 创建的是 小顶堆 -----")
print(heap)  # [0, 1, 3, 4, 2, 9, 5, 8, 6, 7]
heappush(heap, 0.5)
print(heap)  # [0, 0.5, 1, 6, 3, 2, 5, 9, 8, 7, 4]
print(heappop(heap))  # 0
print(heappop(heap))  # 0.5
print(heappop(heap))  # 1
print(heappop(heap))  # 2

print("------ heapify()调整堆")
heap2 = [10, 4,5,6,7,8,9,1, 2, 3]
print(heap2)
heapify(heap2)  # [10, 4, 5, 6, 7, 8, 9, 1, 2, 3]
print(heap2)  # [1, 2, 5, 4, 3, 8, 9, 6, 10, 7]

# 弹出最小元素，压入新元素
ret2 = heapreplace(heap2, 1.5)
print(ret2)  # 1
print(heap2)  # [1.5, 2, 5, 4, 3, 8, 9, 6, 10, 7]


print("-------- 双端队列 deque 模块 ---------")
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)  # deque([6, 0, 1, 2, 3, 4, 5])

ret1 = q.pop()
print(ret1)  # 5
print(q)  # deque([6, 0, 1, 2, 3, 4])

ret2 = q.popleft()
print(ret2)  # 6
print(q)  # deque([0, 1, 2, 3, 4])

# Rotate the deque n steps to the right (default n=1)
q.rotate(3)
print(q)  # deque([2, 3, 4, 0, 1])

q.rotate(-1)
print(q)  # deque([3, 4, 0, 1, 2])
print(deque.rotate.__doc__)


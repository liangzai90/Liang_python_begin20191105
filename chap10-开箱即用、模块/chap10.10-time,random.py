print("-------------- time 模块 ---------------")
"""
asctime(tupple)
localtime([secs])
mktime(tuple)
sleep(secs)
strptime(string[, format])
time()
"""

import time
print(time.asctime())  # 'Sun Nov 10 12:24:33 2019'
print(time.time())  # 1573360258.3418133
print(time.localtime(1234567890))  # time.struct_time(tm_year=2009, tm_mon=2, tm_mday=14, tm_hour=7, tm_min=31, tm_sec=30, tm_wday=5, tm_yday=45, tm_isdst=0)
print(time.mktime((2019, 2, 3, 4, 5, 6, 7, 8, 9)))  #
print(time.strptime(time.asctime()))  # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=10, tm_hour=12, tm_min=33, tm_sec=52, tm_wday=6, tm_yday=314, tm_isdst=-1)
# time.sleep(5)
print("--------wake up--------")




print("------------ random 模块 -------------")
"""
random()  返回一个0~1（含）的随机实验数
getrandbits(n)  以长整数方式返回n个随机的二进制位
uniform(a,b)  返回一个a~b（含）的随机实数
randrange([start], stop, [step])  从range(start, stop, step)中随机地选择一个数
choice(seq)  从序列seq中随机地选择一个元素
shuffle(seq[, random])  就地打乱序列seq
sample(seq, n)  从序列seq中随机地选择n个值不同的元素
"""
import random
print(random.random())  # 0.3184695273325854
print(random.uniform(1, 5))  # 2.8829951657673627
print(random.randrange(1, 10))  # 2
print(random.choice([1, 2, 3, 4, 5]))  # 4
print(random.shuffle([1, 2, 3, 4, 5, 6]))  # None
print(random.sample([1, 2, 3, 4, 5, 6], 2))  # [3, 1]

print("--------------")
from random import *
from time import *
date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
random_time = uniform(time1, time2)
print(random_time)  # 1471427897.0693026
print(asctime(localtime(random_time)))  # Sat Jan  2 11:32:32 2016
timeA = time()
sleep(3)
timeB = time()
print(timeB - timeA)  # 3.0000641345977783


print("---------掷骰子---------")
from random import randrange
num = int(input("How many dice? "))
sides = int(input("How many sides per die? "))
sum = 0
for i in range(num): sum += randrange(sides)+1
print("The result is ", sum)

"""
# 需要单独定义为外部模块，并执行  python test2.py abc.txt
# test2.py 模块内容  ---------将随机运气写入一个文本文件-------- 一个 fileinput操作文件的实例
import fileinput, random
fortunes = list(fileinput.input())
print(random.choice(fortunes))
"""

print("---------- 打印 一副牌 ----------------")
values = list(range(1, 11)) + "Jack Queen King".split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['{} of {}'.format(v, s) for v in values for s in suits]
from pprint import pprint
pprint(deck[:12])
from random import shuffle
shuffle(deck)  # 随机洗牌
pprint(deck[:12])

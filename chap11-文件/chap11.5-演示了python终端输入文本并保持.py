
# 这是在python终端操作的情况
>>> f =open("abc.txt", "w")
>>> print("first", "line", file=f)
>>> print("second", "line", file=f)
>>> f.close()
>>> lines = list(open("abc.txt"))
>>> lines
['first line\n', 'second line\n']
>>> first, second, third = open('abc.txt')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    first, second, third = open('abc.txt')
ValueError: not enough values to unpack (expected 3, got 2)
>>> first, second = open('abc.txt')
>>> first
'first line\n'
>>> second
'second line\n'
>>>

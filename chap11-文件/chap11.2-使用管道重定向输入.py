import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print("Word count:", wordcount)

"""
-----使用管道重定向输出，注意，在Linux下面运行的时候，不能有中文出现，否则会报错
在Linux下面执行的情况

[heliang@localhost python]$  cat test.txt | python chap11_2.py | sort 
('Word count:', 2)
"""

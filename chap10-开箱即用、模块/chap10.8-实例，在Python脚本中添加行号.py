print("-----------在Python脚本中添加行号 ------------")

import fileinput

for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50}#{:2d}'.format(line, num))

#外部有一个文本文件 test.py，给test.py后面添加行号
# python  chap10_8.py test.py
# 添加后的效果如下图
"""
# test.py                                         # 1
# second line                                     # 2
print("hello, world!"                             # 3
                                                  # 4
                                                  # 5
print("end line")                                 # 6
# 20191110                                        # 7

"""

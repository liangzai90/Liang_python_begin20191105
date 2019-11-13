print("------- 一个使用 doctest 的简单测试 --------")
print("请注意，这里的语法要求特别的严格 >>> 后面需要跟1个空格")
print("需要在cmd命令窗口，运行 python  my_math.py  -v ")
def square(x):
    '''
    计算平方并返回结果
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x ** x

if __name__ == '__main__':
    import doctest, my_math
    doctest.testmod(my_math)

# 需要在cmd命令窗口，运行 python  my_math.py  -v 
# 有关模块 doctest 的详细信息，请参阅 Python库参考手册

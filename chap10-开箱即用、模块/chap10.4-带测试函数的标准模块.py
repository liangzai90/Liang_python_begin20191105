# chap10_4.py

def hello4():
    print("Hello4, world!")

# python的测试函数（用来做各种单元测试）
def test():
    hello4()


# 区分模块是导入还是测试..
if __name__ == '__main__': test()

# 每个模块的 __name__属性不同，可以在命令窗口输入下面的命令查看
# __name__
# chap10_4.__name__

print("------ 生 成 器 -------")

nested = [[1, 2], [3, 4], [5]]
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

print("--- 包含 yield 语句的函数都被称为【生成器】---")
for num in flatten(nested):
    print(num)


print(list(flatten(nested)))  # [1, 2, 3, 4, 5]


print("--------生成器推导（也叫生成器表达式）---------")
g = ((i + 2)**2 for i in range(1, 10))
# print(list(g))  # [9, 16, 25, 36, 49, 64, 81, 100, 121]
print(next(g))  # 9
print(next(g))  # 16
print(list(g))  # [25, 36, 49, 64, 81, 100, 121]
print(list(g))  # []

ret = sum(i ** 2 for i in range(5))
print(ret)  # 30


print("---------- 递归式 生成器 -----------")
print("----- 处理 任意层 嵌套的列表 -----")
def flatten(nested):
    try:
        # 不迭代类似于字符串的对象
        try: nested + ''
        except TypeError:pass
        else:
            print("字符串在这里会产生异常，异常会跳出到外层A")
            raise TypeError

        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        print("跳出的异常在这里被捕获B")
        yield nested

ret = list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
print(ret)  # [1, 2, 3, 4, 5, 6, 7, 8]

ret2 = list(flatten(["foo", ["bar", ["Baz"]]]))
print(ret2)  # ['foo', 'bar', 'Baz']


print("------- 生成器的方法 next,send,throw,close-------")
def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

rt = repeater(42)
print(next(rt))
print(next(rt))
print(rt.send("Hello, world!"))  # Hello, world!
print(next(rt))  # Hello, world!



print("--------- 模拟 生成器C --------")
def normal_flatten(nested):
    result = []
    try:
        # 不迭代类似于字符串的对象
        try: nested + ""
        except TypeError: pass
        else:
            print("custom yield")
            raise TypeError
        for sublist in nested:
            for element in normal_flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result

rt3 = list(normal_flatten(["abc", ["def", ["ghk"]]]))
print(rt3)  # ['abc', 'def', 'ghk']


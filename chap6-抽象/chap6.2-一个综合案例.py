print("------------一个综合案例---------------")

# 这里的参数是字典，所以需要用 format_map,否则会报错
def story(**kwds):
    return "Once upon a time, there was a " "{job} called {name}.".format_map(kwds)

def power(x, y, *others):
    if others:
        print("Received redundant parameters:", others)
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start  # 如果没有给参数stop指定值，就调整参数start 和 stop 的值
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print(story(job="King", name="Gumby"))  # Once upon a time, there was a King called Gumby.
print(story(name="Sir Robin", job="brave knight"))  # Once upon a time, there was a brave knight called Sir Robin.

params = {'job': 'language', 'name': 'Python'}
print(story(**params))  # Once upon a time, there was a language called Python.

del params["job"]
print(story(job='stroke of genius', **params))  # Once upon a time, there was a stroke of genius called Python.

print(power(2, 3))  # 8
print(power(3, 2))  # 9
print(power(y=3, x=2))  # 8
params = (5,)*2
print(params)  # (5, 5)
print(power(*params))  # 3125
print(power(3, 3, "Hello, world!"))

ret1 = interval(10)
print(ret1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ret2 = interval(1, 5)
print(ret2)  # [1, 2, 3, 4]

ret3 = interval(3, 13, 4)
print(ret3)  # [3, 7, 11]

ret4 = power(*interval(3, 7))
print(ret4)



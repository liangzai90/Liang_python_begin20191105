print("-------- finally ----------")
x = None
try:
    x = 1 / 0
finally:
    print("Cleaning up ...")
    del x



print("-------检查某个对象是否可写------------")
obj = None
try:
    obj.write
except AttributeError:
    print("The object is not writeable")
else:
    print("The object is writeable ")

print("--------- warnings模块----------")
print("-----------warn 发出警告，多次运行也只警告一次")
from warnings import warn
warn("I've got a bad feeling aboug this.")
print("Hello second!")


print("------抑制发出的警告 filterwarnings [ignore, error]-------")
from warnings import filterwarnings
filterwarnings("ignore")
warn("Anyone out there?")

filterwarnings("error")
warn("Something is very wrong!")  # UserWarning: Something is very wrong!
print("hello,third")  # 没有执行


print("-------根据异常过滤特定类型的警告----------")
filterwarnings("error")
warn("This function is really old ...", DeprecationWarning)

filterwarnings("ignore", category=DeprecationWarning)
warn("Another deprecation warning.", DeprecationWarning)  # 这个警告被过滤掉了
warn("Something else.")

print("----------end----------")


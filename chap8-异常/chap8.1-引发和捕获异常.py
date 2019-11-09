print("--------用 raise 语句 引发异常---------")

# raise Exception("何亮到此一游")

"""
>>> raise Exception("何亮到此一游")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    raise Exception("何亮到此一游")
Exception: 何亮到此一游


>>> raise ArithmeticError("AAAAAAAAAAAAA")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    raise ArithmeticError("AAAAAAAAAAAAA")
ArithmeticError: AAAAAAAAAAAAA

"""




print("------自定义异常类------")
class SomeCustomException(Exception):pass

print("--------- 捕获异常 try/except  多个 except --------")
try:
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")
except TypeError:
    print("That wan't a number, was it?")


print("---------抑制异常，不继续向上传播--------")
class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise

calculator = MuffledCalculator()
ret1 = calculator.calc('10 / 2')
print(ret1)  # 5.0
# 关闭了抑制功能
# ret2 = calculator.calc('10 / 0')

# 开启抑制功能
calculator.muffled = True
ret3 = calculator.calc('10 / 0')
print(ret3)  # None



print("-------异常上下文------")
try:
    1/0
except ZeroDivisionError:
    raise ValueError from None


print("--------元组中定义多个异常---------")
try:
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    print(x / y)
except (ZeroDivisionError, TypeError, NameError):
    print("Your numbers were bogus ...")



print("--------捕获异常---------")
try:
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
    print(x / y)
except (ZeroDivisionError, TypeError, NameError) as e:
    print(e)

print("------------------ 作用域 vars() -----------------")
x = 1
scope = vars()
print(scope['x'])  # 1


def combine(parameter):
    print(parameter + external)
external = "AAAA"
combine("YOU")  # YOUAAAA

print("------globals() 解决全局变量被局部变量 【遮盖】 问题-----")
def combine_2(parameter):
    print(parameter + globals()['parameter'])
parameter = "BBB"
combine_2("Day Day UP --> ")  # Day Day UP --> BBB

print("------- 重新关联全局变量 --------")
var_x = 1
def change_global():
    global var_x
    var_x = var_x + 1

change_global()
print(var_x)  # 2


print("------------- 作用域 嵌套 ------------------")
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor

double = multiplier(2)
ret1 = double(5)
print(ret1)  # 10

triple = multiplier(3)
ret2 = triple(3)
print(ret2)  # 9

print("-------- 像multiplyByFactor这样，存储其所在作用域的函数称为【闭包】-------")
ret3 = multiplier(5)(4)
print(ret3)  # 20

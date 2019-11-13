print("对某个模块的某个函数的性能进行检查")
import cProfile
from my_math2 import product
print(cProfile.run("product(1,2)"))


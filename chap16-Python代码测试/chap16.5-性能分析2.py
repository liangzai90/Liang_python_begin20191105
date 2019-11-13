import cProfile
import pstats
from my_math2 import product

# 通过第2个参数向run提供一个文件名为（如my_math2.profile），分析结果将保存到这个文件中。
# 然后使用 pstats模块来研究。通过使用Stats对象，可以编程方式研究分析结果。有关这个API的详情，请参考标准库文档。

cProfile.run("product(1,2)", 'my_math2.profile')
p = pstats.Stats('my_math2.profile')

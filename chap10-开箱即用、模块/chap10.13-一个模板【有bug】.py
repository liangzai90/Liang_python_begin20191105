print('----------模板系统示例--------')
import fileinput, re

# 与使用方括号括起来的字段匹配
field_pat = re.compile(r'\[(.+?)\]')

# 我们将把变量收集到这里
scope = {}

# 用于调试 re.sub
def replacement(match):
    code = match.group(1)
    try:
        # 如果字段为表达式，就返回其结果
        return str(eval(code, scope))
    except SyntaxError:
        # 否则在当前作用域内执行该赋值语句
        # 并返回一个空字符串
        print("----SyntaxError----")
        return ''

# 获取所有文本并合并成一个字符串
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

# 替换所有与字段模式匹配的内容
print(field_pat.sub(replacement, text))

# 定义一个用于匹配字段的模式
# 创建一个用作模板作用域的字典
# 定义一个替换函数
# 使用fileinput读取所有的行
# 调用re.sub来使用替换函数来体会所有与模式field_pat匹配的字段

print("------------end-----------")

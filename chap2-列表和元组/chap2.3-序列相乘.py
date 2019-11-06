# 序列相加
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
print("Hello, " + "world!")  # Hello, world!

# 序列相乘
print("python" * 5)  # 'pythonpythonpythonpythonpython'

x = [42] * 5
print(x)  # [42, 42, 42, 42, 42]

# 空列表是使用不包含任何内容的两个方括号（[]）表示的。
# 在Python中，None表示什么都没有。
sequence = [None] * 10
print(sequence)  # [None, None, None, None, None, None, None, None, None, None]


# 序列（字符串）乘法运算示例
# 在位于屏幕中央且宽度合适的方框内打印一个句子
sentence = input("Sentence: ")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+' + '-'*(box_width-2) + '+')
print(' ' * left_margin + '|  ' + ' '*text_width + '  |')
print(' ' * left_margin + '|  ' + sentence + '  |')
print(' ' * left_margin + '|  ' + ' '*text_width + '  |')
print(' ' * left_margin + '+' + '-'*(box_width-2) + '+')
print()


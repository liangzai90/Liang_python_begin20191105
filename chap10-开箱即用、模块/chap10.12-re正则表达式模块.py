print("---------- re 正则表达式 ----------------")
"""
参考官方的正则表达式文档介绍
https://docs.python.org/2/howto/regex.html

r'(http://)?(www\.)?python\.org'

只与下面这些字符串匹配：
'http://www.python.org'
'http://python.org'
'www.python.org'
'python.org'
"""

"""
compile(pattern[, flags])  根据包含正则表达式的字符串创建模式对象
search(pattern, string[, flags])  在字符串中查找模式
match(pattern, string[, flags])  在字符串开头匹配模式
split(pattern, string[, maxsplit=0])  根据模式来分割字符串
findall(pattern, string)  返回一个列表，其中包含字符串中所有与模式匹配的子串
sub(pat, repl, string[, count=0])  将字符串中与模式pat匹配的子串都替换为 repl
escape(string)  对字符串中所有的正则表达式特殊字符都进行转义
"""

import re
some_text = "alpha, beta, ,,, gamama  delta"
ret = re.split('[, ]+', some_text)
print(ret)  # ['alpha', 'beta', 'gamama', 'delta']
# 最多分割2次
ret2 = re.split('[, ]+', some_text, maxsplit=2)
print(ret2)  # ['alpha', 'beta', 'gamama  delta']

ret3 = re.split('[, ]+', some_text, maxsplit=1)
print(ret3)  # ['alpha', 'beta, ,,, gamama  delta']
# 如果模式包含圆括号，将在分割得到的子串之间插入括号中的内容
print(re.split('o(o)', "fooobar"))  # ['f', 'o', 'obar']

print("------找出字符串中包含的所有单词-----")
pat = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
ret4 = re.findall(pat, text)
print(ret4)  # ['Hm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']

print("-----查找所有的标点符号-----")
pat = r'[.?\-",]+'
ret5 = re.findall(pat, text)
print(ret5)  # ['"', '...', '--', '?"', ',', '.']


print("----- re.sub 从左往右将与模式匹配的子串替换为指定内容-----")
pat = '{name}'
text = 'Dear {name}...'
ret6 = re.sub(pat, 'Mr. Gumby', text)
print(ret6)  # Dear Mr. Gumby...

ret7 = re.escape('www.python.org')
print(ret7)  # 'www\\.python\\.org'

ret8 = re.escape('But where is the ambiguit?')
print(ret8)  # 'But\\ where\\ is\\ the\\ ambiguit\\?'


print("-------- 匹配对象和编组 --------")
m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
print(m.group(1))  # python
print(m.start(1))  # 4
print(m.end(1))  # 10
print(m.span(1))  # (4, 10)

print("------替换中的组号和函数-------")
emphasis_pattern1 = r'\*([^\*]+)\*'

print("--------- VERBOSE 标志 -----------")
emphasis_pattern2 = re.compile(r'''
    \*          # 起始突出标志--一个星号
    (           # 与要突出的内容匹配的编组的起始位置
    [^\*]+      # 与除星号外的其他字符都匹配
    )           # 编组到此结束
    \*          # 结束突出标志
            ''', re.VERBOSE)

print("---将纯文本替换为了 html ----")
print(re.sub(emphasis_pattern2, r'<em>\1</em>', 'Hello, *world*!'))
# Hello, <em>world</em>!


print('-------贪婪和非贪婪模式-----')
print("-------贪婪版本，匹配第一个和最后一个*之间的所有内容 + ------")
emphasis_pattern3 = r'\*(.+)\*'
print(re.sub(emphasis_pattern3, r'<em>\1<em>', "*This* is *it*!"))
# <em>This* is *it<em>!

print("-----重复运算符的非贪婪版本 加问号 +? ------")
emphasis_pattern4 = r'\*\*(.+?)\*\*'
print(re.sub(emphasis_pattern4, r'<em>\1</em>', '**This** is **it**!'))
# <em>This</em> is <em>it</em>!


print("--------找出发件人 From打头，包含在<>内的邮件地址结尾--------")
# find_sender.py
import fileinput, re
pat = re.compile('From:(.*)<.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m: print(m.group(1))

# 在外部调用python命令指向脚本文件，解析邮件内容
# python find_sender.py  message.eml



print("-------列出所有发件人地址-------")
import fileinput, re
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
address = set()
for line in fileinput.input():
    for address in pat.findall(line):
        address.add(address)

for address in sorted(address):
    print(address)

#  https://docs.python.org/2/howto/regex.html


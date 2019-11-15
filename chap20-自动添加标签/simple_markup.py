# -*- coding: utf-8 -*-
# print("一个简单的标记程序")

import sys, re
import util
print('<html><head><title>...</title><body>')

title = True
for block in util.blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')


"""
下载 Cygwin，然后切换到当前目录下面，执行下面的命令
python simple_markup.py  < test_input.txt > output.html
这会自动生成一个 output.html网页格式的文档
"""

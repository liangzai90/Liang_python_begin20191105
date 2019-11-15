# 第20章  小结

### 1.项目中用到的正则表达式

分别用来找出【要突出的内容】、【URL】、【Email】 :octocat:

```
 r'\*(.+?)\*'
 r'(http://[\.a-zA-Z/]+)'
 r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)'
```

### 2.通过stdin输入文本字符   :earth_asia:

目前，在windows运行脚本，没有得到期望的结果。不知道如何在windows的cmd窗口执行这中带文本参数的命令。

我在电脑上安装了 Cygwin，然后执行了 **带参数的Python命令** ，是可以正常执行的。

```
python  markup.py  < test_input.txt >  output.html 
```

### 3.存在的问题 :cold_sweat: :joy: :broken_heart: :muscle:

虽然生成了 output.html，但是里面的文本重复了3次。

可能是程序哪里有bug了。后期需要跟踪调试。Python下面跟踪调试也是挺麻烦的。

特别是这个程序嵌套的比较厉害。

### 5.进一步探索  :100:

这个程序存在潜在的扩展空间。 :bicyclist: :gem: :memo:  :simple_smile:

- [ ] 增加对表格的支持。为此，只需找出左对齐内容的边界，并将文本块分成多列。

- [ ] 突出全部大写的单词。为此，需要考虑缩略语、标点、姓名和其他首字母大写的单词。

- [ ] 支持LATEX格式的输出。

- [ ] 编写一个执行其他处理（而不是添加标记）的处理程序，如以某种方式对文档进行分析。

- [ ] 创建一个脚本，将特定目录中的所有文本文件都自动转换为HTML文件。

- [ ] 了解其他纯文本格式，如Markdown、reStructuredText或维基百科使用的格式。

### other topic

[if you want to know more about emoji, click me!](https://www.webfx.com/tools/emoji-cheat-sheet/)



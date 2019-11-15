# 第21章 小结

### 1.本章介绍如何使用Python创建图表。具体地说，你将创建一个PDF文件。

使用到的第三方工具是 ReportLab，这个网站是需要注册的。其它图形包还有PYX([https://pyx-project.org/](https://pyx-project.org/))。


**要想深入学习，需要研究一下这些模块都有哪些函数，功能是什么，要深入源码，研究源码。**

```Python console
>>> import reportlab
>>> reportlab.__file__
'C:\\Users\\heliang\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\reportlab\\__init__.py'
>>> 
```
 

### 2.进一步探索

无论是ReportLab、PYX还是很多其他绘图包，都可尝试将自动生成的图形嵌入文档（甚至生成文档的各个部分）。要给文本添加标签，可使用第20章介绍的技巧。
如果要创建PDF文件，可使用ReportLab中的Platypus（也可使用LATEX等排版系统来继承PDF图形）。
如果要创建网页，Python也提供了很多创建像素映射图形（gif, png）的方法----在网上搜索这个主题就能找到相关资料。






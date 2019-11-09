第8章 小结

--------------------------------------------

【异常对象】异常情况是用异常对象表示的。

【引发异常】使用raise语句引发异常。

【自定义的异常类】通过从Exception派生来创建自定义的异常

【捕获异常】try/except 语句捕获。

【else子句】处except子句外，还可使用else子句，在try没有引发异常时执行

【finally】确保代码块（如清理代码）无论是否引发异常都将执行，可使用try/finally，并将代码块放在finally子句中。

【异常和函数】在函数中引发异常时，异常将传播到调用函数的地方

【警告】警告类似于异常，但（通常）只打印一条错误消息。可以指定警告类别，它们是warning的子类

---------------------

新函数

warnings.filterwarnings(action, category=warning, ...)  用于过滤警告

warnings.warn(message, category=None)  用于发出警告

-----------------------------

内置异常类

------------------------------

Exception  几乎所有的异常类都是从它派生而来的

AttributeError  引用属性或给它赋值失败时引发

OSError  操作系统不能执行指定任务（如打开文件）时引发，有多个子类

IndexError  使用序列中不存在的索引时引发，为LookupError的子类

KeyError  使用映射中不存在的键时引发，为LookupError的子类

NameError  找不到名称（变量）时引发

SyntaxError  代码不正确时引发

TypeError  将内置操作或函数用于类型不正确的对象时引发

ValueError  将内置操作或函数用于这样的对象时引发：其类型正确但保护的值不合适

ZeroDivisionError  在出发或求模运算的第二个参数为零时引发


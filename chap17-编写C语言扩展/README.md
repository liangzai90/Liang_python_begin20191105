## 关于编写C语言扩展这部分，请参考这里：[第18章 关于C语言扩展](../chap18-程序打包/chap18.2-编译扩展.md)


### 编写C语言扩展的步骤：

1.安装setuptools工具
```
pip install setuptools
```

2.编写c语言文件

3.编写 .i 接口文件。[请参考官方说明文档](http://www.swig.org/Doc4.0/SWIGDocumentation.html#SWIG_nn9)

一个 palindrome2.i的接口文件示例
```
%module palindrome2

%{
#include <string.h>
%}

extern int is_palindrome2(char *text);
```


4.编写 setup.py脚本，用来编译/打包/安装模块文件

一个setup.py示例：
```
# file name: setup_palindrome2.py

# 编译扩展 setuptools 和 distutils.core 都可以

# from distutils.core import setup, Extension
from setuptools import setup, Extension

palindrome2_module = Extension('_palindrome2',
    sources=['palindrome2.c', 'palindrome2.i',],
)
setup(
    name='palindrome2',
    version='1.5',
    author="HE Liang Liang",
    description= """Simple swig C\+\+/Python example""",
    ext_modules=[palindrome2_module],
    py_modules=["palindrome2"],
)
```

5.测试功能（测试我们编写的模块是否导入成功、以及模块内函数是否可调用）



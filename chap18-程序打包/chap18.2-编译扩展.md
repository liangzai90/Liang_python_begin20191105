## 编译扩展，将C语言编写的函数封装到Python动态库(.pyd文件)，供Python导入模块并调用

#### 1.准备好 palindrome2.c 文件

```
#include <string.h>

int is_palindrome2(char *text) {
    int i, n = strlen(text);
    for (i = 0; i <= n/2; ++i) {
        if (text[i] != text[n-i-1]) return 0;
    }
    return 1;
}

```

#### 2.准备好打包脚本 setup_palindrome2.py 请注意，这里是导入distutils.core模块

```
# file name: setup_palindrome2.py
# 编译扩展.
from distutils.core import setup, Extension

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

#### 3.编写 palindrome2.i 接口文件

[请参考swig官方文档](http://www.swig.org/Doc4.0/SWIGDocumentation.html#SWIG_nn9)

```
%module palindrome2

%{
#include <string.h>
%}

extern int is_palindrome2(char *text);
```


### 4.执行打包命令 

```
python setup_palindrome2.py build
```

### 5.安装模块 

```
python setup_palindrome2.py install
```


如果没有报错，那么目录下面会生成一个build文件夹，下面会有一个.pyd的文件，我这里是_palindrome2.cp38-win32.pyd。
这就是我们生成的Pythong动态库，把它所在路径包含到python目录中，就可以导入模块并调用我们刚才的C函数了。

```
基础知识再回顾一下：

1.将某个模块的路径加入到环境变量

>>> import  sys 
>>> sys.path.append(r"F:\palindrome2\build\lib.win32-3.8")

2.检测C函数封装是否成功

>>> import palindrome2
>>> palindrome2.is_palindrome2("在封装的模块中调用C函数")

```


----------------------------------------------------------------------

## Python的扩展是个重点、打包也是一个重点

这本书里面没有详细将这些。而且也不太严谨。很多例子无法编译通过。

> 1.利用pycharm打包

> 2..pipinstall工具打包

> 3.pypi打包





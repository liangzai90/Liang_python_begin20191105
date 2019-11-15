## 将C语言编写的函数封装，供Python调用

#### 1.准备好 palindrome2.c 文件

```c
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

```python
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

#### 3.编写 palindrome2.i 接口文件

[请参考swig官方文档](http://www.swig.org/Doc4.0/SWIGDocumentation.html#SWIG_nn9)

```shell
%module palindrome2

%{
#include <string.h>
%}

extern int is_palindrome2(char *text);
```


### 4.执行打包命令 

```shell
python setup_palindrome2.py build
```

### 5.安装模块 

```shell
python setup_palindrome2.py install
```

### 6.测试 

打开环境Python GUI 工具，测试模块是否安装、是否可调用

```
如果模块成功安装了，就不会报错
>>> import palindrome2

测试在Python中是否可以调用我们刚才导出的C函数
>>> palindrome2.is_palindrome2("在封装的模块中调用C函数")
```


## 7.如果你只想就地编译扩展（不想install）

```shell
python setup_palindrome4.py build_ext --inplace
```

将会在当前目录下，看到 '_palindrome4.cp38-win32.pyd'， 'palindrome4.py' 这2个文件，
还有palindrome4_wrap.c等等。
把当前的路径添加到环境变量中，
再测试 palindrome4模块是否刻意导入，是否可以调用模块里面的函数。


## 8.基础知识再回顾一下：

```
1.将某个模块的路径加入到环境变量
>>> import  sys 
>>> sys.path.append(r"F:\这里是你本地的那个模块的路径\palindrome2\build\lib.win32-3.8")

2.检测C函数封装是否成功
>>> import palindrome2
>>> palindrome2.is_palindrome2("在封装的模块中调用C函数")

3.若干编译和发布的命令 

执行build和install之后，会在系统里面自动安装你刚才写的模块
python setup.py  build
python setup.py  install

执行sdist命令会发布你的模块
python setup.py  sdist

执行  build_ext  --inplace，可以就地测试模块功能
python setup.py  build_ext  --inplace
```


----------------------------------------------------------------------

## 9.Python的扩展是个重点、打包也是一个重点

这本书里面没有详细将这些。而且也不太严谨。很多例子无法编译通过。

> 1.利用pycharm打包

> 2..pipinstall工具打包

> 3.pypi打包

### 10.一点意外发现
```
编译扩展的时候，setuptools 和 distutils 都可以，只需要像下面这么导入模块

from distutils.core import setup, Extension

from setuptools import setup, Extension

```



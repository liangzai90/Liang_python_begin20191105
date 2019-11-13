## 使用Setuptools实现编译扩展

#### 1.准备好 palindrome2.c 文件

```
#include <string.h>

int is_palindrome(char *text) {
    int i, n = strlen(text);
    for (i = 0; i <= n/2; ++i) {
        if (text[i] != text[n-i-1]) return 0;
    }
    return 1;
}
```

#### 2.准备好打包脚本 setup_palindrome2.py

```
# file name: setup_palindrome2.py
# 编译扩展.
from setuptools import setup, Extension

setup(
    name='palindrome2',
    version='1.0',
    author='He Liang Liang',
    ext_modules = [
        Extension('palindrome2', ['palindrome2.c'])
    ]
)
```

### 3.执行打包命令 

```
python setup_palindrome2.py build_ext --inplace
```
编译出错了。。。卡壳了。。

```

running build_ext
building 'palindrome2' extension
creating build
creating build\temp.win32-3.8
creating build\temp.win32-3.8\Release
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\BIN\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -IC:\Users\heliang\AppData\Local\Programs\Python\Python38-32\include -IC:\Users\heliang\AppData\Local\Programs\Python\Python38-32\include "-IC:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\INCLUDE" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.10240.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\8.1\include\shared" "-IC:\Program Files (x86)\Windows Kits\8.1\include\um" "-IC:\Program Files (x86)\Windows Kits\8.1\include\winrt" /Tcpalindrome2.c /Fobuild\temp.win32-3.8\Release\palindrome2.obj
palindrome2.c
creating F:\003_Project____Python\pycharm_project\PythonBegin_execise\chap18\palindrome2\build\lib.win32-3.8
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\BIN\link.exe /nologo /INCREMENTAL:NO /LTCG /DLL /MANIFEST:EMBED,ID=2 /MANIFESTUAC:NO /LIBPATH:C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\libs /LIBPATH:C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\PCbuild\win32 "/LIBPATH:C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\LIB" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.10240.0\ucrt\x86" "/LIBPATH:C:\Program Files (x86)\Windows Kits\8.1\lib\winv6.3\um\x86" /EXPORT:PyInit_palindrome2 build\temp.win32-3.8\Release\palindrome2.obj /OUT:build\lib.win32-3.8\palindrome2.cp38-win32.pyd /IMPLIB:build\temp.win32-3.8\Release\palindrome2.cp38-win32.lib
LINK : error LNK2001: unresolved external symbol PyInit_palindrome2
build\temp.win32-3.8\Release\palindrome2.cp38-win32.lib : fatal error LNK1120: 1 unresolved externals
error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\link.exe' failed with exit status 1120

```

## Python的扩展是个重点、打包也是一个重点

这本书里面没有详细将这些。而且也不太严谨。很多例子无法编译通过。

> 1.利用pycharm打包

> 2..pipinstall工具打包

> 3.pypi打包





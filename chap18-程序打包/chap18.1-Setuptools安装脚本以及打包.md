### 1.如果还没有安装Setuptools，请使用 pip 安装

```
pip install setuptools
```

### 2.编写好setup.py脚本，以及要被打包的hello.py脚本（前面已经准备好了）

### 3.执行打包命令

```
python setup.py  build
```

### 4.执行安装命令

```
python setup.py install
```

### 4.验证结果

```
>>> import hello
This is a Hello py!
---------end

>>> hello.GetTime()
This func get time.
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=13, tm_hour=21, tm_min=5, tm_sec=26, tm_wday=2, tm_yday=317, tm_isdst=0)
```

## 5.这里只是初步演示一个简单的Setuptools安装脚本。

```
Setuptools还有很多功能等待解锁。
以及有很多其他的软件可以实现这样的功能。
有待后面去完成。
```

==============================

## 编写让用户能够安装模块的脚本setup.py后,就可以使用它来创建归档文件了。

```
python  setup.py  sdist
```
现在，除目录build外，应该还有一个名为dist的目录。在这个目录下，有一个名为hello-1.0.tar.gz的文件。
你可以将其分发给其他人，而对方可将其解压缩，再使用脚本setup.py进行安装。

可通过命令行开关 --formats 指定多种用逗号分隔的格式。


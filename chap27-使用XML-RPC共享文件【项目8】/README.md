# 第27章 小结:mortar_board:

我们要创建一个P2P(peer-to-peer)文件共享程序。:first_quarter_moon:

1.执行 listing27.1.py 的命令
```python console
python listing27.1.py http://localhost:4243 fiel2 secret2
```

2.执行 client.py 的命令

```
python client.py urls.txt file1 http://localhost:4247
python client.py urls.txt file2 http://localhost:4248
python client.py urls.txt file3 http://localhost:4249

```

3.本章介绍的模块

```
from xmlrpc.client import ServerProxy, Fault
from cmd import Cmd
from random import choice
from string import ascii_lowercase
from server import Node, UNHANDLED
from threading import Thread
from time import sleep
import sys


from xmlrpc.client import ServerProxy, Fault
from os.path import join, abspath, isfile
from xmlrpc.server import SimpleXMLRPCServer
from urllib.parse import urlparse
import sys

from xmlrpc.client import ServerProxy
from os.path import join, isfile
from xmlrpc.server import SimpleXMLRPCServer
from urllib.parse import urlparse
import sys


```


### 进一步探索【这个项目还是蛮不错的】 :recycle::checkered_flag::airplane:

对于本章介绍的系统，你可能会相出多种改进和扩展方式。下面是一些建议。

- [ ] 添加缓存功能。在结点通过调用query来传递文件时，为何不同时存储该文件呢？
这样，再有人请求这个文件时，响应速度将更快。
你可以设置最大缓存空间，删除最早缓存的文件等。

- [ ] 使用线程化（异步）服务器。（这有点难）这样，可向多个结点寻求帮助，
而无需等待它们应答（它们将在以后通过调用方法 reply 来应答）

- [ ] 支持更高级的查询，如查询文本文件的内容。

- [ ] 更充分地利用方法 hello。通过调用 hello 发现新结点时，为何不将这个新结点介绍给其他所有已知的对等体呢？
或许你还能想到更巧妙的新对等体发现方式。

- [ ] 深入研究用于分布式系统的表属性状态传递( REST )理念。REST 可用于替代 XML-RPC 等 Web服务技术。

- [ ] 使用 xmlrpc.client.Binary 来封装文件，从而更安全地传输非文本文件。

- [ ] 阅读 SimpleXMLRPCServer 的代码。研究 DocXMLRPCServer 类以及 libxmlrpc 中的多调用(multicall)扩展


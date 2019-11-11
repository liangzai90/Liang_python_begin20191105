print("---------使用 Twisted 创建的简单服务器---------")

# 快捷方式，在pycharm里面搜索 twisted模块，自动安装。

# 笨办法，自己手动安装。步骤如下：
# windows下面，以管理员身份运行cmd，然后 输入下面的命令
# 【问题1】pip版本过低
# python -m pip install --upgrade pip
# 【问题2】error: Microsoft VisualC + + 14.0 is required.Get it with "Microsoft Visual C++ Build Tools": https: // visualstudio.microsoft.com / downloads /
# 这个对应vs2015
# 安装 Twisted
# python -m pip install  Twisted



from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleLogger(Protocol):
    def connectionMade(self):
        print("Twisted....Got connection from:", self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    def dataReceived(self, data):
        print(data)

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()

第14章 小结

-------------------------------------------

【套接字和模块socket】套接字是让程序能够进行通信的信息通道，这种通信可能需要通过网络进行。
服务器套接字在指定地址处监听客户端连接，客户端套接字直接连接到服务器。

【urllib和urllib2】这些模块让你能够从各种服务器读取和下载数据。

【框架SocketServer】这个框架位于标准库中，包含一些列同步服务器基类，让你能够轻松地编写服务器。

【select和poll】这两个函数让你能够在一组连接中找出为读取和写入准备就绪的连接。

【Twisted】这是Twisted Matrix Laboratories开发的一个框架，功能丰富而复杂，支持大多数主要的网络协议。
Twisted框架是异步的

------------------------------------------

新函数

urllib.urlopen(url[, data[, proxies]])  根据指定的URL打开一个类似于文件的对象 

urllib.urlretrieve(url[, fname[,hook[,data]]])  【【下载URL指定的文件】】

urllib.quote(string[, safe])  替换特殊的URL字符

urllib.quote_plus(string[, safe])  与 quote 一样，但也将空格替换为+

urllib.unquote(string)  与 quote 相反

urllib.unquote_plus(string)  与 quote_plus 相反

urllib.urlencode(query[, doseq])  对映射进行编码，以便用于CGI查询中

select.select(iseq, oseq, eseq[, timeout])  找出为读/写做好了准备的套接字

select.poll()  创建一个轮询对象，用于轮询套接字

reactor.listenTCP(port, factory)  监听连接的Twisted函数

reactor.run()  启动服务器循环的Twisted函数

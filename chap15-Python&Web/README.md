# 第15章 小结

-------------------------------------------------

【屏幕抓取】：指的是自动下载网页并从中提取信息。
程序Tidy及其库版本是很有用的工具，可以用来修复格式糟糕的HTML，然后使用HTML解析器进行解析。
另一种抓取方式是使用Beautiful Soup，即便面对混乱的输入，它也可以处理

【CGI】：通用网关接口是一种创建动态网页的方式，这是通过让Web服务器运行、与客户端程序通信并显示结果而实现的。
模块 cgi 和 cgitb 可用于编写 CGI脚本。CGI脚本通常是在HTML表单中调用的。

【Flask】：一个简单的Web框架，让你能够将代码作为Web应用发布，同时不用过多操心Web部分。

【web应用框架】：要使用Python开发复杂的大型Web应用，Web应用的框架必不可少。
对简单的项目来说，Flask是不错的选择；
但对于较大的项目，你可能应考虑使用Django或TurboGears。

【Web服务】Web服务之于程序犹如网页之于用户。你可以认为，Web服务让你能够以更抽象的方式进行网络编程。
常用的Web服务标准包括RSS(以及与之类似的RDF和Atom)、XML-RPC和SOAP。

-----------------------------------------------------

### 新函数

cgitb.enable()  在CGI脚本中启用栈跟踪

----------------------------------------

### 请注意

使用CGI创建动态网页

```
Linux环境，第1行 应该像下面这么写
#!/usr/bin/env python

windows环境，第1行应该明确指出 python.exe的路径
#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe

```

你需要在Windows 配置Apache+CGI，然后通过浏览器访问脚本

[安装和设置方法，请点击这里。](https://www.cnblogs.com/music-liang/p/11846268.html)



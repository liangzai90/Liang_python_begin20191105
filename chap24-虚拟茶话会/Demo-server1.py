# -*-coding: utf-8  -*-

# 一个极简单的服务器程序
from asyncore import dispatcher
import asyncore

class ChatServer(dispatcher):pass

s = ChatServer()
asyncore.loop()

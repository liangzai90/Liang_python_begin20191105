# 第26章 小结

很多软件都让你能够通过互联网与他人交流，你已经见过其中的一些，
如第23章介绍的Usenet讨论组以及24章介绍的聊天服务器。
本章将实现另一种这样的系统----基于web的论坛。


### 知识点回顾


1.在SQLite中创建一个表，插入数据

```Python
import sqlite3
conn = sqlite3.connect('myweb.db')
curs = conn.cursor()

""" 创建表的时候，开启这里的代码；表创建好了，就屏蔽这里的代码
curs.execute('''
CREATE TABLE messages(
id         integer    primary  key  autoincrement,
subject    text       not null, 
sender     text       not null,
reply_to   int,
text       text      not null
)
''')
"""


reply_to = input("Reply to: ")
subject = input("Subject: ")
sender = input("Sender: ")
text = input("Text: ")

if reply_to:
    query = """
    INSERT INTO messages(reply_to, sender, subject, text)
    VALUES({}, '{}', '{}', '{}')""".format(reply_to, sender, subject, text)
else:
    query = """
    INSERT INTO messages(sender, subject, text)
    VALUES('{}', '{}', '{}')""".format(sender, subject, text)

curs.execute(query)

conn.commit()
conn.close()

```


2.连接数据库，取出表中所有的数据（根据具体需求，修改sql语句）

```
#!C:\Users\heliang\AppData\Local\Programs\Python\Python38-32\python.exe

import logging
logging.basicConfig(level=logging.INFO, filename="mylog.log")

print('Content-type: text/html \n')
import cgitb; cgitb.enable()
import sqlite3
conn =sqlite3.connect('myweb.db')
curs = conn.cursor()

curs.execute('select * from messages')
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]

print(names)
print(rows)

# ##('SELECT * FROM messages WHERE id = %s'.format(id))

```

3.这里还有网页之间的互相跳转、表单提交跳转


```html

<p><a href="edit.cgi">Post message</a></p>

<a href='main.cgi'>Back to the main page</a>
   
<a href='main.cgi'>Back to the main page</a>
| <a href="edit.cgi?reply_to={id}">Reply</a>  
   
<form action='save.cgi' method='POST'>
<input type='submit' value='Save'/>
</form>

```

### 吐槽

在后面的项目介绍的几章，感觉作者不是那么用心了。很多项目不是那么容易跑起来。

可能是要展示真正的实例的时候了。。。

要自己动手了，不能太依赖书本。

这里的cgi项目，需要 [在windows搭建Apache和cgi环境，请参考这里](https://www.cnblogs.com/music-liang/p/11846268.html)


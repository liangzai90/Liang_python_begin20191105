import sqlite3
conn = sqlite3.connect("chap13.1.db")

# 从连接获得游标，这个游标可用来执行 sql查询
curs = conn.cursor()

#   do_something 执行sql查询

# 提交修改的内容
conn.commit()

# 关闭连接
conn.close()



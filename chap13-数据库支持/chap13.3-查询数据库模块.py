import sqlite3, sys
conn = sqlite3.connect("food.db")
curs = conn.cursor()

query = 'Select * from food where ' + sys.argv[1]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print("{}: {}".format(*pair))
    print()
    
"""
脚本功能是，从本地的food.db数据库读取数据，并查询数据.

使用带命令行的参数来运行这个脚本。
在IDLE界面，打开我们的这个py文件，然后 [Run]-->[Run...Cumtomized] 然后输入参数

"kcal<=100 and fiber >= 100 order by sugar"

"""

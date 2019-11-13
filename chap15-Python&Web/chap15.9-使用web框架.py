from flask import Flask
app = Flask(__name__)

@app.route('chap15.9.py')
def powers(n=10):
    return ', '.join(str(2**i) for i in range(n))

# 找不到变量的处理方式
# 将下面命令替换set FLASK_APP = chap15.9.py  成 $env:FLASK_APP = "chap15.9.py"
# 卡壳了。。。环境配置不熟悉
# RSS, XML-RPC 等等 高级内容不太好理解


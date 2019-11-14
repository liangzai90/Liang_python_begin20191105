from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello Flask world!"

if __name__ == "__main__":
    app.run()


# RSS, XML-RPC 等等 高级内容不太好理解


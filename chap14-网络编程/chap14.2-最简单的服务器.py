print("---------- 最简单的 服务器 ----------")
import socket
skt = socket.socket()

host = socket.gethostname()
port = 1234
skt.bind((host, port))

skt.listen(5)

while True:
    conn, addr = skt.accept()
    print("Got connection from: ", addr)
    # 请注意这里要发送的内容，参考官方帮助文档才知道需要在字符串前面加个 b
    conn.send(b"Thank you for connecting.")
    conn.close()

import socket
s = socket.socket()
host = socket.gethostname()
print(host)
port = 5005
s.connect((host, port))
# 接受到的是字节流，这里解码为utf-8字符
print(s.recv(port).decode('utf-8'))

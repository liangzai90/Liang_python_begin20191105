print("---------最简单的客户端------------")
import socket

skt = socket.socket()

host = socket.gethostname()
port = 1234

skt.connect((host, port))
print(skt.recv(1024))

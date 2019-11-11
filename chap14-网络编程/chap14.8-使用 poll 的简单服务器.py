print("------- 使用 poll 的简单服务器...windows不支持poll,需要在 Linux 下面运行 --------")

import socket, select

skt = socket.socket()
host = socket.gethostname()
port = 1234
skt.bind((host, port))
fdmap = {skt.fileno(): skt}
skt.listen(5)
p = select.poll()
p.register(skt)

while True:
    events = p.poll()
    for fd, event in events:
        if fd in fdmap:
            conn, addr = skt.accept()
            print("Got connection from : ", addr)
            p.register()
            fdmap[conn.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:  #没有数据，连接已关闭
                print(fdmap[fd].getpeername(), 'disconnected')
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)

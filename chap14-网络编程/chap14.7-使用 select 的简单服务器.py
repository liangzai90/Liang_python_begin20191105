print("-------使用 select 的简单服务器---------")

import socket, select

skt = socket.socket()
host = socket.gethostname()
port = 1234
skt.bind((host, port))
skt.listen(5)
inputs = [skt]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is skt:
            conn, addr = skt.accept()
            print("Got connection from ", addr)
            inputs.append(conn)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print(r.getpeername(), 'disconnected')
                inputs.remove(r)
            else:
                print(data)


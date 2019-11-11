print("------- SocketServer 模块 ------")
print("-------基于 SocketServer 的极简服务器 ------")
from socketserver import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print("Got connection from: ", addr)
        self.wfile.write(b"Thank you for connecting...")

server = TCPServer(("", 1234), Handler)
server.serve_forever()

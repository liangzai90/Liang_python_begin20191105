# print("--------- 使用 SocketServer 实现分叉和线程化 -------------")
# print("-----分叉服务器------windows下无法运行，需要再linux下运行")
from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print("Got connection from: ", addr)
        self.wfile.write(b"Thank you for connecting!")

server = Server(("", 1234), Handler)
server.serve_forever()

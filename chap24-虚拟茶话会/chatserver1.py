# -*-  coding: utf-8  -*-

from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005
NAME = "TestChat"

class EndSession(Exception):pass

class CommandHandler:
    """
    类似于标准库中cmd.Cmd的简单命令处理程序
    """
    def unknown(self, session, cmd):
        '响应未知命令'
        session.push('Unknown command: {}s\r\n'.format(cmd).encode())
    def handle(self, session, line):
        '处理从指定会话收到的行'
        if not line.strip():return
        # 提取命令
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:line = parts[1].strip()
        except IndexError: line = ''
        # 尝试查找处理程序
        meth = getattr(self, 'do_' + cmd, None)
        try:
            # 嘉定它是可调用的
            meth(session, line)
        except TypeError:
            # 如果是不可调用的，就响应未知命令
            self.unknown(session, cmd)

class Room(CommandHandler):
    """
    可能包含一个或多个用户（会话）的通用环境。它负责基本的命令处理和广播
    """
    def __init__(self, server):
        self.server = server
        self.sessions = []
    def add(self, session):
        '有会话（用户）进入聊天室'
        self.sessions.append(session)
    def remove(self, session):
        '有会话（用户）离开聊天室'
        self.sessions.remove(session)
    def broadcast(self, line):
        '将一行内容发送给聊天室内的所有会话'
        for session in self.sessions:
            session.push(line.encode())
    def do_logout(self, session, line):
        '响应命令 Logout'
        raise EndSession

class LoginRoom(Room):
    """
    为刚连接的用户准备的聊天室
    """
    def add(self, session):
        Room.add(self, session)
        # 用户进入时，向他发出问候        
        self.broadcast('Welcome 何亮亮 to{}\r\n'.format(self.server.name))
    def unknown(self, session, cmd):
        # 除login和logout外的所有命令都会导致系统显示提示消息
        session.push('Please log in \n Use "login <nick> " \r\n'.encode())
    def do_login(self, session, line):
        name = line.strip()
        # 确保用户输入了用户名
        if not name:
            session.push("Please enter a name \r\n".encode())
        # 确保用户名没有被占用
        elif name in self.server.users:
            session.push('The name "{}" is taken.\r\n'.format(name).encode())
            session.push('Please try again.\r\n'.encode())
        else:
            # 用户名没问题、因此将其存储到会话中并将用户移到主聊天室
            session.name = name
            session.enter(self.server.main_room)

class ChatRoom(Room):
    """
    为多个用户相互聊天准备的聊天室
    """
    def add(self, session):
        # 告诉所有人有新用户进入
        self.broadcast(session.name + ' has entered the room.\r\n')
        self.server.users[session.name] = session
        super().add(session)
    def remove(self, session):
        Room.remove(self, session)
        # 告诉所有人有用户离开
        self.broadcast(session.name + ' has left the room.\r\n')
    def do_say(self, session, line):
        self.broadcast(session.name + ': ' + line + '\r\n')
    def do_look(self, session, line):
        '处理命令look,这个命令用于查看聊天室里都有谁'
        session.push('The following are in this room:\r\n'.encode())
        for other in self.sessions:
            session.push('{0}\r\n'.format(other.name).encode())
    def do_who(self, session, line):
        '处理命令who，这个命令用于查看谁已登录'
        session.push('The following are logged in: \r\n'.encode())
        for name in self.server.users:
            session.push('{0}\r\n'.format(name).encode())

class LogoutRoom(Room):
    """
    为单个用户准备的聊天室，仅用于将用户名从服务器中删除
    """
    def add(self, session):
        # 将进入LogoutRoom的用户删除
        try: del self.server.users[session.name]
        except KeyError:pass

class ChatSession(async_chat):
    """
    单个会话， 负责与单个用户通信
    """
    def __init__(self, server, sock):
        super().__init__(sock)
        self.server = server
        self.set_terminator("\r\n".encode())
        self.data = []
        self.name = None
        # 所有会话最初都位于LoginRoom中
        self.enter(LoginRoom(server))
    def enter(self, room):
        # 自己从当前聊天室离开，并进入下一个聊天室
        try:cur = self.room
        except AttributeError:pass
        else: cur.remove(self)
        self.room = room
        room.add(self)
    def collect_incoming_data(self,data):
        self.data.append(data)
    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        try:self.room.handle(self, line)
        except EndSession:self.handle_close()
    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))

class ChatServer(dispatcher):
    """
    只有一个聊天室的聊天服务器
    """
    def __init__(self, port, name):
        super().__init__()
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.users = {}
        self.main_room = ChatRoom(self)
    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)

if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:asyncore.loop()
    except KeyboardInterrupt:print()

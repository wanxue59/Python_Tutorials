import socket

s = socket.socket()    # 创建socket对象
host = socket.gethostname()    # 获取本地主机名
port = 12345    # 设置端口号

s.connect((host, port))    # 主动初始化TCP服务器连接。一般address的格式为元组（hostname,port)
print(s.recv(1024))    # s.recv()：接收 TCP 数据，数据以字符串形式返回
s.close()    # 关闭连接
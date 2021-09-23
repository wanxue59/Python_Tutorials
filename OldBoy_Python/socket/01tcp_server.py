"""
基于TCP的套接字
    TCP是基于链接的，必须先启动服务端，然后再启动客户端去链接服务端
"""
from socket import *
ss = socket()    # 创建服务器套接字
ss.bind()    # 把地址绑定到套接字
ss.listen()    # 监听链接
while True:    # 服务器无限循环
    cs = ss.accept()    # 接受客户端链接

"""
10.2.4  实例32：实现基于事件机制的消息队列
    创建两个线程，让其共同操作一个队列。一个线程是readthread，负责从队列里往外读取数据；
一个线程是writethread，负责写入数据。
    要求：readthread读时，writethread不能写；writethread写时，readthread不能读
"""
import queue
from random import randint
from threading import Thread
from threading import Event

class WriteThread(Thread):    # 写数据线程
    def __init__(self, q, WE, RE):
        super().__init__()
        self.queue = q
        self.RE = RE
        self.WE = WE
    def run(self):
        data = [randint(1, 10) for _ in range(0, 5)]
        self.queue.put(data)
        print("WriteThread 写队列：", data)
        self.RE.set()    # 通知线程可以读了
        print("WriteThread 通知读事件")
        print("WriteThread 等待写事件")
        self.WE.wait()    # 等待写事件
        print("WriteThread 收到写事件")
        self.WE.clear()    # 清除写事件，以方便下次读取

class ReadThread(Thread):    # 读数据线程
    def __init__(self, q, WE, RE):
        super().__init__()
        self.queue = q
        self.RE = RE
        self.WE = WE

    def run(self):
        self.RE.wait()    # 等待读事件
        print("ReadThread 收到读事件")
        data = self.queue.get()
        print("ReadThread 读队列{0}".format(data))
        print("ReadThread 发送写事件")
        self.WE.set()    # 发送写事件
        self.RE.clear()    # 清除读事件，以方便下次读取

q = queue.Queue()
WE = Event()
RE = Event()
writethread = WriteThread(q, WE, RE)    # 实例化线程类
readthread = ReadThread(q, WE, RE)

writethread.start()
readthread.start()
import threading
def handle(sid):    # 线程处理函数当键盘按下CTRL+C从shell中发出信号，信号被传递给shell中前台运行的进程，对应该信号的默认操作是中断 (INTERRUPT) 该进程
    print("Thread %d run"%sid, threading.current_thread())
class MyThread(threading.Thread):    # 定义threading.Thread的派生类
    def __init__(self, sid):   # 重载初始化方法
        threading.Thread.__init__(self)
        self.sid = sid
    def run(self):    # 重载run方法
        handle(self.sid)

for i in range(1, 11):    # 循环创建多线程
    t = MyThread(i)    # 实例化threading.Thread的派生类
    t.start()    # 调用start方法
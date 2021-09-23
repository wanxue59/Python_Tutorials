import threading

def handle(sid):    # 线程处理函数，内部打印出当前线程的参数及名称
    print("Thread %d run:"%sid, threading.current_thread())

for i in range(1, 11):    # 使用一个循环来创建多个线程
    # 每次将计数器作为参数传入新建的线程中
    t = threading.Thread(target=handle,    # target: 线程函数
                         args=(i, ))    # args: 传递给线程函数的参数，必须为元组类型
    t.start()    # 启动线程
print("main thread:", threading.current_thread())    # 打印主线程信息
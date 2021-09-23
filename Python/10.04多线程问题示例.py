'''多线程问题示例'''
import threading
import time
g_num = 1    # 公共计数器
def handle(arg):    # 线程处理函数
    global g_num
    g_num *= 2    # 计数器乘以2
    time.sleep(arg%2)    # 类似与其他操作，这里用sleep代替计算时间
    print("thread{}: {}".format(arg, g_num))    # 输出线程对应的计数器数值
threads = []    # 建立线程列表
for i in range(1, 10):
    t = threading.Thread(target=handle, args=(i,))
    t.start()
    threads.append(t)    # 将创建的线程全都放到列表里
for t in threads:    # 等待所有线程完成
    t.join()
print("main thread end")    # 程序结束，退出主线程
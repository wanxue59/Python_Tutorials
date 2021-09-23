"""
10.2.3  实例31：使用信号量来同步多线程间的顺序关系
    先定义两个线程处理函数：一个是生产者，一个是消费者。使用信号量来同步两个函数顺序关系。
在生产者函数中，不定期的完成生产任务。消费者函数中直接进行消费操作。
    接着，同时启用若干个关于生产者及消费者的线程。观察程序运行情况。
"""
import threading
import time
import random
semaphore = threading.Semaphore(1)    # 创建纯粹信号量
# semaphore = threading.BoundedSemaphore(1)    # 创建边界信号量，参数不能为0，而且item得在函数外定义
def producer():    # 定义生产者
    global item    # 定义商品编号
    # time.sleep(3)    # 休眠3秒
    item = random.randint(1, 1000)    # 产生随机数
    print("producer: 生产 {}".format(item))
    semaphore.release()

def consumer():    # 定义消费者
    print("consumer :挂起.")
    semaphore.acquire()
    print("consumer : 消费 %s."%item)

threads = []    # 定义列表收集线程

for i in range(0, 2):    # 建立生产者和消费者线程
    t1 = threading.Thread(target=producer)    # 生产者线程
    t2 = threading.Thread(target=consumer)    # 消费者线程
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

for t in threads:    # 等待所有线程完成
    t.join()
"""
10.2.5  实例33：使用条件锁同步多线程中的生产者与消费者关系
    条件锁，是线程同步中更高级的一种应用。它是在保护互斥资源的基础之上，又增加了条件判断的机制。
在判断当前情况不满足某条件时，条件锁可以主动挂起当前程序，等待条件准备好后再去执行。
实例描述：
    定义两个线程处理函数：一个是生产者，另一个是消费者，并使用条件锁进行顺序关系的同步。在生产者
函数中，不定期的完成生产任务。在消费者函数中，直接进行消费操作。
    接着，同时启用若干个关于生产者及消费者的线程。观察程序运行情况。
"""
from threading import Thread
from threading import Condition
import time
import random

c = Condition()    # 创建条件锁
itemNum = 0
item = 0
def consumer():    # 定义消费者
    global item    # 定义商品编号
    global itemNum    # 定义商品个数
    c.acquire()    # 锁住资源
    while 0 == itemNum:    # 如无产品，则让线程等待
        print("consumer: 挂起.")
        c.wait()    # 挂起当前线程，等待唤起
    itemNum -= 1    # 消费者每消费一件商品，itemNum减一
    print("consumer: 消费{}".format(item), itemNum)
    c.release()    # 解锁资源


def producer():    # 定义生产者
    global item    # 定义生产者
    global itemNum    # 定义商品编号
    time.sleep(3)
    c.acquire()    # 锁住资源
    item = random.randint(1, 1000)
    itemNum += 1
    print("producer: 生产{}".format(item), itemNum)
    c.notifyAll()    # 唤醒所有等待的线程（消费者）
    c.release()    # 解锁资源

threads = []    # 定义线程收集列表

for i in range(0, 2):    # 使用循环完成生产者与消费者线程的建立
    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

for t in threads:    # 等待所有线程完成
    t.join()
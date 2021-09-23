"""
10.2.7  实例35：使用线程池提示运行效率
    线程池的处理方式是：在程序启动时就创建好若干个线程，并保持到内存中。当线程启动并执行完成之后，并不做
销毁处理，而是等待下次再使用。这样内存中的线程就像个池子一样，需要时过来取，用完了再还回去。
实例描述：
    编写代码，实现一个列表，其中的内容是具体的人名；编写函数，输出传入内容；调用函数，依次处理列表中的
元素。并做如下处理：
（1）使用一个主线程进行处理并记录处理时间
（2）使用线程池处理并记录处理时间（两种方式：抢占式、顺序式）
（3）对两个时间进行比较，体会多线程的优势
"""
from concurrent.futures import ThreadPoolExecutor
import time

def printperson(p):    # 定义线程池处理函数
    print(p)
    time.sleep(2)

person = ["Anna", "Gary", "All"]
start1 = time.time()    # 获取开始时间

#################### 单线程顺序执行 ####################
for p in person:    # 调用函数，将列表元素依次传入
    printperson(p)
end1 = time.time()
print("单线程顺序执行时间time1: " + str(end1-start1))    # 打印时间差
#################### 单线程顺序执行 ####################


#################### 抢占式线程池多线程执行 ####################
start2 = time.time()
with ThreadPoolExecutor(3) as executor1:    # 创建抢占式线程池，池内有3个线程
    for p in person:
        executor1.submit(printperson, p)    # 启用线程
end2 = time.time()
print("抢占式线程池多线程执行时间time2: "+str(end2-start2))
#################### 抢占式线程池多线程执行 ####################


#################### 顺序式线程池多线程执行 ####################
start3 = time.time()
with ThreadPoolExecutor(3) as executor2:
    executor2.map(printperson, person)    # 启用线程
end3 = time.time()
print("顺序式线程池多线程执行时间time3: "+str(end3-start3))
#################### 顺序式线程池多线程执行 ####################
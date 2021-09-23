"""
10.2.8  实例36：创建多进程的程序
    在Python中，进程相关的实现被统一封装在模块multiprocessing中。进程的创建方式有两种：
1. 继承：multiprocessing中的Process类，并重写run方法
2. 直接通过multiprocessing中的进程类Process进行创建
实例描述：
    分别使用继承类与类的实例化方式创建多线程程序，并做如下操作：
（1）向进程传入参数
（2）打印进程中已启动的进程ID
（3）分析输出结果，理解多进程程序
"""
from multiprocessing import Process
import time
import random
import os

#################### 使用继承类的方式创建线程 ####################
# class Myproc(Process):    # 继承Process类，并实现自己的run方法
    # def __init__(self, name):    # 必须调用父类的init方法
    #     super().__init__()
    #     self.name = name
    # def run(self):
    #     print("{} start".format(self.name), os.getpid())    # 获取并打印当前进程的进程ID
    #     time.sleep(random.randint(1, 3))
    #     print("{} end".format(self.name), os.getpid())
#################### 使用继承类的方式创建线程 ####################


#################### 使用类的实例化方式创建线程 ####################
def run_proc(name):    # 进程处理函数
    print("%s start"%name, os.getpid())    # 获取并打印当前进程的进程ID
    time.sleep(random.randint(1, 3))
    print("{} end".format(name), os.getpid())
#################### 使用类的实例化方式创建线程 ####################


if __name__ == '__main__':    # 使用创建进程语句时，必须要有这句
    ### 使用继承类的方式创建线程 ###
    # p1 = Myproc("test")    # 实例化子进程并传入参数
    # p1.start()    # 启动进程
    # print("主进程！", os.getpid())    # 获取并打印当前进程的进程ID
    # p1.join()
    # print("主进程结束.")

    #### 使用类的实例化方式创建线程 ###
    p = Process(target=run_proc, args=("test", ))    # 实例化
    print("主进程！", os.getpid())    # 获取并打印当前进程的进程ID
    p.start()
    p.join()
    print("主进程结束.")
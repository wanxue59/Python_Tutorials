"""
10.2.6  实例34：创建定时器触发程序，在屏幕上输出消息
    定时器，时Python应用在运维自动化项目中的常用方法。在其他方向的项目中也有广泛的应用。其功能是
设定一个时间，当到达该时间时让机器自动去做某事。这种方式又叫作“时间触发事件”。
实例描述：
    创建一个定时器，并实现如下功能：
（1）一秒钟之后，在屏幕打印一句话："Timer headle!"
（2）之后每隔一秒在屏幕上打印一次："Timer headle!"
（3）为第二步加个限制，只允许持续10秒
"""
import threading
import time

#################### 单次触发定时器 ####################
def timer_headle():    # 定时器触发函数
    print("Timer headle!")
    loop_timer_headle()
#################### 单次触发定时器 ####################


#################### 循环触发定时器 ####################
def loop_timer_headle():    # 定时器循环触发函数
    global timer
    timer = threading.Timer(1, timer_headle)
    timer.start()
#################### 循环触发定时器 ####################

loop_timer_headle()
time.sleep(10)    # 休眠十秒
timer.cancel()    # 结束定时器
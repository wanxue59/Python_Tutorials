# -*- coding: utf-8 -*-
"""
Project: Tutorials
File Name: EXP009代码运行时间
Author: wjz
date: 2021-09-13
"""

import time

# 程序执行时间 = cpu时间 + io时间 + 休眠或者等待时间
def timeit(func):
    def wrapper(*args, **kwargs):    # 使用字典和元组的解包参数来作形参
        start = time.time_ns()    # 程序运行前的时间
        print("start:", start)
        func(*args, **kwargs)    # 将参数透传给原函数
        end = time.time_ns()    # 程序运行完的时间
        print("end:", end)
        print("%s函数运行时间为：%.8f Seconds." % (func.__name__, end - start))
    return wrapper  # 将装饰后的函数返回


@timeit
def func1(x):
    return x**3 - x**2 -x

func1 = func1(12306)
print("func1(12306) =", func1)
# -*- coding: utf-8 -*-
"""
Project: Tutorials
File Name: 01时间复杂度
Author: wjz
date: 2021-09-16
"""
import time

start_time = time.time()
for i in range(1001):
    for j in range(1001):
        for k in range(1001):
            if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2:
                print(i, j, k)
end_time = time.time()
print("RunningTime: {} Seconds.".format(end_time - start_time))
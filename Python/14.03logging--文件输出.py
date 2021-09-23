# -*- coding: utf-8 -*-
"""
参考文档：python中logging模块的一些简单用法
网址：https://www.cnblogs.com/CJOKER/p/8295272.html
Project: Tutorials
File Name: 14.03logging--文件输出
Author: wjz
date: 2021-09-09
"""

import logging
import os
import time

##### 第1步，创建一个logger #####
proc_name = os.path.basename(__file__)    # 获取本文件的文件名：14.03logging--文件输出.py
logger = logging.getLogger(proc_name)    # 创建一个logger日志对象
logger.setLevel(logging.INFO)


##### 第2步，创建一个handler，用于写入日志文件 #####
strtime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
log_dir = os.getcwd() + "/Logs/"    # D:\PyCharm_Code\Tutorials\Logs\
log_file = log_dir + strtime + "_" + "日志文件输出" + "_log.log"    # log文件绝对路径
fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")    # 创建FileHandler对象
fh.setLevel(logging.INFO)    # 输出到file的log等级的开关


##### 第3步，定义handler的输出格式 #####
logging_format = "%(asctime)s|%(levelname)-10s|%(name)s|%(message)s"
formatter = logging.Formatter(logging_format)
fh.setFormatter(formatter)    # FileHandler对象自定义日志格式


##### 第4步，将logger添加到handler里面 #####
logger.addHandler(fh)    # logger日志对象加载FileHandler对象


# 日志
logger.debug("细节信息，仅当诊断问题时适用。")    # 因为日志输出级别设置为INFO，所以debug的内容不会在console中打印输出
logger.info("确认程序按预期运行。")
logger.warning("表明有已经或即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行。")
logger.error("由于严重的问题，程序的某些功能已经不能正常执行。")
logger.critical("严重的错误，表明程序已不能继续执行。")
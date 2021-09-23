# -*- coding: utf-8 -*-
"""
参考文档：python中logging模块的一些简单用法
网址：https://www.cnblogs.com/CJOKER/p/8295272.html
Project: Tutorials
File Name: 14.02logging模块--控制台输出
Author: wjz
date: 2021-09-09
"""

import logging

# 日志中可能用到的格式化串如下:
"""
%(name)s    Logger的名字
%(levelno)s    数字形式的日志级别
%(levelname)s    文本形式的日志级别
%(pathname)s    调用日志输出函数的模块的完整路径名，可能没有
%(filename)s    调用日志输出函数的模块的文件名
%(module)s    调用日志输出函数的模块名
%(funcName)s    调用日志输出函数的函数名
%(lineno)d    调用日志输出函数的语句所在的代码行
%(created)f    当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d    输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s    字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d    线程ID。可能没有
%(threadName)s    线程名。可能没有
%(process)d    进程ID。可能没有
%(message)s    用户输出的消息
"""
logging_format = "%(asctime)s|%(levelname)-10s|%(filename)s|%(message)s"
logging.basicConfig(level=logging.INFO, format=logging_format)    # 对日志的输出格式及方式做相关配置

logging.debug("细节信息，仅当诊断问题时适用。")    # 因为日志输出级别设置为INFO，所以debug的内容不会在console中打印输出
logging.info("确认程序按预期运行。")
logging.warning("表明有已经或即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行。")
logging.error("由于严重的问题，程序的某些功能已经不能正常执行。")
logging.critical("严重的错误，表明程序已不能继续执行。")
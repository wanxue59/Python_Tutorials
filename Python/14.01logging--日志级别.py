# -*- coding: utf-8 -*-
"""
参考文档：python中logging模块的一些简单用法
网址：https://www.cnblogs.com/CJOKER/p/8295272.html
Project: Tutorials
File Name: 14.01logging模块
Author: wjz
date: 2021-09-09
"""
import logging

logging.debug("细节信息，仅当诊断问题时适用。")
logging.info("确认程序按预期运行。")
logging.warning("表明有已经或即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行。")
logging.error("由于严重的问题，程序的某些功能已经不能正常执行。")
logging.critical("严重的错误，表明程序已不能继续执行。")
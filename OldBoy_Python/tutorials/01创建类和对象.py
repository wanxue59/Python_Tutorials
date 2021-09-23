# -*- coding: utf-8 -*-
"""
参考文档：Python 面向对象（初级篇）
网址：https://www.cnblogs.com/wupeiqi/p/4493506.html
Project: Tutorials
File Name: 01创建类和对象
Author: wjz
date: 2021-09-14
"""

class Foo:    # class--关键字，表示要创建类；Foo--类名称
    # 类中定义的函数叫做“方法”
    def Bar(self):    # self--特殊参数，必填
        print("Bar")

    def Hello(self, name):
        print("I am", name)


# 根据类Foo创建对象obj
obj = Foo()    # 实例化类Foo为对象，取名为obj
obj.Bar()    # 执行Bar方法
obj.Hello("egon")    # 执行Hello方法
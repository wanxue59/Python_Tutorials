# -*- coding: utf-8 -*-
"""
参考文档：Python 面向对象（初级篇）
网址：https://www.cnblogs.com/wupeiqi/p/4493506.html
Project: Tutorials
File Name: 03练习一
Author: wjz
date: 2021-09-14
"""
"""
练习一：在终端输出如下信息
    ·小明，10岁，男，上山去砍柴
    ·小明，10岁，男，开车去东北
    ·小明，10岁，男，最爱大保健
    ·老李，90岁，男，上山去砍柴
    ·老李，90岁，男，开车去东北
    ·老李，90岁，男，最爱广场舞
    ·
    ·老张...
"""

class Foo:
    def __init__(self, name, age, male):    # __init__--构造方法，根据类创建对象时自动执行
        self.name = name
        self.age = age
        self.male = male

    def chop(self):
        print("{}，{}岁，{}，上山去砍柴".format(self.name, self.age, self.male))

    def drive(self):
        print("{}，{}岁，{}，开车去东北".format(self.name, self.age, self.male))

    def dance(self):
        print("{}，{}岁，{}，最爱广场舞".format(self.name, self.age, self.male))


# 根据类Foo创建对象：自动执行Foo类的__init__方法
ming = Foo("小明", 10, "男")    # 将小明、10和男分别封装到ming(self)的name、age和male属性中
li = Foo("老李", 90, "男")    # 将老李、90和男分别封装到li(self)的name、age和male属性中

ming.chop()    # 通过self间接调用被封装的内容
ming.drive()    # 通过self间接调用被封装的内容
ming.dance()    # 通过self间接调用被封装的内容
li.chop()    # 通过self间接调用被封装的内容
li.drive()    # 通过self间接调用被封装的内容
li.dance()    # 通过self间接调用被封装的内容

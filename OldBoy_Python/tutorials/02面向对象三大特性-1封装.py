# -*- coding: utf-8 -*-
"""
参考文档：Python 面向对象（初级篇）
网址：https://www.cnblogs.com/wupeiqi/p/4493506.html
Project: Tutorials
File Name: 02面向对象三大特性
Author: wjz
date: 2021-09-14
"""

"""
面向对象三大特性：封装、继承和多态
    封装：顾名思义就是将内容封装到某个地方，以后再去调用被封装在某处的内容。所以，在使用封装特性时，需要：
        ·将内容封装到某处
        ·从某处调用被封装的内容
    继承：面向对象中的继承和现实生活中的继承相同，即：子可以继承父的内容。
    多态
"""

# 一、封装
class Foo1:
    def __init__(self, name, age):    # __init__--构造方法，根据类创建对象时自动执行
        self.name = name
        self.age = age

"""
self是一个形式参数，当执行obj1 = Foo("egon", 30)时，self 等于 obj1；
                  当执行obj2 = Foo("alex", 28)时，self 等于 obj2。
"""
# 根据类Foo创建对象：自动执行Foo类的__init__方法
obj1 = Foo1("egon", 30)    # 将egon和18分别封装到obj1(self)的name和age属性中
# 根据类Foo创建对象：自动执行Foo类的__init__方法
obj2 = Foo1("alex", 28)    # 将alex和28分别封装到obj2(self)的name和age属性中


# 通过对象直接调用被封装的内容
print("obj1.name: {}   obj1.age: {}".format(obj1.name, obj1.age))    # 直接调用obj1对象的name和age属性
print("obj2.name: {}   obj2.age: {}".format(obj2.name, obj2.age))    # 直接调用obj2对象的name和age属性


# --------------------------------------------------------------------------------------------------------------- #
# 通过self间接调用被封装的内容
class Foo2:
    def __init__(self, name, age):    # __init__--构造方法，根据类创建对象时自动执行
        self.name = name
        self.age = age

    def detail(self):
        print("obj3.name: {}   obj3.age: {}".format(self.name, self.age))

obj3 = Foo2("anny", 25)
# Python默认会将obj3传给self参数，即：obj3.detail(obj3)，所以此时方法内部的 self=obj3，即：self.name是anny，self.age是25
obj3.detail()
# -*- coding: utf-8 -*-
"""
参考文档：Python 面向对象（初级篇）
网址：https://www.cnblogs.com/wupeiqi/p/4493506.html
Project: Tutorials
File Name: 02面向对象三大特性-2多继承
Author: wjz
date: 2021-09-15
"""
"""
Python的类如果继承了多个，那么其寻找方式有两种：深度优先和广度优先
    ·当类是经典类时，多继承情况下，会按照深度优先方式查找
    ·当类是新式类时，多继承情况下，会按照广度优先方式查找
当前类或者父类继承了object类，那么该类便是新式类，否则便是经典类
"""

# 经典类多继承
class D:
    def bar(self):
        print("D.bar")


class C(D):
    def bar(self):
        print("C.bar")


class B(D):
    def bar(self):
        print("B.bar")


class A(B, D):
    def bar(self):
        print("A.bar")

a = A()
a.bar()
print("---"*2)
"""
执行bar方法时（深度优先）：查找顺序：A --> B --> D --> C
    首先去A类中查找；如果A类中没有，则继续去B类中找；如果B类中没有，则继续去D类中找；如果D类中没有，则继续去C类中找；
如果还是未找到，则报错。
    在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
"""

# --------------------------------------------------------------------------------------------------------------- #

# 新式类多继承
class D(object):
    def bar(self):
        print("D.bar")


class C(D):
    def bar(self):
        print("C.bar")


class B(D):
    def bar(self):
        print("B.bar")


class A(B, D):
    def bar(self):
        print("A.bar")

a = A()
a.bar()
"""
执行bar方法时（广度优先）：查找顺序：A --> B --> C --> D
    首先去A类中查找；如果A类中没有，则继续去B类中找；如果B类中没有，则继续去C类中找；如果C类中没有，则继续去D类中找；
如果还是未找到，则报错。
    在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
"""
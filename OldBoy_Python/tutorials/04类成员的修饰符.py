# -*- coding: utf-8 -*-
"""
参考文档：python 面向对象（进阶篇）
网址：https://www.cnblogs.com/wupeiqi/p/4766801.html
Project: Tutorials
File Name: 04类成员修饰符
Author: wjz
date: 2021-09-16
"""
"""
类成员的两种形式：
    ·公有成员：在任何地方都能访问
    ·私有成员：只有在类的内部才能访问
公有成员和私有成员的定义：私有成员命名时，前两个字符是下划线（特殊成员除外，例如：__init__, __dict__等）
公有成员和私有成员的访问限制：
    静态字段：
        ·公有静态字段：类可以访问；类内部可以访问；派生类中可以访问
        ·私有静态字段：仅类内部可以访问
    普通字段：
        ·公有普通字段：对象可以访问；类内部可以访问；派生类中可以访问
        ·私有普通字段：仅类内部可以访问
    ps：如果想要强制访问私有字段，可以通过 【对象._类名__私有字段明 】访问（如：obj._C__foo），不建议强制访问私有成员。
"""

print("\n")
print("***"*20)
class C:
    name = "公有静态字段"
    __name = "私有静态字段"

    def __init__(self):
        self.foo = "公有普通字段"
        self.__foo = "私有普通字段"

    def func(self):
        return C.name, C.__name, self.foo, self.__foo    # 类内部访问公有静态字段和私有静态字段，公有普通字段和私有普通字段


class D(C):
    def show(self):
        return C.name, self.foo


print("类访问公有静态字段：", C.name)    # 类访问公有静态字段
obj1 = C()
print("类内部访问公有字段和私有字段：", obj1.func())    # 类内部访问公有静态字段和私有静态字段
print("强制访问私有字段：", obj1._C__name)    # 强制访问私有字段
obj1_son = D()
print("派生类访问公有静态字段：", obj1_son.show())
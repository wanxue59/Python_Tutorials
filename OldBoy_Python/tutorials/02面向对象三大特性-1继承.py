# -*- coding: utf-8 -*-
"""
参考文档：Python 面向对象（初级篇）
网址：https://www.cnblogs.com/wupeiqi/p/4493506.html
Project: Tutorials
File Name: 05继承
Author: wjz
date: 2021-09-15
"""
"继承：面向对象中的继承和现实生活中的继承相同，即：子可以继承父的内容。"
class Animals:    # 父类（也叫基类）
    def eat(self):
        print("{} 吃".format(self.name))

    def drink(self):
        print("{} 喝".format(self.name))

    def shit(self):
        print("{} 拉".format(self.name))

    def pee(self):
        print("{} 撒".format(self.name))


class Cat(Animals):    # 子类（/派生类）继承父类（/基类），即拥有了父类中的所有方法
    def __init__(self, name):
        self.name = name
        self.breed = "猫"

    def cry(self):
        print("喵喵叫")


class Dog(Animals):  # 子类（/派生类）继承父类（/基类），即拥有了父类中的所有方法
    def __init__(self, name):
        self.name = name
        self.breed = "狗"
        print("{} {}".format(self.name, self.breed))

    def cry(self):
        print("汪汪叫")

bai = Cat("小白")
bai.cry()
bai.eat()    # 使用从父类继承的方法
bai.drink()    # 使用从父类继承的方法
bai.shit()    # 使用从父类继承的方法
bai.pee()    # 使用从父类继承的方法
print("---"*5)

wang = Dog("旺财")
wang.cry()
wang.eat()    # 使用从父类继承的方法
wang.drink()    # 使用从父类继承的方法
wang.shit()    # 使用从父类继承的方法
wang.pee()    # 使用从父类继承的方法

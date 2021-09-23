# -*- coding: utf-8 -*-
"""
参考文档：Python 面向对象（初级篇）
网址：https://www.cnblogs.com/wupeiqi/p/4493506.html
Project: Tutorials
File Name: 04练习二
Author: wjz
date: 2021-09-15
"""
"""
练习二：游戏人生程序
    1、创建三个游戏人物，分别是：
        ·苍井井，女，18，初始战斗力1000
        ·东尼木木，男，20，初始战斗力1800
        ·波多多，女，19，初始战斗力2500
    2、游戏场景，分别：
        ·草丛战斗，消耗200战斗力
        ·自我修炼，增长100战斗力
        ·多人游戏，消耗500战斗力
"""

class Game:
    def __init__(self, name, male, age, combat):
        self.name = name
        self.male = male
        self.age = age
        self.combat = combat
        print("{}，{}，{}，初始战斗力{}".format(self.name, self.male, self.age, self.combat))

    def grasscombat(self):
        self.combat -= 200
        print("{}：草丛战斗，消耗200战斗力，当前战斗力{}".format(self.name, self.combat))

    def practice(self):
        self.combat += 100
        print("{}：自我修炼，增长100战斗力，当前战斗力{}".format(self.name, self.combat))

    def multiplay(self):
        self.combat -= 500
        print("{}：多人游戏，消耗500战斗力，当前战斗力{}".format(self.name, self.combat))


cang = Game("仓井井", "女", 18, 1000)
dong = Game("东尼木木", "男", 20, 1800)
bo = Game("波多多", "女", 19, 2500)

cang.grasscombat()
cang.practice()
cang.practice()


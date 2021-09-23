# -*- coding: utf-8 -*-
"""
参考文档：数据结构与算法（python版）
网址：https://blog.csdn.net/m0_46204224/article/details/107774211
Project: Tutorials
File Name: LinkedList
Author: wjz
date: 2021-09-16
"""
import logging

class Node:    # 定义一个结点类
    def __init__(self, data=None, next=None):
        self.data = data    # 结点的数据
        self.next = next    # 结点的指针



class SingLinkList(Node):
    def __init__(self):
        self._head = None    # 单链表的头结点，私有属性
        # self.tail = None    # 单链表的尾结点
        self.length = 0    # 单链表的长度

    def isEmpty(self):
        '''判断单链表是否为空'''
        return self._head == None    # 若self._head为None，说明链表为空，返回True；否则，返回False

    def travel(self):
        current = self._head
        List = []
        for n in range(self.length):
            List.append(current.data)
            current = current.next
        return List

    def add(self, data):
        '''在头部插入结点'''
        newnode = Node(data, None)    # 新建一个结点，值为data，next为None
        newnode.next = self._head    # newnode的next指向头结点
        self._head = newnode    # 头结点设为newnode
        self.length += 1    # 长度加一

    def append(self, data):
        '''在尾部插入结点'''
        newnode = Node(data)
        if self.isEmpty():    # 若为空表，则插入结点即为头结点
            self._head = newnode
            # print(self._head.data, self._head.next)
        else:
            current = self._head  # 将头结点赋值给临时结点current
            while current.next != None:  # 当current的next指针不为None时，说明current不是尾结点
                current = current.next  # current向后遍历
            current.next = newnode  # 此时current遍历到了尾结点，将尾结点的next指向newnode，newnode成为新的尾结点
        self.length += 1    # 长度加一

    def add_i(self, i, data):
        '''在索引为i的结点后添加新结点'''
        newnode = Node(data)
        if self.isEmpty():
            self._head = newnode
        if i in range(self.length):
            current = self._head
            for a in range(i):
                if current.next != None:
                    current = current.next
                    cur = current.next
                else:
                    current.next = newnode
                    self.length += 1
                    break
            newnode.next = cur
            current.next = newnode
            # print(current.next.)
            self.length += 1

        else:
            logging.ERROR("索引超出范围")
            exit(1)


    def search(self, i):
        '''返回第i个结点的值'''
        if not self.isEmpty():
            if i >= 0 and i < self.length:# and i.isdigit()
                count = 0    # 计数器
                current = self._head
                while count != i:
                    current = current.next    # current向后遍历
                    count += 1    # 计数器加一
                print(current.data)    # 打印索引为i的结点的值
                return
            print("索引超出范围")
        print("该表为空表")

    def isInLink(self, data):
        '''判断data是否在链表中'''
        current = self._head
        for _ in range(self.length - 1):
            if current.data == data:
                print("{}在链表中".format(data))
                return
            current = current.next
        print("{}不在链表中".format(data))
        return


    def remove(self, i):
        '''删除第i个结点'''
        if not self.isEmpty():
            if i in range(self.length):
                current = self._head  # 临时结点，用来遍历链表
                h = self._head  # 头结点，最后需要返回
                if i == 0:
                    self._head = self._head.next
                    self.length -= 1
                elif i == 1:
                    current = self._head
                    current = current.next
                    self._head.next = current.next
                    self.length -= 1
                else:
                    count = 0

                    for a in range(i):
                        current = current.next
                        if a == i - 2:
                            cur = current
                    cur.next = current.next
                    self.length -= 1
                    return h
            # print("索引超出范围")
            logging.ERROR("索引超出范围")
            exit(1)
        else:
            print("该链表为空表")

if __name__ == '__main__':
    # Lin = input("请输入链表值，数字之间用逗号隔开，并按Enter结束：").split(',')
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    Lin = SingLinkList()
    print(Lin)
    for i in List:
        Lin.append(i)

    print("Lin:", Lin.travel())    # 将链表以列表的形式打印

    Lin.add(10)    # 在链表头部添加结点
    print("Lin:", Lin.travel())  # 将链表以列表的形式打印

    Lin.append(30)  # 在链表尾部添加结点
    print("Lin:", Lin.travel())  # 将链表以列表的形式打印

    # Lin.isInLink(5)    # 判断5是否在链表中
    # Lin.isInLink(15)    # 判断15是否在链表中
    #
    # Lin.search(0)    # 查看索引为2的结点的值
    # Lin.search(Lin.length-1)    # 返回最后一个结点的值

    # Lin.remove(0)  # 将索引为11的结点从链表中删去
    # Lin.remove(Lin.length-1)    # 将索引为11的结点从链表中删去
    # print("删除索引为11的结点:", Lin.travel())  # 将链表以列表的形式打印

    Lin.add_i(2, 20)    # 在索引为2的结点后添加值为20的结点
    print("在索引为2的结点后添加结点:", Lin.travel())  # 将链表以列表的形式打印
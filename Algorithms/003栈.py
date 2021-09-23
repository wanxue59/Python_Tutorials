# -*- coding: utf-8 -*-
"""
参考文档：数据结构与算法（python版）
网址：https://blog.csdn.net/m0_46204224/article/details/107774211
Project: Tutorials
File Name: 02栈
Author: wjz
date: 2021-09-17
"""
import logging

class Node:    # 定义一个结点类
    def __init__(self, data=None, next=None):
        self.data = data    # 结点的数据
        self.next = next    # 结点的指针



class Stack(Node):
    def __init__(self):
        self._head = None    # 单链表的头结点，私有属性
        # self.tail = None    # 单链表的尾结点
        self.length = 0    # 单链表的长度

    def isEmpty(self):
        '''判断单链表是否为空'''
        return self._head == None    # 若self._head为None，说明栈为空，返回True；否则，返回False

    def travel(self):
        '''以列表的形式打印栈'''
        current = self._head
        List = []
        for n in range(self.length):
            List.append(current.data)
            current = current.next
        return List

    def push(self, data):
        '''将新元素data添加到栈顶'''
        newnode = Node(data, None)  # 新建一个结点，值为data，next为None
        if self.isEmpty():
            self._head = newnode
            self.length += 1  # 长度加一
        else:
            current =  self._head
            while current.next != None:
                current = current.next
            current.next = newnode
            self.length += 1

    def pop(self):
        '''弹出栈顶元素'''
        if not self.isEmpty():
            current = self._head
            for _ in range(self.length-1):
                current = current.next
            current.next = None
            self.length -= 1

        else:
            logging.WARNING("该栈为空栈")

    def peek(self):
        '''返回栈顶元素'''
        if not self.isEmpty():
            current = self._head
            while current.next != None:
                current = current.next
            return current.data
        else:
            logging.WARNING("该栈为空栈")



if __name__ == '__main__':
    # Lin = input("请输入链表值，数字之间用逗号隔开，并按Enter结束：").split(',')
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    sta = Stack()
    print(sta.travel())    # 以列表形式打印栈
    for i in List:
        sta.push(i)    # 将列表List中的元素依次压入栈顶

    print(sta.travel())    # 以列表形式打印栈

    for _ in range(5):
        sta.pop()    # 将栈顶元素弹出
        print(sta.peek())    # 返回栈顶元素

    print(sta.peek())    # 返回栈顶元素
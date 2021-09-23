# -*- coding: utf-8 -*-
"""
参考文档：数据结构与算法（python版）
网址：https://blog.csdn.net/m0_46204224/article/details/107774211
Project: Tutorials
File Name: 04队列
Author: wjz
date: 2021-09-18
"""
import logging

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue(Node):
    def __init__(self):
        self._head = None
        self.length = 0

    def isEmpty(self):
        '''判断队列是否为空队列'''
        return self._head == None

    def print(self):
        L = []
        if not self.isEmpty():
            current = self._head
            for _ in range(self.length):
                L.append(current.data)
                current = current.next
        return L

    def push(self, data):
        newnode = Node(data)
        if not self.isEmpty():
            current = self._head
            while current.next != None:
                current = current.next
            current.next = newnode
            self.length += 1
        else:
            self._head = newnode
            self.length += 1


    def pop(self):
        if not self.isEmpty():
            self._head = self._head.next
            self.length -= 1
        else:
            print("该队列为空")



if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    q = Queue()
    print("空队列:", q.print())    # 以列表形式打印队列

    for i in List:
        q.push(i)    # 将元素i压入队列
    print("将列表List中的元素压入队列:", q.print())    # 以列表形式打印队列

    q.pop()    # 将队首元素出队
    print("将列表List中的元素压入队列:", q.print())  # 以列表形式打印队列
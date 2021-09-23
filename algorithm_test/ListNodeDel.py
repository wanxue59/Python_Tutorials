from datastruct.LinkList import LinkList
import numpy
a = numpy.reshape
class ListNode:   # 定义一个结点类
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

data = list(int(input("请输入一串数字，并按Enter结束：")))
N = int(input("请输入结点序号N，并按Enter结束："))
# data = [1, 2, 3, 4, 5]
Nodes = [ListNode(i, i+1) for i in data[:]]   # 将输入的数字创建链表

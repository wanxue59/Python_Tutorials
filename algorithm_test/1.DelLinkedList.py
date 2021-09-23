class Node:   # 定义一个结点类
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def getValue(self):   # 返回结点的数值
        return self.value

    def getNext(self):   # 返回结点的指针
        return self.next

    def setValue(self, new_value):   # 设置新的数值
        self.value = new_value

    def setNext(self, new_next):   # 设置新的指针
        self.next = new_next

class LinkList:   # 定义单链表类及其各种操作方法
    def __init__(self):   # 初始化链表为空表
        self.head = Node()
        self.tail = None   # 永远指向最后一个结点
        self.length = 0   # 链表长度为0

    def isEmpty(self):   # 检测是否为空表
        return self.head == None   # 若返回True，表示是空表；否则，不是空表

    def traversal(self):    # 遍历链表，返回链表的个数
        current = self.head
        count = 0
        if self.isEmpty():
            return 0
        else:
            while current.getNext() != None:
                count += 1
                current = current.getNext()
            return count

    def add_tail(self, value):   # 在链表的尾端添加元素
        newnode = Node(value)
        if self.isEmpty():
            self.head = newnode   # 若为空表，添加的元素则为第一个结点
        else:
            current = self.head
            while current.getNext() != None:   # 遍历链表，直到某个结点的next为None
                current = current.getNext()   # 当前结点的next值不为空时，返回next值
            current.setNext(newnode)   # 将链表的最后一个结点的next指向新的结点

    def remove(self,len, n):
        h = self.head
        current = self.head
        pre = self.head
        count = 0
        for i in range(len-n+2):
            if i < len-n:
                current = current.getNext()
            # print("current",current.value)
            pre = pre.getNext()
            # print("pre:", pre.value)
        # print("连接前current:", current.next.value)
        current.setNext(pre)
        # print("连接后current:", current.next.value)
        # print("last current:", current.value)
        # print(h)
        return h


    def printlistNode(self, h):
        p = h
        list = []
        while p.next != None:
            p = p.next
            list.append(p.value)
        print(list)

List = list(map(int,input("请输入数组nums，并按Enter结束：").split(',')))
n = int(input("请输入数字n，并按Enter结束："))
Lin = LinkList()    # 实例化类为对象
for i in List:    # 将List中的元素作为结点添加到单链表Lin中
    Lin.add_tail(i)
len = Lin.traversal()    # 遍历单链表Lin并返回链表长度
h = Lin.remove(len, n)    # 删除链表的倒数第n个结点
Lin.printlistNode(h)    # 打印删除结点后的链表

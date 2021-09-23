'''用Python实现单链表数据类型及其基本操作'''
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

    def add_head(self, value):   # 在链表前端添加元素
        newnode = Node(value, None)   # 创建一个结点，该结点为链表的第一个结点
        newnode.setNext(self.head)   # 该结点的next指向之前的头结点head
        self.head = newnode   # 把新添加的结点设置为链表的头结点

    def add_tail(self, value):   # 在链表的尾端添加元素
        newnode = Node(value)
        if self.isEmpty():
            self.head = newnode   # 若为空表，添加的元素则为第一个结点
        else:
            current = self.head
            while current.getNext() != None:   # 遍历链表，直到某个结点的next为None
                current = current.getNext()   # 当前结点的next值不为空时，返回next值
            current.setNext(newnode)   # 将链表的最后一个结点的next指向新的结点

    def search(self, value):   # 检索元素value是否在链表中
        current = self.head
        foundvalue = False    # 是否找到结点的标志
        while current != None and not foundvalue:    # 链表不为空且显示没找到结点时
            if current.getValue() == value:    # 如果当前结点的值为目标值，说明找到了
                foundvalue = True   # 当当前结点的value值等于value时，说明元素在链表中
            else:
                current = current.getNext()    # 遍历链表，找下一个结点
        return foundvalue

    def index(self, value):   # 索引元素在列表中的位置
        current = self.head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError("%d is not in LinkList"%value)

    def remove(self, value):   # 删除链表中的某个元素
        current = self.head
        pre = None
        while current != None:
            if current.getValue() == value:
                if not pre:
                    self.head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    def insert(self, i, value):   # 在链表中指定位置插入元素
        if i <= 1:
            self.add_head(value)
        elif i > self.size():
            self.add_tail(value)
        else:
            temp = Node(value)
            count = 1
            pre = None
            current = self.head
            while count < i:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)


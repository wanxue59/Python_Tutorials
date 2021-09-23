"""
实例26：演示super函数功能
该代码中没用super函数
"""
class Record:   # 定义一个父类
    __Occupation = 'scientist'  # 职业为科学家，私有变量
    def __init__(self, name, age):  # 定义该类的初始化函数
        self.name = name  # 将传入的参数值赋值给该类的成员变量
        self.age = age

    def showrecode(self):   # 定义一个成员函数
        print('Occupation:', self.getOccupation())   # 该成员函数输出该类的成员变量

    def getOccupation(self):   # 返回私有变量的方法
        return self.__Occupation

class FemaleRecord(Record):   # 定义一个子类
    def showrecode(self):   # 定义一个成员函数
        print(self.name, ':', self.age, ",female")   # 该成员函数返回该类的成员变量
        Record.showrecode(self)   # 调用其父类的showrecode方法

class RetireRecord(Record):   # 定义一个子类
    def showrecode(self):   # 定义一个成员函数
        Record.showrecode(self)   # 调用其父类的showrecode方法
        print("retired worker")   # 该成员函数返回该类的成员变量

class ThisRecord(FemaleRecord, RetireRecord):   # 同时继承FemaleRecord, RetireRecord
    def showrecode(self):   # 定义一个成员函数
        print("the member detail as follow:")   # 该成员函数返回该类的成员变量
        FemaleRecord.showrecode(self)   # 调用其父类的showrecode
        RetireRecord.showrecode(self)

myc = ThisRecord("Anna", 62)
myc.showrecode()
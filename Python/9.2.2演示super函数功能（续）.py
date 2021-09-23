"""实例26：演示super函数功能（续）"""
class Record:   # 定义一个父类
    """A record class"""
    __Occupation = "scientist"   # 职业为科学家，私有变量
    def __init__(self, name, age):   # 定义该类的初始化函数
        self.name = name   # 将传入的参数值赋值给成员变量
        self.age = age
    def showrecode(self):   # 定义一个成员函数
        print("Occupation:", self.getOccupation())   # 该成员函数返回该类的成员变量
    def getOccupation(self):   # 返回私有变量的方法
        return self.__Occupation

class FemaleRecord(Record):   # 定义一个子类
    """A GirlRecord class"""
    def showrecode(self):   # 定义一个成员函数
        print(self.name, ':', self.age, ",female")
        super().showrecode()

class RetiredRecord:
    def showrecord(self):
        super().showrecord()
        print("retired worker")

class ThisRecord(FemaleRecord, RetiredRecord):
    def showrecode(self):
        print("the member detail as follow")
        super().showrecode()

myc = ThisRecord("Anna", 62)
myc.showrecode()
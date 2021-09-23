'''实例25：演示类的继承'''
class Record:   # 定义一个类
    ''' A record class'''   # 定义该类的说明字符串
    __Occupation = 'scientist'   # 职业为科学家，私有变量
    def __init__(self, name, age):   # 定义该类的初始化函数
        self.name = name   # 将传入的参数值赋值给该类的成员变量
        self.age = age

    def showrecode(self):   # 定义一个成员函数
        print('Occupation:', self.getOccupation())   # 该成员函数输出该类的成员变量

    def getOccupation(self):   # 返回私有变量的方法
        return self.__Occupation

class GirlRecord(Record):   # 定义一个类子类
    '''A GirlRecord class'''  # 定义类的说明字符串
    def showrecode(self):  # 定义一个成员函数
        Record.showrecode(self)   # 调用父类的方法
        print('the girl:', self.name, "'s age is", self.age)  # 该成员函数输出该类的成员变量

myc = GirlRecord("Anna", 42)   # 对GirlRecord实例化
myc.showrecode()   # 调用其showrecode方法
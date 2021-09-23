"""
工厂函数：
    Garyfun和Annafun都是工厂函数，分别对recorder函数进行封装
"""
def recoder(strname, age):    # 定义一个函数recorder
    print("姓名：", strname, "年龄：", age)

def Garyfun(age):    # 实现偏函数的功能
    strname = "Gary"    # 定义了本地作用域L下的变量
    return recoder(strname, age)    # 直接将固定的变量strname传入
Garyfun(35)    # 调用生成器函数，传入age=32

def Annafun(age):    # 再定义一个工厂函数Annafun
    strname = "Anna"    # 定义了本地作用域L下的变量
    return recoder(strname, age)    # 直接将固定的变量strname传入
Garyfun(20)    # 调用生成器函数，传入age=32


"""
闭合函数（closure）：又叫闭包函数
    实现方法是将名字作为自由变量，将原有recorder函数作为嵌套函数，通过一次函数的封装即可实现前面的功能
"""
def wrapperfun(strname):    # 闭合函数，strname作为自由变量
    def recoder(age):  # 定义一个嵌套函数recorder
        print("姓名：", strname, "年龄：", age)
    return recoder    # 返回recorder函数
fun = wrapperfun("Judy")    # 自由变量设为Judy
fun(14)    # 为age赋值
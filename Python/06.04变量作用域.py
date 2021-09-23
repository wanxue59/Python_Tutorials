"""
Python为变量分配了4个作用域，代表程序中出现同名变量的有效范围。
    ·L：本地作用域，被当前函数包括。
    ·E：上一层结构中def或lambda的本地作用域（其实就是函数嵌套的情况）。
    ·G：全局作用域,不被任何函数包括。
    ·B：内置作用域,是Python内部的命名空间。
"""

var = 1    # 在全局作用域G中定义变量var，值为1
def func1():    # 定义函数func1，其内部的函数体都属于作用域E
    var = 2    # 将作用域E中的变量var赋值为2
    def func2():    # 只有打印功能
        print("func2打印：", var)

    def func3():    # 在函数func1中定义函数func3，其内部的函数体都属于作用域L：只限于函数func3中
        var = 3    # 在L中定义变量var，值为3
        print("func3打印：", var)
    func2()    # 调用函数func2，打印作用域E（即函数func1）中的var值，2
    func3()    # 调用函数func3，将打印作用域L（即函数func3）中的var值，3

print("函数体外打印：", var)    # 打印全局作用域G中的var值，1
func1()    # 调用函数func1


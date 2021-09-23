# "global语句"
# a = 6
# b = 16
# def func():
#     global a    # 获得全局变量a
#     a = 15    # 将全局变量a的值改为15
#     b = 5    # b只在作用域L（即func函数）内有效，并不改变全局作用域G中的b值
#     print("func内：b =", b)
#
# print("全局变量: a = {}, b = {}".format(a, b))
# func()    # 调用函数func
# print("调用函数func后：a = {}, b = {}".format(a, b))


"nonlocal语句"
a = 2    # 在全局作用域G中定义变量a，值为1
def func1():    # 定义函数func1，其内部的函数体都属于作用域E
    a = 5    # 将作用域E中的变量a赋值为5
    def func2():    # 定义函数func
        nonlocal a    # 使用nonlocal关键字，引用外层（即作用域E，也就是func1中）的变量a
        a += 1    # 对func1内的变量a进行加一操作
    func2()    # 调用函数func2
    print("func1内：", a)
func1()    # 调用函数func1
print("全局变量：a =", a)    # 可以发现，即使调用函数，全局变量a也没有改变

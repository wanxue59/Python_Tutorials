"匿名函数"
r = lambda x, y: x*y    # 定义一个匿名函数实现x与y相乘
print("匿名函数实现2*3：", r(2, 3))


"匿名函数在函数中应用"
def sum_func(n):
    return lambda x: x+n    # 返回一个匿名函数
f = sum_func(15)    # 调用sum_func函数，传入实参15，得到一个匿名函数，函数体为x+15
print("在函数sum_func中调用匿名函数：", f(5))    # 计算15+5，并打印


"""
匿名函数与reduce函数组合应用
reduce(function, sequence, [initial])
    ·function：要回调的函数
    ·sequence：一个“系列”类型的数据
    ·第三个参数可选，是一个初始值
reduce的功能是按照参数sequence中的元素顺序，依次调用函数function，并且每次调用都会向其内传入两个参数：
一个是sequence系列中的当前元素，另一个是sequence系列中上一个元素在函数function中的返回值。
reduce一般用于归并性任务
"""
from functools import reduce
print(reduce(lambda x, y: x+y, range(1, 101)))    # reduce函数与匿名函数组合使用实现1~100相加


"""
匿名函数与map函数的组合应用
"""


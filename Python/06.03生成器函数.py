"""
迭代器与生成器的区别：
    ·迭代器是所有的内容都在内存里，使用next函数来依次往下遍历。--时间优先
    ·生成器不会把内容放到内存里，每次调用next函数时，返回的都是本次计算出来的那个元素，用完之后立刻销毁。--空间优先

生成器（Generator）函数：
    生成器函数是一种特殊的函数，是用来创建生成器对象的工具。生成器函数使用yield语句返回，返回一个生成器对象。
"""
def Reverse(data):    # 定义一个函数实现字符串反转
    for idx in range(len(data)-1, -1, -1):
        yield data[idx]    # 使用yield返回具体的一个元素
for c in Reverse('Python'):    # 使用for循环迭代Reverse返回的生成器对象
    print(c, end=' ')
print("\n")

"""
生成器表达式
生成器表达式与for循环列表表达式的区别：
    生成器表达式外层是圆括号；而for循环列表推导式外层是方括号
"""
print("for循环列表推导式：")
mylist = [x*x for x in range(5)]    # for循环列表推导式
for i in mylist:
    print(i)
print("\n")
print("生成器表达式：")
mygen = (x*x for x in range(5))    # 生成器表达式
for i in mygen:
    print(i)
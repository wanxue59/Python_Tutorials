"""
try...except...语句后面还可以跟else语句。当没有异常发生时，将执行else语句
"""
while(1):
    try:
        x = int(input("请输入一个除数："))  # 等待输入一个数
        print("30除以{0}等于{1}".format(x, 30 / x))
    except (ZeroDivisionError, ValueError):  # 同时捕获ZeroDivisionError和ValueError异常
        print("输入错误，请重新输入")
        continue
    else:
        print("byebye!")
        break
"""
except关键字还可以同时接收多个异常。具体的写法是在except后面加个括号，将要接收的异常当成参数传入
"""
try:
    x = int(input("请输入一个除数："))    # 等待输入一个数
    print("30除以{0}等于{1}".format(x, 30/x))
except (ZeroDivisionError,ValueError):    # 同时捕获ZeroDivisionError和ValueError异常
    print("输入错误，请重新输入")
"""
通过except后面跟着Exception as e语句，可得到异常类型e
"""
while(1):
    try:
        x = int(input("请输入一个除数："))  # 等待输入一个数
        print("30除以{0}等于{1}".format(x, 30 / x))
        break
    except Exception as e:  # 捕获未知异常
        print(e)
        print("其他异常")
        continue
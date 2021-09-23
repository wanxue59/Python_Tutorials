"""
    创建异常又叫抛出异常（或触发异常），是主动向系统报出的异常，使用关键字raise来实现，具体写法为：
raise [Exception [, args [, traceback]]]
    Exception：异常参数值，指代异常的类型，该参数是可选的，默认为None
    traceback：可选（实际中很少用），代表所要跟踪的异常对象
"""
while(1):
    try:
        x = int(input("请输入一个除数："))  # 等待输入一个数
        if x == 0:
            raise ValueError("输入错误：0不能做除数")
        print("30除以{0}等于{1}".format(x, 30 / x))
        break
    except Exception as e:
        print(e)
    except ZeroDivisionError:    # 捕获ZeroDivisionError异常
        print("除数不能等于0，请重新输入......")
        continue
    except:
        print("其他异常......")
        continue
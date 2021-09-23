"""
一个try语句可以有多条except语句，用以指定不同的异常，但至多只有一个会被执行
"""
while(1):
    try:
        x = int(input("请输入一个除数："))  # 等待输入一个数
        print("30除以{0}等于{1}".format(x, 30/x))
        break
    except ValueError:  # 捕获ValueError异常
        print("输入了无效的整数。重新输入......")
        continue
    except ZeroDivisionError:  # 捕获ZeroDivisionError异常
        print("除数不能等于0，重新输入......")
        continue
    except:    # 捕获其他异常
        print("其他异常")
        continue
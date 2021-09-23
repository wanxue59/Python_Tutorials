"""
    模块sys中有两个函数可以返回异常的全部信息：exc_into和last_traceback。exc_into会将当前的异常
信息以元组的类型返回，元组内分别包含：
    Type：异常类型的名称
    value：捕获到的异常实例
    traceback：一个traceback对象
    要查看traceback对象的内容，需要导入traceback模块，调用traceback模块中的print_tb方法，并将
sys.exc_into输出的traceback对象传入。print_tb方法专用于显示traceback对象的内容；调用traceback
模块中的print_exc方法，可以直接将异常内容打印出来
"""
import sys
import traceback
while(1):
    try:
        x = int(input("请输入一个除数："))  # 等待输入一个数
        print("30除以{0}等于{1}".format(x, 30 / x))
        break
    except:
        print(sys.exc_info())  # 捕获其他异常
        traceback.print_tb(sys.exc_info()[2])    # 显示traceback对象的内容，红色字体显示
        traceback.print_exc()    # 直接将异常内容打印出来
        print("其他异常......")
        continue
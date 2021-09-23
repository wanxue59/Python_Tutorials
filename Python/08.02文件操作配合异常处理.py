"""
8.3  实例21：带有异常处理的文件操作
实例描述：
    对文件分别进行写入和读取操作，并且都使用try/except进行异常处理，最终在finally中进行关闭。
    （1）在第一个try里面，以二进制形式打开一个文件，以文本的方式向里面写入一个字符串。使用except
对try里面的异常进行捕获。最终在finally中对文件进行关闭。
    （2）在第二个try里面，以文本的方式打开一个文件，并读取里面的内容。使用except对里面的异常进行
捕获。最终在finally中对文件进行关闭。
"""
try:    # 第一个try语句
    f = open(r"D:\PyCharm_Code\Data\test\test.txt", 'wb+')   # 以二进制的形式打开一个文件
    f.write("I like Python!")    # 以文本的方式写入一个用二进制打开的文件，会报错
except Exception as e:    # 将错误异常捕获
    print(e)
    f.write(b"I like Python!")    # 以二进制的形式写入
finally:
    f.close()    # 关闭文件


try:    # 第二个try语句
    f = open(r"D:\PyCharm_Code\Data\test\test.txt", 'r+')
    for line in f:    # 直接使用for循环读取文件
        print(line)    # 将文件中的内容打印出来
finally:
    f.close()    # 关闭文件
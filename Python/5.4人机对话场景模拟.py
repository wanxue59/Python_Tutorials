# 人机对话场景模拟
getstr = ''   # 定义一个空字符串，用来接收输入
while("Bye" != getstr):
    if '' == getstr:   # 如果输入字符为空，输出欢迎语句
        print("hello! Password")
    getstr = input("请输入字符，并按Enter键结束：")
    if 'hello' == getstr.strip():   # 如果输入字符串为hello，启动对话服务
        print("How are you today?")
        getstr = "start"   # 将getstr设为start，标志是启动对话服务
    elif 'go away' == getstr.strip():   # 如果输入的是go away，则退出
        print("sorry! bye-bye")
        break   # 使用break语句退出循环
    elif 'pardon' == getstr.strip():   # 如果输入的是pardon，请重新再输入一次
        getstr = ''
        continue   # 结束本次执行，开始循环下一次执行
    else:
        pass   # 什么也不做，保持程序的完整性

    if 'start' == getstr:   # 如果getstr为start，启动对话服务
        print("...init dialog-serving...")   # 伪代码，打印一些语句，表明启动了对话服务
        print("...one thing...")
        print("...two thing...")
        print("......")
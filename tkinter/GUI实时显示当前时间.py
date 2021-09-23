import tkinter
import time
def gettime():
    timestr = time.strftime("%Y-%m-%d %H:%M:%S")    # 获取当前时间并转为字符串
    lb.configure(text=timestr)    # 重新设置标签文本
    root.after(1000, gettime)    # 每隔一秒调用函数gettime自身获取时间


root = tkinter.Tk()
root.title('电子时钟')
lb = tkinter.Label(root, text='', fg='red', font=("黑体", 21))    # 设置字体大小颜色
lb.pack()
gettime()
root.mainloop()
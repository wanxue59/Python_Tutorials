"""
简单说明：
    Button（按钮）部件是一个标准的Tkinter窗口部件，用来实现各种按钮。按钮能够包含文本或图象，并且你能够将
按钮与一个Python函数或方法相关联。当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。按钮仅能显示一种
字体，但是这个文本可以跨行。另外，这个文本中的一个字母可以有下划线，例如标明一个快捷键。默认情况，Tab键用
于将焦点移动到一个按钮部件。

什么时候用按钮部件：
    简言之，按钮部件用来让用户说“马上给我执行这个任务”，通常我们用显示在按钮上的文本或图象来提示。按钮通
常用在工具条中或应用程序窗口中，并且用来接收或忽略输入在对话框中的数据。关于按钮和输入的数据的配合，可以
参看Checkbutton和Radiobutton部件。

如何创建：
    普通的按钮很容易被创建，仅仅指定按钮的内容（文本、位图、图象）和一个当按钮被按下时的回调函数即可：
b = tk.Button(window, text="hit me", command=hit_me)
    没有回调函数的按钮是没有用的，当你按下这个按钮时它什么也不做。你可能在开发一个应用程序的时候想实现
这种按钮，比如为了不干扰你的beta版的测试者：
b = tk.Button(window, text="Help", command=DISABLED)
"""

import tkinter as tk  # 使用Tkinter前需要先导入

##### 第1步，实例化object，建立窗口window #####
window = tk.Tk()

##### 第2步，给窗口的可视化起名字 #####
window.title('My Window')

##### 第3步，设定窗口的大小(长 * 宽) #####
window.geometry('500x300')  # 这里的乘是小写字母x

##### 第4步，在图形界面上设定标签 #####
"""将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上"""
l = tk.Label(master=window,    #  框架的父容器:创建的窗口对象
             anchor='center',    # 文本或图像在背景内容区的位置，可选值(n,s,w,e,ne,nw,sw,se,center)
             text='你好！this is Tkinter',    # 标签的文本内容
             bg='green',    # 标签的背景颜色
             fg='white',    # 标签文本的字体颜色
             font=('Arial', 12),    # 标签文本的字体设置
             width=30, height=2)    # 文本的长和高，比如height=2，就是标签有2个字符这么高

##### 第5步，放置标签 #####
l.pack()    # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();

##### 第6步，主窗口循环显示 #####
window.mainloop()
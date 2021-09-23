# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
"""
简单说明：　　
    Entry是tkinter类中提供的的一个单行文本输入域，用来输入显示一行文本，收集键盘输入（类似HTML中的text）。

什么时候用：
    需要用户输入用户信息时，比如我们平时使用软件、登录网页时，用户交互界面让我们登录账户信息等时候可以用到。
"""

import tkinter as tk  # 使用Tkinter前需要先导入

##### 第1步，实例化object，建立窗口window #####
window = tk.Tk()

##### 第2步，给窗口的可视化起名字 #####
window.title('My Window')

##### 第3步，设定窗口的大小(长 * 宽) #####
window.geometry('500x300')  # 这里的乘是小写字母x

##### 第4步，在图形界面上设定输入框控件entry并放置控件 #####
e1 = tk.Entry(master=window,    #  按钮的父容器：创建的窗口对象
              show=None,    # 指定文本框内容显示为字符，值随意，满足字符即可，None表示显示成明文形式
              font=('Arial', 14))    # 文本字体
e2 = tk.Entry(master=window,    #  按钮的父容器：创建的窗口对象
              show='*',    # 指定文本框内容显示为字符，值随意，满足字符即可，'*'表示显示成密文形式
              font=('Arial', 14))    # 文本字体
e1.pack()
e2.pack()

##### 第5步，主窗口循环显示 #####
window.mainloop()
"""
简单说明：　　
　　Text是tkinter类中提供的的一个多行文本区域，显示多行文本，可用来收集(或显示)用户输入的文字(类似HTML
中的textarea)，格式化文本显示，允许你用不同的样式和属性来显示和编辑文本，同时支持内嵌图象和窗口。
什么时候用：
　　在需要显示编辑用户、产品多行信息时，比如显示用户详细描述文字，产品简介等等，支持随时编辑。
"""
import tkinter as tk  # 使用Tkinter前需要先导入

##### 第1步，实例化object，建立窗口window #####
window = tk.Tk()

##### 第2步，给窗口的可视化起名字 #####
window.title('My Window')

##### 第3步，设定窗口的大小(长 * 宽) #####
window.geometry('500x300')  # 这里的乘是小写字母x

##### 第4步，在图形界面上设定输入框控件entry并放置控件 #####
e = tk.Entry(master=window,    #  按钮的父容器：创建的窗口对象
             font=None,    # 字体，默认值
             show=None)   # 指定文本框内容显示为字符，值随意，满足字符即可，None表示显示成明文形式
e.pack()


##### 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为  #####
#####       Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）      #####
def insert_point():  # 在鼠标焦点（光标）处插入输入内容
    var = e.get()
    t.insert('insert', var)


def insert_end():  # 在文本框内容最后接着插入输入内容
    var = e.get()
    t.insert('end', var)


##### 第6步，创建并放置两个按钮分别触发两种情况 #####
b1 = tk.Button(master=window,    # 按钮的父容器
              text='insert point',    # 按钮上的文字
              font=None,    # 按钮文字的字体设置，可省略
              width=10, height=1,    # 按钮的宽度和高度
              command=insert_point)    # 按钮关联的函数，当按钮被点击时，执行该函数
b1.pack()
b2 = tk.Button(master=window,    # 按钮的父容器
              text='insert point',    # 按钮上的文字
              font=None,    # 按钮文字的字体设置
              width=10, height=1,    # 按钮的宽度和高度
              command=insert_end)    # 按钮关联的函数，当按钮被点击时，执行该函数
b2.pack()

##### 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度 #####
t = tk.Text(window, height=3)
t.pack()

##### 第8步，主窗口循环显示 #####
window.mainloop()
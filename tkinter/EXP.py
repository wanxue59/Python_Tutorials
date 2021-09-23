from tkinter import ttk
import tkinter as tk

##### 第1步，实例化object，建立窗口window #####
window = tk.Tk()

##### 第2步，给窗口的可视化起名字 #####
window.title('My Window')

##### 第3步，设定窗口的大小(长 * 宽) #####
window.geometry('500x300')  # 这里的乘是小写字母x


choose_channel_lb = tk.Label(window, text="通道:", width=8, height=1)
choose_channel_lb.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

choose_channel_var = tk.StringVar()
choose_channel_var.set(str(4).zfill(2))
choose_channel_list = [str(i).zfill(2) for i in range(30)]
choose_channel_box = ttk.Combobox(master=window,
                                  state='readonly',
                                  textvariable=choose_channel_var,
                                  values=choose_channel_list,
                                  width=3)
choose_channel_box.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
window.mainloop()
print(choose_channel_var.get())
#coding=UTF-8
"""
filedialog.asksaveasfilename() # 选择以什么文件名保存，返回文件名
filedialog.asksaveasfile() # 选择以什么文件保存，创建文件并返回文件流对象
filedialog.askopenfile() # 选择打开什么文件，返回IO流对象
filedialog.askdirectory() # 选择目录，返回目录名
filedialog.askopenfilenames() # 选择打开多个文件，以元组形式返回多个文件名
filedialog.askopenfiles() # 选择打开多个文件，以列表形式返回多个IO流对象
"""

import tkinter as tk
import tkinter.filedialog as tkFileDialog
from tkinter import constants

class TkFileDialogExample(tk.Frame):
    """
    tkinter.filedialog模块简介示例
    """
    def __init__(self, root):

        tk.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': constants.BOTH, 'padx': 5, 'pady': 5}

        # define buttons
        tk.Button(self, text='askopenfile', command=self.askopenfile).pack(**button_opt)
        tk.Button(self, text='askopenfilename', command=self.askopenfilename).pack(**button_opt)
        tk.Button(self, text='asksaveasfile', command=self.asksaveasfile).pack(**button_opt)
        tk.Button(self, text='asksaveasfilename', command=self.asksaveasfilename).pack(**button_opt)
        tk.Button(self, text='askdirectory', command=self.askdirectory).pack(**button_opt)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'

        # This is only available on the Macintosh, and only when Navigation Services are installed.
        #options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        #options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'

    def askopenfile(self):

        """Returns an opened file in read mode."""

        print("askopenfile: ", tkFileDialog.askopenfile(mode='r', **self.file_opt))
        return tkFileDialog.askopenfile(mode='r', **self.file_opt)

    def askopenfilename(self):

        """Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        print("askopenfilename: ", filename)

        # open file on your own
        if filename:
            return open(filename, 'r')

    def asksaveasfile(self):

        """Returns an opened file in write mode."""

        return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)

    def asksaveasfilename(self):

        """Returns an opened file in write mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = tkFileDialog.asksaveasfilename(**self.file_opt)

        # open file on your own
        if filename:
            return open(filename, 'w')

    def askdirectory(self):

        """Returns a selected directoryname."""
        print("askdirectory: ", tkFileDialog.askdirectory(**self.dir_opt))

        return tkFileDialog.askdirectory(**self.dir_opt)

if __name__ == '__main__':
    root = tk.Tk()
    TkFileDialogExample(root).pack()
    root.mainloop()

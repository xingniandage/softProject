from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from abc import ABCMeta,abstractmethod

class CheckMailWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("主页")
        self.geometry("900x640+180+80")
        self.resizable(0, 0)# 窗体大小不允许变，两个参数分别代表x轴和y轴
        self["bg"] = "white"
        self.setup_UI()

    def setup_UI(self):
        self.Label_addressee = Label(self, text="收件人:", style="user.TLabel")
        self.Label_content = Label(self, text="内容:", style="user.TLabel")

        self.Entry_addressee = Entry(self, width=24)

        self.writetext = Text(self, height=20, width=100)

        self.Button_send = Button(self, text="下一条", width=20, command=self.NextMail)  ###绑定函数

        # 布局

        self.Label_addressee.grid(row=0, column=0, sticky='nw', ipadx=5)
        self.Entry_addressee.grid(row=0, column=1, sticky='w')
        self.Label_content.grid(row=1, column=0, sticky='nw', ipadx=5)
        self.writetext.grid(row=2, column=0, sticky=E, columnspan=2, padx=20, pady=20, ipadx=8)
        self.Button_send.grid(row=3, column=1, sticky=E, pady=20, ipadx=5)
    # showinfo(message='the password is error')  # password错误处理函数
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from abc import ABCMeta,abstractmethod

class writeMailWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("写邮件")
        self.geometry("900x640+180+80")
        self.resizable(0, 0)# 窗体大小不允许变，两个参数分别代表x轴和y轴
        self["bg"] = "white"

        self.setup_UI()

    def setup_UI(self):
        self.Label_addressee = Label(self, text="收件人:", style="user.TLabel")
        self.Label_addressee.pack(side = LEFT,padx = 20,pady = 20)
        self.Entry_addressee = Entry(self,width = 24)
        self.Entry_addressee.pack(side = LEFT,padx = 20,pady = 20)
        self.writetext = Text(self, height=100, width=150)
        showinfo(message='the password is error')  # password错误处理函数
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from abc import ABCMeta,abstractmethod

import WriteMail
import CheckMail
class HomeWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("主页")
        self.geometry("900x640+180+80")
        self.resizable(0, 0)# 窗体大小不允许变，两个参数分别代表x轴和y轴
        self["bg"] = "white"

        self.setup_UI()

    def setup_UI(self):
        self.Button_write = Button(self, text="写邮件", width=20, command=self.WriteMail)  ###绑定函数
        self.Button_write.pack(expand="yes", padx=40, pady=20)
        self.Button_check = Button(self, text="查看邮件", width=20, command=self.CheckMail)  ###绑定函数
        self.Button_check.pack(expand="yes", padx=40, pady=20)

    def WriteMail(self):
        writeMailwindow = WriteMail.writeMailWindow()#跳转到WriteMail函数

    def CheckMail(self):
        checkMailWindow = CheckMail.CheckMailWindow()  # 跳转到CheckMail函数


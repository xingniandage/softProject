from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from abc import ABCMeta,abstractmethod
from main import manager
import WriteMail
import Manage
import CheckMail
class HomeWindow(Tk):
    def __init__(self,ismanager):
        super().__init__()
        self.title("主页")
        self.geometry("900x640+180+80")
        self.resizable(0, 0)# 窗体大小不允许变，两个参数分别代表x轴和y轴
        self.canvas=Canvas(self,highlightthickness=0)
        self.canvas.place(width=900,height=640)
        bg=PhotoImage(file='img/bg3.png')
        self.canvas.create_image(450,320,image=bg)
        self.ismanager=ismanager
        self.setup_UI()
        self.mainloop()
    def setup_UI(self):
        self.Style01 = Style()
        self.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="royalblue")
        self.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="royalblue")
        if self.ismanager==1:
            self.Button_check = Button(self, text="管理成员", width=20, command=self.ManageCounter,style='TButton')  ###绑定函数
            self.Button_check.pack(expand="yes", padx=40, pady=20)
        else:
            self.Button_write = Button(self, text="写邮件", width=20, command=self.WriteMail,style='user.TButton')  ###绑定函数
            self.Button_write.pack(expand="yes", padx=40, pady=20)
            self.Button_check = Button(self, text="查看邮件", width=20, command=self.CheckMail)  ###绑定函数
            self.Button_check.pack(expand="yes", padx=40, pady=20)

    def WriteMail(self):
        self.destroy()
        writeMailwindow = WriteMail.writeMailWindow()#跳转到WriteMail函数


    def CheckMail(self):
        self.destroy()
        checkMailWindow = CheckMail.CheckMailWindow()#跳转到CheckMail函数
    
    def ManageCounter(self):
        self.destroy()
        manageMailWindow = Manage.manageMailWindow()#跳转到管理员界面
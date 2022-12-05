from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
import global_var#引入全局变量文件
from abc import ABCMeta,abstractmethod
from main import manager
from main import users
class manageMailWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("管理")
        self.geometry("900x640+180+80")
        self.resizable(0, 0)# 窗体大小不允许变，两个参数分别代表x轴和y轴
        self.canvas = Canvas(self, highlightthickness=0)
        self.canvas.place(width=900, height=640)
        bg = PhotoImage(file='img/bg3.png')
        self.canvas.create_image(450, 320, image=bg)
        self.setup_UI()
        self.mainloop()

    def setup_UI(self):
        self.Style01 = Style()
        self.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="royalblue")
        self.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="royalblue")
        self.Label_addressee = Label(self, text="成员名：", style="user.TLabel")
        self.Label_addressee1 = Label(self, text="状态：", style="user.TLabel")
        self.Label_content = Label(self, text="内容:", style="user.TLabel")

        self.Entry_addressee = Entry(self,width = 24,style='TEntry')
        self.Entry_addressee1 = Entry(self,width = 10,style='TEntry')


        self.writetext = Text(self, height=12, width=100)

        self.Button_check =Button(self,text="查询",width=10, command=self.check)
        self.Button_delet =Button(self,text="删除用户",width=10, command=self.delet)
        self.Button_add =Button(self,text="添加用户",width=10, command=self.addcounter)
        self.Button_block =Button(self,text="冻结用户",width=10, command=self.block)
        self.Button_unblock =Button(self,text="解冻用户",width=10, command=self.unblock)
        self.Button_initmail =Button(self,text="清空邮箱",width=10, command=self.initmail)

        #布局

        self.Label_addressee.grid(row=0, column=0,sticky='nw', ipadx=5)
        self.Label_addressee1.grid(row=1, column=0,sticky='nw', ipadx=5)
        self.Entry_addressee.grid(row=0, column=1,sticky='w')
        self.Entry_addressee1.grid(row=1, column=1,sticky='w')
        self.Label_content.grid(row=2, column=0, sticky='nw', ipadx=5)
        self.writetext.grid(row=3, column=0, sticky=E,columnspan=2,padx=20,pady=20,ipadx=8)
        self.Button_check.grid(row=6, column=1, sticky='w',pady=20,ipadx=5,padx=80)

        self.Button_initmail.grid(row=6, column=0, sticky='w',pady=20,ipadx=5,padx=80)

        self.Button_delet.grid(row=4, column=0, sticky='w',pady=20,ipadx=5,padx=80)
        self.Button_add.grid(row=4, column=1, sticky='w',pady=20,ipadx=5,padx=80)
        self.Button_block.grid(row=5, column=0, sticky='w',pady=20,ipadx=5,padx=80)
        self.Button_unblock.grid(row=5, column=1, sticky='w',pady=20,ipadx=5,padx=80)
       # showinfo(message='the password is error')  # password错误处理函数
    def SendMail(self):
        receiver=self.Entry_addressee.get()
        print(receiver)
        content=self.writetext.get('1.0','end')
        if receiver!='2':
            showinfo(message='can not find the receiver')
        else:
            self.writetext.delete('1.0',"end")
            showinfo(message='send successfully!')
            str=receiver+'.txt'
            f = open(str,'a')
            content=content+'\n'
            f.write(content)
            f.close()
    def check(self):
        print("check")
        checker=self.Entry_addressee.get()
        print(checker)
        # print(manager.countername)
        if checker in manager.countername:
            self.Entry_addressee1.select_clear()
            index=manager.countername.index(checker)
            self.Entry_addressee1.insert('insert',manager.counters[index].issent)
            self.writetext.delete('1.0',"end")
            str = checker[-1]+".txt"
            a = open(str, 'r')
            for id_names in a:
                self.writetext.insert('insert', id_names)
            a.close()
        else:
            showinfo(message='No access')
    def delet(self):
        print("delet")
        deleter=self.Entry_addressee.get()
        print(deleter)
        if deleter in manager.countername:
            index=manager.countername.index(deleter)
            manager.rmcounter(manager.counters[index])
            showinfo(message='Delete successfully!')
        else:
            showinfo(message='No access')
    def addcounter(self):
        print('add')
        adder=self.Entry_addressee.get()
        print(adder)
        if adder in manager.countername:
            showinfo(message='Exit!')
        elif adder in users:
            if manager.addcounter(users[adder])==True:
                showinfo(message='Add successfully!')
            else:
                showinfo(message='Add fail')
        else:
            showinfo(message='Not exit!')
    def block(self):
        print('block')
        blocker=self.Entry_addressee.get()
        print(blocker)
        if blocker in manager.countername:
            index=manager.countername.index(blocker)
            manager.counters[index].issent=0
            showinfo(message='Block successfully!')
        else:
            showinfo(message='No access')
    def unblock(self):
        print('unblock')
        unblocker=self.Entry_addressee.get()
        print(unblocker)
        if unblocker in manager.countername:
            index=manager.countername.index(unblocker)
            if manager.counters[index].issent==1:
                showinfo(message='Unblocked!')
            else:
                manager.counters[index].issent=1
                showinfo(message='Unblock successfully!')
        else:
            showinfo(message='No access')
    def initmail(self):
        print('initmail')
        initmailer=self.Entry_addressee.get()
        print(initmailer)
        if initmailer in manager.countername:
            index=manager.countername.index(initmailer)
            if manager.initcounter(manager.counters[index])==1:
                showinfo(message='Init successfully!')
            else :
                showinfo(message='Init fail!')
        else:
            showinfo(message='No access')
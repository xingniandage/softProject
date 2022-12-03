from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from abc import ABCMeta,abstractmethod
import linecache
import global_var#引入全局变量文件
class CheckMailWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("主页")
        self.geometry("900x640+180+80")
        self.resizable(0, 0)# 窗体大小不允许变，两个参数分别代表x轴和y轴
        self["bg"] = "white"
        self.setup_UI()

    def setup_UI(self):

        self.Label_SumNum=Label(self,text="信件总数:", style="user.TLabel")
        self.Text_SumNum = Text(self, height=1,width=24)
        self.Label_num=Label(self,text="信件编号:", style="user.TLabel")
        self.Text_num = Text(self,height=1, width=24)
        self.Label_addressee = Label(self, text="发件人:", style="user.TLabel")
        self.Text_addressee = Text(self,height=1, width=24)
        self.Label_content = Label(self, text="内容:", style="user.TLabel")
        self.writetext = Text(self, height=20, width=100)

        self.Button_Pre = Button(self, text="上一条", width=20, command=self.PreMail)
        self.Button_send = Button(self, text="下一条", width=20, command=self.NextMail)  ###绑定函数


        self.SendFolder = Button(self,text="发件箱",width=20,command=self.SendFolder)
        self.ReceiveFolder = Button(self, text = "收件箱",width = 20,command=self.ReceiveFolder)


        # 布局
        self.Label_SumNum.grid(row=0, column=0, sticky='nw', ipadx=5)
        self.Text_SumNum.grid(row=0, column=1, sticky='w')
        self.Label_num.grid(row=1, column=0, sticky='nw', ipadx=5)
        self.Text_num.grid(row=1, column=1, sticky='w')
        self.Label_addressee.grid(row=2, column=0, sticky='nw', ipadx=5)
        self.Text_addressee.grid(row=2, column=1, sticky='w')
        self.Label_content.grid(row=3, column=0, sticky='nw', ipadx=5)
        self.writetext.grid(row=4, column=0, sticky=E, columnspan=2, padx=20, pady=20, ipadx=8)

        self.Button_Pre.grid(row=5, column=0, sticky=E, pady=20, ipadx=5)
        self.Button_send.grid(row=5, column=1, sticky=E, pady=20, ipadx=5)

        self.SendFolder.grid(row=6,column=0,sticky=E,pady=20,ipadx=8)
        self.ReceiveFolder.grid(row=6, column=1, sticky=E, pady=20, ipadx=8)

        row_len=0
        user=global_var.get_value('user')
        if user=='1':
            fobj = open('1.txt', 'r')
            row_len = len(fobj.readlines())
            fobj.close()
        elif user=='2':
            fobj = open('2.txt', 'r')
            row_len = len(fobj.readlines())
            fobj.close()
        else:
            showinfo(message='user is error')
        self.Text_SumNum.insert('insert',str(row_len))
        self.Text_num.insert('insert','0')

        global_var.set_value('folder','ReceiveFolder')
    # showinfo(message='the password is error')  # password错误处理函数
    def NextMail(self):

        if (global_var.get_value("folder") == "sendFolder"):
            # print("进入发件箱了...")

            strname = ''
            user = global_var.get_value('user')
            if user == '1':
                strname = '2.txt'
            elif user == '2':
                strname = '1.txt'
            else:
                showinfo(message='user is error')
            fobj = open(strname, 'r')
            row_len = len(fobj.readlines())
            nownum = self.Text_num.get('1.0', 'end')

            nownum = int(nownum)
            nownum += 1
            print(nownum)


            content = ''
            if nownum <= row_len and strname == '1.txt':
                content = linecache.getline(r'1.txt', nownum)
            if nownum <= row_len and strname == '2.txt':
                content = linecache.getline(r'2.txt', nownum)
            if len(content) > 0:
                self.Text_addressee.delete('1.0', "end")
                self.Text_num.delete('1.0', "end")
                self.writetext.delete('1.0', "end")

                self.Text_addressee.insert('insert', content[:1])
                self.Text_num.insert('insert', str(nownum))
                self.writetext.insert('insert', content[1:])
            if nownum > row_len:
                showinfo(message='read over')

        elif (global_var.get_value("folder") == "ReceiveFolder"):
            # print("进入收件箱了...")

            strname = ''
            user = global_var.get_value('user')
            if user == '1':
                strname = '1.txt'
            elif user == '2':
                strname = '2.txt'
            else:
                showinfo(message='user is error')
            fobj = open(strname, 'r')
            row_len = len(fobj.readlines())
            nownum = self.Text_num.get('1.0', 'end')

            nownum = int(nownum)
            nownum += 1
            print(nownum)


            content = ''
            if nownum <= row_len and strname == '1.txt':
                content = linecache.getline(r'1.txt', nownum)
            if nownum <= row_len and strname == '2.txt':
                content = linecache.getline(r'2.txt', nownum)
            if len(content) > 0:
                self.Text_addressee.delete('1.0', "end")
                self.Text_num.delete('1.0', "end")
                self.writetext.delete('1.0', "end")

                self.Text_addressee.insert('insert', content[:1])
                self.Text_num.insert('insert', str(nownum))
                self.writetext.insert('insert', content[1:])
            if nownum > row_len:
                showinfo(message='read over')

    def PreMail(self):

        if (global_var.get_value("folder") == "sendFolder"):
            # print("进入发件箱了...")

            strname = ''
            user = global_var.get_value('user')
            if user == '1':
                strname = '2.txt'
            elif user == '2':
                strname = '1.txt'
            else:
                showinfo(message='user is error')
            fobj = open(strname, 'r')
            row_len = len(fobj.readlines())
            nownum = self.Text_num.get('1.0', 'end')

            nownum = int(nownum)
            nownum -= 1
            print(nownum)


            content = ''
            if nownum >= 0 and strname == '1.txt':
                content = linecache.getline(r'1.txt', nownum)
            if nownum >= 0 and strname == '2.txt':
                content = linecache.getline(r'2.txt', nownum)
            if len(content) > 0:
                self.Text_addressee.delete('1.0', "end")
                self.Text_num.delete('1.0', "end")
                self.writetext.delete('1.0', "end")

                self.Text_addressee.insert('insert', content[:1])
                self.Text_num.insert('insert', str(nownum))
                self.writetext.insert('insert', content[1:])
            if nownum <= 0:
                showinfo(message='read over')

        elif (global_var.get_value("folder") == "ReceiveFolder"):
            # print("进入收件箱了...")

            strname = ''
            user = global_var.get_value('user')
            if user == '1':
                strname = '1.txt'
            elif user == '2':
                strname = '2.txt'
            else:
                showinfo(message='user is error')
            fobj = open(strname, 'r')
            row_len = len(fobj.readlines())
            nownum = self.Text_num.get('1.0', 'end')

            nownum = int(nownum)
            nownum -= 1
            print(nownum)

            content = ''
            if nownum >= 0 and strname == '1.txt':
                content = linecache.getline(r'1.txt', nownum)
            if nownum >= 0 and strname == '2.txt':
                content = linecache.getline(r'2.txt', nownum)
            if len(content) > 0:
                self.Text_addressee.delete('1.0', "end")
                self.Text_num.delete('1.0', "end")
                self.writetext.delete('1.0', "end")

                self.Text_addressee.insert('insert', content[:1])
                self.Text_num.insert('insert', str(nownum))
                self.writetext.insert('insert', content[1:])
            if nownum <= 0:
                showinfo(message='read over')

    def SendFolder(self):
        global_var.set_value('folder', 'sendFolder')
        print("现在是发件箱...")
        user = global_var.get_value('user')
        if user == '1':
            fobj = open('2.txt', 'r')
            row_len = len(fobj.readlines())
            fobj.close()
        elif user == '2':
            fobj = open('1.txt', 'r')
            row_len = len(fobj.readlines())
            fobj.close()
        else:
            showinfo(message='user is error')

        self.Text_SumNum.delete('1.0', "end")
        self.Text_addressee.delete('1.0', "end")
        self.Text_num.delete('1.0', "end")
        self.writetext.delete('1.0', "end")

        self.Text_SumNum.insert('insert', str(row_len))
        self.Text_addressee.insert('insert', "")
        self.Text_num.insert('insert',"0")
        self.writetext.insert('insert', "")

    def ReceiveFolder(self):

        global_var.set_value('folder', 'ReceiveFolder')
        print("现在是收件箱...")
        user = global_var.get_value('user')
        if user == '1':
            fobj = open('1.txt', 'r')
            row_len = len(fobj.readlines())
            fobj.close()
        elif user == '2':
            fobj = open('2.txt', 'r')
            row_len = len(fobj.readlines())
            fobj.close()
        else:
            showinfo(message='user is error')

        self.Text_SumNum.delete('1.0', "end")
        self.Text_addressee.delete('1.0', "end")
        self.Text_num.delete('1.0', "end")
        self.writetext.delete('1.0', "end")

        self.Text_SumNum.insert('insert', str(row_len))
        self.Text_addressee.insert('insert', "")
        self.Text_num.insert('insert', "0")
        self.writetext.insert('insert', "")

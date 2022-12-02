from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from abc import ABCMeta,abstractmethod

import Home


class IloginView(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def setUserNameError(self):
        pass
    def setPasswordError(self):
        pass
    def navigateToHome(self):
        pass

class IonLoginFinishedListener(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def onUserNameError(self):
        pass
    def onPasswordError(self):
        pass
    def onSuccess(self):
        pass

class loginActivity(IloginView):
    def setPasswordError(self):
        showinfo(message='the password is error')#password错误处理函数

    def setUserNameError(self):
        showinfo(message='the user is invalid')#user错误处理函数

    def navigateToHome(self):
        if __name__ == '__main__':
            home_window = Home.HomeWindow()#跳转到home函数

class loginPresenter(IonLoginFinishedListener):
    def onUserNameError(self,user):
        if (user != user1.name) and (user != user2.name):
            return True
        else:
            return False
    def onPasswordError(self,user,password):
        if ((user == user1.name) and (password != user1.pw)) or ((user == user2.name) and (password != user2.pw)):
            return True
        else:
            return False
    def onSuccess(self,user,password):
        if (user == user1.name and password == user1.pw) or (user == user2.name and password == user2.pw):
            return True
        else:
            return False



class User():
    def __init__(self,name,pw):
        self.name=name
        self.pw=pw
    def isLogin(self,user):
        if self.name==user.name and self.pw==user.pw:
            return True
        else:
            return False

user1=User('Adam','5201314')
user2=User('Eva','414414')



class LoginWindow(Tk):
    """
    创建登录窗体的GUI界面已经登录的方法
    """
    def __init__(self):
        super().__init__()  # 先执行tk这个类的初始化
        self.title("登录界面")
        # self.geometry("620x420")
        self.resizable(0,0) # 窗体大小不允许变，两个参数分别代表x轴和y轴
        self.iconbitmap("."+os.sep+"img"+os.sep+"mail.ico")
        # self["bg"] = "royalblue"
        # 加载窗体
        self.setup_UI()

    def setup_UI(self):
        # ttk中控件使用style对象设定
        self.Style01 = Style()
        self.Style01.configure("user.TLabel",font = ("华文黑体",20,"bold"),foreground = "royalblue")
        self.Style01.configure("TEntry",font = ("华文黑体",20,"bold"))
        self.Style01.configure("TButton",font = ("华文黑体",20,"bold"),foreground = "royalblue")
        # 创建一个Label标签展示图片
        self.Login_image = ImageTk.PhotoImage(file = "."+os.sep+"img"+os.sep+"bg2.jpg")
        self.Label_image = Label(self,image = self.Login_image)
        self.Label_image.pack(padx = 10,pady = 10)
        # 创建一个Label标签 + Entry   --- 用户名
        self.Label_user = Label(self,text = "用户名:", style = "user.TLabel")
        self.Label_user.pack(side = LEFT,padx = 20,pady = 20)
        self.Entry_user = Entry(self,width = 24)
        self.Entry_user.pack(side = LEFT,padx = 20,pady = 20)
        # 创建一个Label标签 + Entry   --- 密码
        self.Label_password = Label(self, text = "密码:", style = "user.TLabel")
        self.Label_password.pack(side = LEFT,padx = 20,pady = 20)
        self.Entry_password = Entry(self, width=24,show = "*")
        self.Entry_password.pack(side = LEFT,padx = 20,pady = 20)
        # 创建一个按钮    --- 登录
        self.Button_login = Button(self,text = "登录",width = 4,command=self.login)
        self.Button_login.pack(side = LEFT,padx = 40,pady = 20)
    def login(self):
        user = self.Entry_user.get()
        password = self.Entry_password.get()
        if loginPresenter.onUserNameError(self,user):
            loginActivity.setUserNameError(self)
            if loginPresenter.onPasswordError(self,user,password):
                loginActivity.setPasswordError(self)
        if loginPresenter.onSuccess(self,user,password):
            self.destroy()
            loginActivity.navigateToHome(self)#执行此函数


if __name__ == '__main__':
    this_login = LoginWindow()
    this_login.mainloop()
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from abc import ABCMeta,abstractmethod

class HomeWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("主页")
        self.geometry("900x640+180+80")
        self.resizable(0, 0)# 窗体大小不允许变，两个参数分别代表x轴和y轴
        self["bg"] = "royalblue"



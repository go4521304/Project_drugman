from cefpython3 import cefpython as cef
from tkinter import *

class Search:
    def __init__(self, window):
        window.config(bg='light blue')

        self.frame = Frame(window, width=850,
                                height=880,
                                highlightthickness=3,
                                bg='light blue',
                                highlightbackground='white',
                                highlightcolor='white')

        # image = PhotoImage(file='./resource/home.png')
        # Button(window, image=image, command=self.home, relief='flat',bg='white')

        self.frame.place(x=10, y=10)  

    # def home(self):
    #     self.browser.LoadUrl('https://www.health.kr/searchIdentity/search.asp')

    def showWeb(self):
        self.window_info = cef.WindowInfo(self.frame.winfo_id())
        self.window_info.SetAsChild(self.frame.winfo_id(), [3, 3, 847, 877])
        self.browser = cef.CreateBrowserSync(self.window_info, url='https://www.health.kr/searchIdentity/search.asp')
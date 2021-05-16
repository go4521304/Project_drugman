# 이 파일은 GUI를 띄우는 파일입니다.

from tkinter import *

class Main_GUI:
    def Draw_P(self): # Parmachy
        pass
    def Draw_M(self): # Medicine
        pass

    def __init__(self):
        window = Tk()
        window.title("약 좀 주세요 ~약 먹을 시간~")

        self.canvas = Canvas(window,bg = 'white', width = 1200, height = 900)
        self.canvas.pack()

       

        window.mainloop()

if __name__ == "__main__":
    Main_GUI()
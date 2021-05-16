# 이 파일은 GUI를 띄우는 파일입니다.

from tkinter import *

class Main_GUI:
    def Draw_P(self): # Parmachy
        print("약국")
    def Draw_M(self): # Medicine
        print("약")

    def __init__(self):
        window = Tk()
        window.title("약 좀 주세요 ~약 먹을 시간~")

        self.canvas = Canvas(window,bg = 'white', width = 1200, height = 900)
        self.canvas.pack()

        self.Pharmachy = Button(window, text='약', command=self.Draw_M)
        self.Medicine = Button(window, text='국', command=self.Draw_P)

        # 디버그용 그리드
        for i in range(12):
            for j in range(9):
                self.canvas.create_line(100*i,0,100*i,900)
                self.canvas.create_line(0,100*j,1200,100*j)

        self.Pharmachy.place(x=0,y=0)

        window.mainloop()

if __name__ == "__main__":
    Main_GUI()
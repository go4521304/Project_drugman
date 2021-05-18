# 이 파일은 GUI를 띄우는 파일입니다.

from tkinter import *

class Main_GUI:
    def Draw_P(self): # Parmachy
        self.canvas_C.delete('m')
        self.canvas_C.create_rectangle(20,20,850,880,outline="yellow",tags='p',width = 5)
    def Draw_M(self): # Medicine
        self.canvas_C.delete('p')
        self.canvas_C.create_rectangle(20,20,850,880,outline = "blue",tags='m',width = 3)

    def __init__(self):
        # 창 기본설정 (타이틀, 크기, 크기조정 불가)
        window = Tk()
        window.title("약 좀 주세요 ~약 먹을 시간~")
        window.geometry('1200x900')
        window.resizable(False, False)
        

        # 프레임 분리
        frameB = Frame(window, bg='white', width=330, height=900)
        frameB.grid(row=0, column=0)
        frameC = Frame(window, bg='white', width=870, height=900)
        frameC.grid(row=0, column=1)
        

        # 캔버스 생성
        self.canvas_B = Canvas(frameB, width=330, height=900)
        self.canvas_B.place(x=0, y=0)
        self.canvas_C = Canvas(frameC,bg='white', width=870, height=900)
        self.canvas_C.place(x=0, y=0)

        # 이미지 관리용 dict 생성
        image = {}

        image['medicine'] = PhotoImage(file='./resource/medicine.png')
        image['pharmacy'] = PhotoImage(file='./resource/pharmacy.png')
        self.Pharmachy = Button(frameB, text='약', image=image['medicine'], command=self.Draw_M)
        self.Medicine = Button(frameB, text='국', image=image['pharmacy'], command=self.Draw_P)

        # 디버그용 그리드
        for i in range(4):
            for j in range(9):
                self.canvas_B.create_line(100*i,0,100*i,900,fill = "gray")
                self.canvas_B.create_line(0,100*j,330,100*j,fill = "yellow")
        for i in range(9):
            for j in range(9):
                self.canvas_C.create_line(100*i,0,100*i,900,fill = "gray")
                self.canvas_C.create_line(0,100*j,870,100*j,fill = "red")


        self.Pharmachy.place(x=60,y=250)
        self.Medicine.place(x=60,y=550)
        #1
        window.mainloop()

if __name__ == "__main__":
    Main_GUI()
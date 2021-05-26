# 이 파일은 GUI를 띄우는 파일입니다.

from tkinter import *
import medicine as MD

class Main_GUI:
    def Draw_P(self): # Parmachy
        for widgets in self.frameC.winfo_children():
            widgets.destroy()
        MD.Medi(self.frameC)

    def Draw_M(self): # Medicine
        for widgets in self.frameC.winfo_children():
            widgets.destroy()
        MD.Medi(self.frameC)
        # self.canvas_C.delete('p')
        # self.canvas_C.create_rectangle(20,20,850,880,outline = "blue",tags='m',width = 3)

    def __init__(self):
        # 창 기본설정 (타이틀, 크기, 크기조정 불가)
        self.window = Tk()
        self.window.title("약 좀 주세요 ~약 먹을 시간~")
        self.window.geometry('1200x900')
        self.window.resizable(False, False)
        

        # 프레임 분리
        frameB = Frame(self.window, bg='white', width=330, height=900)
        frameB.grid(row=0, column=0)

        self.frameC = Frame(self.window, bg='white', width=870, height=900)
        self.frameC.grid(row=0, column=1)

        # 캔버스 생성
        self.canvas_B = Canvas(frameB, width=330, height=900)
        self.canvas_B.place(x=0, y=0)
        self.canvas_C = Canvas(self.frameC,bg='white', width=870, height=900)
        self.canvas_C.place(x=0, y=0)

        # 이미지 관리용 dict 생성
        image = {}

        image['medicine'] = PhotoImage(file='./resource/medicine.png')
        image['pharmacy'] = PhotoImage(file='./resource/pharmacy.png')
        self.Pharmachy = Button(frameB, text='약', image=image['medicine'], command=self.Draw_M)
        self.Medicine = Button(frameB, text='국', image=image['pharmacy'], command=self.Draw_P)

        # 디버그용 그리드
        #for i in range(4):
        #    for j in range(9):
        #        self.canvas_B.create_line(100*i,0,100*i,900,fill = "gray")
        #        self.canvas_B.create_line(0,100*j,330,100*j,fill = "yellow")
        #for i in range(9):
        #    for j in range(9):
        #        self.canvas_C.create_line(100*i,0,100*i,900,fill = "gray")
        #        self.canvas_C.create_line(0,100*j,870,100*j,fill = "red")


        self.Pharmachy.place(x=60,y=250)
        self.Medicine.place(x=60,y=550)
        #1
        self.window.mainloop()

if __name__ == "__main__":
    Main_GUI()
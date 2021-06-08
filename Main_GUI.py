# 이 파일은 GUI를 띄우는 파일입니다.

from tkinter import *
import medicine as MD
import pharmacy as PM

class Main_GUI:
    def Draw_P(self): # Parmachy
        self.framePM.tkraise()

    def Draw_M(self): # Medicine
        self.frameMD.tkraise()

    def __init__(self):
        # 창 기본설정 (타이틀, 크기, 크기조정 불가)
        self.window = Tk()
        self.window.title("약 좀 주세요 ~약 먹을 시간~")
        self.window.geometry('1200x900')
        self.window.resizable(False, False)

        # 프레임 분리
        frameB = Frame(self.window, bg='white', width=330, height=900, highlightthickness=3, highlightbackground='light blue', highlightcolor='light blue')
        frameB.place(x=0, y=0)

        # Medicine 프레임
        self.frameMD = Frame(self.window, width=870, height=900)
        self.frameMD.place(x=330, y=0)
        MD.Medi(self.frameMD)

        # Pharmacy 프레임
        self.framePM = Frame(self.window, width=870, height=900)
        self.framePM.place(x=330, y=0)
        PM.Pharm(self.framePM)

        # 초기화면 프레임
        self.frameS = Frame(self.window, bg='white', width=870, height=900)
        self.frameS.place(x=330, y=0)

        # 캔버스 생성

        # self.canvas_B = Canvas(frameB, width=330, height=900, bg='white')
        # self.canvas_B.place(x=0, y=0)
        
        self.canvas_C = Canvas(self.frameS,bg='light gray', width=870, height=920)
        self.canvas_C.place(x=0, y=-10)
        # self.canvas_B.create_rectangle(10,10,320,890,width=7,outline='light blue')
        #self.canvas_C.create_rectangle(20, 20, 850, 900, width=7, outline='light blue')
        # 이미지 관리용 dict 생성
        image = {}

        image['medicine'] = PhotoImage(file='./resource/medicine.png')
        image['pharmacy'] = PhotoImage(file='./resource/pharmacy.png')
        image['textImg'] = PhotoImage(file='./resource/text.png')
        self.Pharmachy = Button(frameB, text='약', image=image['medicine'], command=self.Draw_M,relief='flat', bg='white')
        self.Medicine = Button(frameB, text='국', image=image['pharmacy'], command=self.Draw_P,relief='flat', bg='white')
        self.Text = Button(self.canvas_C, image=image['textImg'],relief='flat')
        #self.textImg = Button(self.frameS, text='글', image=image['textImg'], relief='flat')
        # 디버그용 그리드
        #for i in range(4):
        #    for j in range(9):
        #        self.canvas_B.create_line(100*i,0,100*i,900,fill = "gray")
        #        self.canvas_B.create_line(0,100*j,330,100*j,fill = "yellow")
        #for i in range(9):
        #    for j in range(9):
        #        self.canvas_C.create_line(100*i,0,100*i,900,fill = "gray")
        #        self.canvas_C.create_line(0,100*j,870,100*j,fill = "red")


        self.Pharmachy.place(x=35,y=300)
        self.Medicine.place(x=35,y=600)


        #self.textImg.place(x=0,y=50)
        #1
        self.window.mainloop()

if __name__ == "__main__":
    Main_GUI()
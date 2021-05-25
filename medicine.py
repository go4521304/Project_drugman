from io import BytesIO
from PIL import Image as P
from PIL import ImageTk
from tkinter import *
from tkinter import font
from tkinter import ttk
from collections import ChainMap
import tkinter.messagebox
from medicine_conn import *
import requests

class Medi:
    pageNum = 0
    
    def __init__(self) -> None:
        window = Tk()
        window.title('Medicine')
        window.geometry('600x800')
        window.config(bg='light green')

        self.medi = Medicine()

        # 글꼴
        fontSet = font.Font(family='Consolas', weight='normal', size=15)

        # 버튼용 글꼴
        fontSet_Btn = font.Font(family='Consolas', weight='normal', size=12)

        # 상단부 영역
        frameTop = Frame(window,width=580,
                                height=85,
                                highlightthickness=3,
                                bg='light blue',
                                highlightbackground='white',
                                highlightcolor='white')
        frameTop.place(x=10, y=10)          # 좌표

        # 하단부 영역
        frameBottom = Frame(window, width=580,
                                    height=680,
                                    highlightthickness=3,
                                    bg='light blue',
                                    highlightbackground='white',
                                    highlightcolor='white')
        frameBottom.place(x=10, y=110)      # 좌표

        ###################### 상단부 영역 위젯들 ######################
        # 검색 종류
        self.strType = StringVar()
        searchType = ttk.Combobox(frameTop, state='readonly',
                                            font=fontSet,
                                            values=["증상", "제약사", "약 이름"],
                                            textvariable=self.strType,
                                            width=7)
        searchType.current(0)
        searchType.place(x=20, y=25)        # 좌표

        # 검색창
        self.strSearch = StringVar()
        searchInput = Entry(frameTop, width=30,
                                      font=fontSet,
                                      textvariable=self.strSearch,
                                      borderwidth=2)
        searchInput.bind('<Return>', self.SearchButtonAction)
        searchInput.place(x=135, y=25)      # 좌표

        # 검색 버튼
        searchButton = Button(frameTop, font=fontSet_Btn,
                                        text="검색",
                                        command=self.SearchButtonAction,
                                        width=7)
        searchButton.place(x=485, y=23)     # 좌표


        ###################### 하단부 영역 위젯들 ######################
        # 목록 리스트
        self.listBtn = []
        for i in range(8):
            self.listBtn.append(Button(frameBottom, font=fontSet_Btn, text='', relief=FLAT, height=3, width=62, state=DISABLED,
                                                    bg='light blue', activebackground='light blue', disabledforeground='black', wraplength=560))
            self.listBtn[-1].place(x=3, y=80*i) # 좌표
        
        self.listBtn[0]['command'] = lambda: self.ShowDetail(0)
        self.listBtn[1]['command'] = lambda: self.ShowDetail(1)
        self.listBtn[2]['command'] = lambda: self.ShowDetail(2)
        self.listBtn[3]['command'] = lambda: self.ShowDetail(3)
        self.listBtn[4]['command'] = lambda: self.ShowDetail(4)
        self.listBtn[5]['command'] = lambda: self.ShowDetail(5)
        self.listBtn[6]['command'] = lambda: self.ShowDetail(6)
        self.listBtn[7]['command'] = lambda: self.ShowDetail(7)


        # 이전 버튼
        self.prevBtn = Button(frameBottom,  font=fontSet_Btn, text='이전', relief=FLAT, state=DISABLED, command=lambda: self.ShowList(-1),
                                            bg='light blue', activebackground='light green')
        
        # 다음버튼
        self.nextBtn = Button(frameBottom,  font=fontSet_Btn, text='다음', relief=FLAT, state=DISABLED, command=lambda: self.ShowList(+1),
                                            bg='light blue', activebackground='light green')

        self.prevBtn.place(x=3, y=640)      # 좌표
        self.nextBtn.place(x=525, y=640)    # 좌표

        window.mainloop()


    def SearchButtonAction(self, event = None):
        t = self.strType.get()
        type = 0
        if t == '증상':
            type = 0
        elif t == '제약사':
            type = 1
        else:
            type = 2
        self.medi.request(type, self.strSearch.get())

        self.pageNum = 0
        self.ShowList(0)

    def ShowList(self, option = 0):
        self.pageNum += option
        if self.pageNum == 0:
            self.nextBtn['state'] = NORMAL
            self.prevBtn['state'] = DISABLED
        elif self.pageNum == 4:
            self.nextBtn['state'] = DISABLED
            self.prevBtn['state'] = NORMAL 
        else:
            self.nextBtn['state'] = NORMAL
            self.prevBtn['state'] = NORMAL        

        for i in range(8):
                self.listBtn[i]['state'] = DISABLED
                self.listBtn[i]['text'] = ''

        if len(self.medi.medicine) == 0:
            self.nextBtn['state'] = DISABLED
            self.prevBtn['state'] = DISABLED
            self.listBtn[3]['text'] = '검색 결과가 없습니다.'

        else:
            for i in range(8):
                if i+(self.pageNum*8) == len(self.medi.medicine):
                    break
                
                self.listBtn[i]['state'] = NORMAL
                self.listBtn[i]['text'] = self.medi.medicine[i+(self.pageNum*8)]['제품명'] + " / " + self.medi.medicine[i+(self.pageNum*8)]['업체명']

    def ShowDetail(self, index):
        detail = Toplevel()
        detail.resizable(0, 0)
        detail.title('자세히 보기')

        RenderTextScrollbar = Scrollbar(detail)

        TempFont = font.Font(detail, size=10, family='Malgun Gothic')
        RenderText = Text(detail, font = TempFont, yscrollcommand=RenderTextScrollbar.set)
        for i in self.medi.COLUMNS:
            if i != '낱알 이미지':
                RenderText.insert(INSERT, "[" + i + "]\n")
                RenderText.insert(INSERT, str(self.medi.medicine[index+(self.pageNum*8)][i]) + "\n\n")
            else:
                try:
                    res = requests.get(str(self.medi.medicine[index+(self.pageNum*8)][i]))
                    img = P.open(BytesIO(res.content))
                    img1_size = img.size
                    img = img.resize((400, int(img1_size[1]*(400/img1_size[0]))), P.ANTIALIAS)
                    resized_image = ImageTk.PhotoImage(image=img)
                    label = Label(detail, image = resized_image)
                    label.image = resized_image
                    label.pack(side='bottom')
                    
                    # img.show() 그냥 기본 프로그램으로 열기

                except:
                    label = None
                
                
        RenderText.pack(side='left')
        RenderTextScrollbar.pack(side='right', fill='y')
        

test = Medi()
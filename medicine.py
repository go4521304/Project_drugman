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
import threading

#이메일 테스트
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # MIMEMultipart MIME 생성

host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = "logo.html"


class Medi:
    pageNum = 0
    
    def __init__(self, window):
        # window = Tk()
        # window.title('Medicine')
        # window.geometry('870x900')
        window.config(bg='light gray')

        self.medi = Medicine()

        # 쓰레딩시 사용할 락
        self.lock = threading.Lock()

        # 글꼴
        fontSet = font.Font(family='Consolas', weight='normal', size=15)

        # 버튼용 글꼴
        fontSet_Btn = font.Font(family='Consolas', weight='normal', size=12)

        # 가상이미지
        self.pixelVirtual = PhotoImage(width=1, height=1)

        # 상단부 영역
        frameTop = Frame(window,width=850,
                                height=85,
                                highlightthickness=3,
                                bg='light blue',
                                highlightbackground='white',
                                highlightcolor='white')
        frameTop.place(x=10, y=10)          # 좌표

        # 하단부 영역
        frameBottom = Frame(window, width=850,
                                    height=780,
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
        searchType.set("선택")
        searchType.place(x=20, y=25)        # 좌표

        # 검색창
        self.strSearch = StringVar()
        searchInput = Entry(frameTop, width=53,
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
        searchButton.place(x=745, y=23)     # 좌표


        ###################### 하단부 영역 위젯들 ######################
        # 목록 리스트
        self.listBtn = []
        for i in range(8):
            self.listBtn.append(Button(frameBottom, font=fontSet_Btn, text='', relief=FLAT, height=72, width=835, state=DISABLED, image=self.pixelVirtual, compound=LEFT,
                                                    bg='light blue', activebackground='light blue', disabledforeground='black', wraplength=600))
            self.listBtn[-1].place(x=1, y=80*i) # 좌표
        
        self.listBtn[0]['command'] = lambda: self.ShowDetail(0)
        self.listBtn[1]['command'] = lambda: self.ShowDetail(1)
        self.listBtn[2]['command'] = lambda: self.ShowDetail(2)
        self.listBtn[3]['command'] = lambda: self.ShowDetail(3)
        self.listBtn[4]['command'] = lambda: self.ShowDetail(4)
        self.listBtn[5]['command'] = lambda: self.ShowDetail(5)
        self.listBtn[6]['command'] = lambda: self.ShowDetail(6)
        self.listBtn[7]['command'] = lambda: self.ShowDetail(7)


        # 이전 버튼
        self.prevBtn = Button(frameBottom,  font=fontSet_Btn, text='이전', relief=FLAT, state=DISABLED, command=lambda: self.ShowList_Tr(-1),
                                            bg='light blue', activebackground='light green')
        
        # 다음버튼
        self.nextBtn = Button(frameBottom,  font=fontSet_Btn, text='다음', relief=FLAT, state=DISABLED, command=lambda: self.ShowList_Tr(+1),
                                            bg='light blue', activebackground='light green')

        self.prevBtn.place(x=3, y=740)      # 좌표
        self.nextBtn.place(x=790, y=740)    # 좌표


    def SearchButtonAction(self, event = None):
        t = self.strType.get()
        type = 0
        if t == '증상':
            type = 0
        elif t == '제약사':
            type = 1
        else:
            type = 2
        
        # 스레드로 생성하여 검색 중에도 ui가 멈추지 않게 함
        thread = threading.Thread(target=self.medi.request, args=(type, self.strSearch.get()))
        thread.daemon = True
        thread.start()
        thread.join()

        # 검색후 결과 표시
        self.pageNum = 0
        self.ShowList_Tr(0)

    def ShowList_Tr(self, option = 0):
        thread = threading.Thread(target=self.ShowList, args=(option,))
        thread.daemon = True
        thread.start()

    def ShowList(self, option = 0):
        self.lock.acquire()

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
                self.listBtn[i].configure(image= self.pixelVirtual)
                self.listBtn[i].image = self.pixelVirtual

        if len(self.medi.medicine) == 0:
            self.nextBtn['state'] = DISABLED
            self.prevBtn['state'] = DISABLED
            self.listBtn[3]['text'] = '검색 결과가 없습니다.'

        else:
            for i in range(8):
                if i+(self.pageNum*8) >= len(self.medi.medicine):
                    self.nextBtn['state'] = DISABLED
                    break

                
                self.listBtn[i]['state'] = NORMAL
                self.listBtn[i]['text'] = self.medi.medicine[i+(self.pageNum*8)]['제품명'] + " / " + self.medi.medicine[i+(self.pageNum*8)]['업체명']

                try:
                    res = requests.get(str(self.medi.medicine[i+(self.pageNum*8)]['낱알 이미지']))
                    img = P.open(BytesIO(res.content))
                    img1_size = img.size
                    img = img.resize((80, int(img1_size[1]*(80/img1_size[0]))), P.ANTIALIAS)
                    resized_image = ImageTk.PhotoImage(image=img)
                    self.listBtn[i].configure(image= resized_image)
                    self.listBtn[i].image = resized_image

                except:
                    pass
            
            if (i+1)+(self.pageNum*8) >= len(self.medi.medicine):
                self.nextBtn['state'] = DISABLED

        self.lock.release()



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

                except:
                    label = None

        Gimage = PhotoImage(file='./resource/logo-gmail.png')
        Send = Button(detail, image=Gimage, command=lambda: self.email_send(index))
        Send.configure(image= Gimage)
        Send.image = Gimage
        Send.pack(side='top')

        RenderText.pack(side='left')
        RenderTextScrollbar.pack(side='right', fill='y')


    def email_send(self,index):
        new = Toplevel()
        new.geometry("400x200")
        new.title('Email 전송')

        global host, port
        self.html = ""

        titleT = Label(new,text='제목을 입력하세요').place(x=5,y=10)
        self.str1 = StringVar()
        self.title = ttk.Entry(new ,width=30,textvariable=self.str1)
        self.title.place(x=180,y = 10)

        titleT = Label(new,text='이메일을 입력하세요').place(x=5,y=40)
        self.str2 = StringVar()
        self.senderAddr = ttk.Entry(new ,width=30,textvariable=self.str2)
        self.senderAddr.place(x=180,y=40)

        titleT = Label(new,text='받는사람 이메일을 입력하세요').place(x=5,y=70)
        self.str3 = StringVar()
        self.recipientAddr = ttk.Entry(new ,width=30,textvariable=self.str3)
        self.recipientAddr.place(x=180,y=70)

        self.msgtext=''
        for i in self.medi.COLUMNS:
            self.msgtext += (str((self.medi.medicine[index+(self.pageNum*8)][i])) + "\n\n")
        #print(msgtext)

        titleT = Label(new,text='비밀번호 입력하세요').place(x=5,y=100)
        self.str4 = StringVar()
        self.passwd = ttk.Entry(new ,width=20,textvariable=self.str4)
        self.passwd.place(x=180, y=100)

        self.msg = MIMEMultipart('alternative')  # Message container를 생성

        send = Button(new,text="보내기!",command=lambda:self.send_Button())
        send.pack(side="left")


    def send_Button(self):
        global host, port

        Title = self.str1.get()
        Email = self.str2.get()
        toEmail = self.str3.get()
        Pass = self.str4.get()

        self.msg['Subject'] = Title  # set message
        self.msg['From'] = Email
        self.msg['To'] = toEmail
        msgPart = MIMEText(self.msgtext, 'plain')
        bookPart = MIMEText(self.html, 'html', _charset='UTF-8')
        self.msg.attach(msgPart)  # 메세지에 생성한 MIME 문서를 첨부합니다
        self.msg.attach(bookPart)
        print("connect smtp server ... ")
        s = smtplib.SMTP(host, port)  # python3.6에서는 smtplib.SMTP(host,port)

        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(Email, Pass)  # 로그인
        s.sendmail(Email, [toEmail], self.msg.as_string())
        s.close()
        print("Mail sending complete!!!")

# showlist 실행중 검색을 실행하면
# 중간에 리스트내 항목을 건드려서 내용이 오염됨
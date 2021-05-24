from tkinter import *
from tkinter import font
from collections import ChainMap
import tkinter.messagebox
from medicine_new import *

class Medi:
    def __init__(self):
        self.items = []
        self.Main()

    def Main(self):
        self.Md = Tk()
        self.Md.title("Medicine")
        self.Md.geometry("600x800")
        self.medicine = Medicine()

        fill_Canvas = Canvas(self.Md,width = 2000,height=2000,bg='light green')
        fill_Canvas.place(x=-10,y=-100)

        Base_Canvas = Canvas(self.Md,width =570,height = 85,bg="light blue",)
        Base_Canvas.place(x=10,y=10)

        Info_Canvas = Canvas(self.Md, width=570, height=670, bg="light blue", )
        Info_Canvas.place(x=10, y=110)

        self.Search_efcyQesitm()
        self.InitInputLabel()
        self.InitSearchButton()

        self.Md.mainloop()

    def Search_efcyQesitm(self):
        self.ListBoxScrollbar = Scrollbar(self.Md)
        self.ListBoxScrollbar.pack()
        self.ListBoxScrollbar.place(x=150, y=30)

        TempFont = font.Font(self.Md, size=15, weight='bold', family='Consolas')
        self.SearchListBox = Listbox(self.Md, font=TempFont, activestyle='none',
                                width=10, height=1,
                                yscrollcommand=self.ListBoxScrollbar.set)

        self.SearchListBox.insert(0, "증상")
        self.SearchListBox.insert(1, "제약사")
        self.SearchListBox.insert(2, "약이름")

        self.SearchListBox.pack()
        self.SearchListBox.place(x=30, y=40)

        self.ListBoxScrollbar.config(command=self.SearchListBox.yview)

    def InitInputLabel(self):
        TempFont = font.Font(self.Md, size=15, weight='bold', family = 'Consolas')
        self.InputLabel = Entry(self.Md, font = TempFont, width = 26, relief = 'ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=180, y=40)

    def InitSearchButton(self):
        TempFont = font.Font(self.Md, size=12, weight='bold', family = 'Consolas')
        self.SearchButton = Button(self.Md, font = TempFont, text="검색",  command=self.SearchButtonAction)
        self.SearchButton.pack()
        self.SearchButton.place(x=490, y=35)

    def SearchButtonAction(self):
        iSearchIndex = self.SearchListBox.curselection()[0]
        key = self.InputLabel.get()

        if iSearchIndex == 0:
            self.medicine.request(0,key)
            self.items = self.medicine.medicine
            #print(type(self.medicine.medicine))
            #print(self.medicine.medicine)
            #print(self.items)
            self.InitRenderText()
        elif iSearchIndex == 1:
            self.medicine.request(1,key)
            self.items = self.medicine.medicine
            self.Render()
        elif iSearchIndex == 2:
            self.medicine.request(2,key)
            self.items = self.medicine.medicine
            self.InitRenderText()

    def InitRenderText(self):
        RenderTextScrollbar = Scrollbar(self.Md)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(self.Md, size=10, family='Consolas')
        RenderText = Text(self.Md, width=80, height=50.5, relief='ridge',font = TempFont,
                          yscrollcommand=RenderTextScrollbar.set)

        for i in range(len(self.items)):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "업체명 : ")
                RenderText.insert(INSERT, self.items[i]["업체명"])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "제품명 : ")
                RenderText.insert(INSERT, self.items[i]["제품명"])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "효능 : ")
                RenderText.insert(INSERT, self.items[i]["효능"])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "사용법 : ")
                RenderText.insert(INSERT, self.items[i]["사용법"])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "주의사항 : ")
                RenderText.insert(INSERT, self.items[i]["주의사항"])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "보관법 : ")
                RenderText.insert(INSERT, self.items[i]["보관법"])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "낱알 이미지 :  ")
                #시발이거왜터짐?
                #RenderText.insert(INSERT, self.items[i]["낱알 이미지"])
                RenderText.insert(INSERT, "\n\n\n")


        RenderText.pack()
        RenderText.place(x=15, y=115)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        RenderText.configure(state='disabled')

    def Render(self):
        for i in range(len(self.items)):
            print()





Medi()

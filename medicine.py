from tkinter import *
from tkinter import font
import tkinter.messagebox
from medicine_new import *

class Medi:
    def __init__(self):
        self.Main()

    def Main(self):
        self.Md = Tk()
        self.Md.title("Medicine")
        self.Md.geometry("600x800")
        self.medicine = Medicine()
        Base_Canvas = Canvas(self.Md,width =570,height = 85,bg="light gray",)
        Base_Canvas.place(x=10,y=10)

        Info_Canvas = Canvas(self.Md, width=570, height=670, bg="light gray", )
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
        self.SearchListBox.insert(1, "약 이름")
        self.SearchListBox.insert(2, "제약사")

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
            print(self.medicine.medicine[0])
        elif iSearchIndex == 1:
            self.medicine.request(1,key)
        elif iSearchIndex == 2:
            self.medicine.request(2,key)




Medi()

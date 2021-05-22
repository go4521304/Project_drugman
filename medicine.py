from tkinter import *
from tkinter import font
import tkinter.messagebox

import urllib
import http.client
from medicine_new import *
conn = http.client.HTTPConnection("apis.data.go.kr")
serviceKey = urllib.parse.quote("6LhIfl4AUMeRlvkH0mimycui3rFJsijVvZWIHR4mt5/symnzRkA+Zi4WZJ8ietyQ/LnNBAKhnSirL3lRX7WllA==")

class Medi:
    def __init__(self):
        pass

    def Main(self):
        Md = Tk()
        Md.title("Medicine")
        Md.geometry("600x800")
        conn.request("GET", "http://apis.data.go.kr/1471000/DrbEasyDrugInfoService?serviceKey=" + serviceKey)
        medicine = Medicine()
        req = conn.getresponse()
        print(req.status, req.reason)
        print(req.read().decode('utf-8'))

        Base_Canvas = Canvas(Md,width =570,height = 85,bg="light gray",)
        Base_Canvas.place(x=10,y=10)

        Info_Canvas = Canvas(Md, width=570, height=670, bg="light gray", )
        Info_Canvas.place(x=10, y=110)

        Md.mainloop()

    def Search_efcyQesitm(self):
        global SearchListBox
        ListBoxScrollbar = Scrollbar(Md)
        ListBoxScrollbar.pack()
        ListBoxScrollbar.place(x=150, y=30)

        TempFont = font.Font(Md, size=15, weight='bold', family='Consolas')
        SearchListBox = Listbox(Md, font=TempFont, activestyle='none',
                                width=10, height=1,
                                yscrollcommand=ListBoxScrollbar.set)

        SearchListBox.insert(0, "증상")
        SearchListBox.insert(1, "약 이름")
        SearchListBox.insert(2, "제약사")

        SearchListBox.pack()
        SearchListBox.place(x=30, y=40)

        ListBoxScrollbar.config(command=SearchListBox.yview)

    def InitInputLabel():
        global InputLabel
        TempFont = font.Font(Md, size=15, weight='bold', family = 'Consolas')
        InputLabel = Entry(Md, font = TempFont, width = 26, relief = 'ridge')
        InputLabel.pack()
        InputLabel.place(x=180, y=40)

    def InitSearchButton():
        TempFont = font.Font(Md, size=12, weight='bold', family = 'Consolas')
        SearchButton = Button(Md, font = TempFont, text="검색",  command=SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=490, y=35)

    def SearchButtonAction():
        iSearchIndex = SearchListBox.curselection()[0]

        if iSearchIndex == 0:
            medicine.request(0,)
        elif iSearchIndex == 1:
            medicine.request(1,)
        elif iSearchIndex == 2:
            medicine.request(2,)




Medi()

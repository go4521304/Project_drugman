from tkinter import *
from branca.element import IFrame
from cefpython3 import cefpython as cef
from tkinter import *
from tkinter import font
from tkinter import ttk
import threading
import sys
import folium
import json
from pharmacy_conn import *

class Pharm:
    def __init__(self, window):
        # window = Tk()
        # window.title('pharmacy')
        # window.geometry('870x900')
        window.config(bg='light gray')

        self.pharm = Pharmacy()

        # 폰트
        fontSet = font.Font(family='Consolas', weight='normal', size=15)
        fontSet_Btn = font.Font(family='Consolas', weight='normal', size=12)

        # 초기 지도 저장
        m = folium.Map(location=[37.3402849,126.7313189], zoom_start=15)
        m.save('map.html')

        # 상단부 영역
        self.frameTop = Frame(window,width=850,
                                height=800,
                                highlightthickness=3,
                                bg='light blue',
                                highlightbackground='white',
                                highlightcolor='white')

        self.frameTop.place(x=10, y=10)  

        # 하단부 영역
        frameBottom = Frame(window, width=850,
                                    height=70,
                                    highlightthickness=3,
                                    bg='light blue',
                                    highlightbackground='white',
                                    highlightcolor='white')
        frameBottom.place(x=10, y=820)


        ###################### 상단부 영역 위젯들 ######################
        # 지도
        thread = threading.Thread(target=self.showMap, args=(self.frameTop,))
        thread.daemon = True
        thread.start()

        ###################### 하단부 영역 위젯들 ######################
        with open("./resource/address_list.json", encoding='UTF-8') as f:
            self.address_data = json.load(f)
        # 주소1
        self.strAdd1 = StringVar()
        searchAdd1 = ttk.Combobox(frameBottom, state='readonly',
                                            font=fontSet,
                                            values=list(self.address_data.keys()),
                                            textvariable=self.strAdd1,
                                            width=15)
        searchAdd1.bind("<<ComboboxSelected>>", self.selAdd1)
        searchAdd1.set("시/도")
        searchAdd1.place(x=160, y=20)        # 좌표

        self.strAdd2 = StringVar()
        self.searchAdd2 = ttk.Combobox(frameBottom, state='readonly',
                                            font=fontSet,
                                            textvariable=self.strAdd2,
                                            width=18)
        self.searchAdd2.set("시/군/구")
        self.searchAdd2.place(x=360, y=20)        # 좌표

        # 검색버튼
        searchButton = Button(frameBottom, font=fontSet_Btn,
                                        text="검색",
                                        command=self.SearchButtonAction,
                                        width=7)
        searchButton.place(x=610, y=18)     # 좌표    
    
    def showMap(self, frame):
        sys.excepthook = cef.ExceptHook
        self.window_info = cef.WindowInfo(frame.winfo_id())
        self.window_info.SetAsChild(frame.winfo_id(), [3,3,847,797])
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(self.window_info, url='file:///map.html')
        cef.MessageLoop()

    def SearchButtonAction(self):
        self.mapSave()
        self.browser.LoadUrl('file:///map.html')
        # self.browser.LoadUrl('https://www.youtube.com')


    def mapSave(self):
        if self.strAdd1.get() == "시/도" or self.strAdd2.get() == "시/군/구":
            return

        self.pharm.request(self.strAdd1.get(), self.strAdd2.get())

        tmp = self.pharm.pharmacy.mean()

        m = folium.Map(location=[tmp['LAT'],tmp['LON']], zoom_start=13)
        for i, row in self.pharm.pharmacy.iterrows():
            html = row['약국 이름'] + """<br><br>""" + """전화번호<br>""" + row['전화번호'] + """<br><br>""" + """주소<br>""" + row['주소'] 
            iframe = folium.IFrame(html=html, width=200, height=200)
            if row['LAT'] != -1.0 and row['LON'] != -1.0:
                folium.Marker(location=[row['LAT'], row['LON']], tooltip=row['약국 이름'], popup=folium.Popup(iframe)).add_to(m)

        m.save('map.html')

    def selAdd1(self, event):
        self.searchAdd2.set("시/군/구")
        self.searchAdd2['value'] = self.address_data[self.strAdd1.get()]
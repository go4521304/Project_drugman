from tkinter import *
from cefpython3 import cefpython as cef
from tkinter import *
from tkinter import font
from tkinter import ttk
import threading
import sys
import folium
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
        # 검색버튼
        searchButton = Button(frameBottom, font=fontSet_Btn,
                                        text="검색",
                                        command=self.SearchButtonAction,
                                        width=7)
        searchButton.place(x=745, y=18)     # 좌표    
        # window.mainloop()
    
    def showMap(self, frame):
        sys.excepthook = cef.ExceptHook
        self.window_info = cef.WindowInfo(frame.winfo_id())
        self.window_info.SetAsChild(frame.winfo_id(), [3,3,847,797])
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(self.window_info, url='file:///map.html')
        cef.MessageLoop()

    def SearchButtonAction(self):
        self.mapSave()
        self.browser.Reload()
        

    def mapSave(self):
        m = folium.Map(location=[37.3402849,126.7313189], zoom_start=12)
        self.pharm.request()

        for i, row in self.pharm.pharmacy.iterrows():
            folium.Marker(location=[row['LAT'], row['LON']], tooltip=row['약국 이름']).add_to(m)

        m.save('map.html')
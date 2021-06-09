from tkinter import *
import threading
import sys
from tkinter import messagebox
# pip install folium
import folium
# pip install cefpython3==66.1
from cefpython3 import cefpython as cef

# cef모듈로 브라우저 실행
class Search:
    def __init__(self):
        pass

    def showMap(self, frame):
        sys.excepthook = cef.ExceptHook
        window_info = cef.WindowInfo(frame.winfo_id())
        window_info.SetAsChild(frame.winfo_id(), [0,0,800,600])
        cef.Initialize()
        browser = cef.CreateBrowserSync(window_info, url='https://www.health.kr/searchIdentity/search.asp')
        cef.MessageLoop()

# 이 파일은 GUI를 띄우는 파일입니다.

from tkinter import *

class Main_GUI:
    def __init__(self):
        window = Tk()
        window.title("약 좀 주세요 ~약 먹을 시간~")

        window.mainloop()

if __name__ == "__main__":
    Main_GUI()
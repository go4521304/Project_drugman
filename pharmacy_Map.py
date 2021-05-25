from tkinter import *
import folium
import webbrowser
import pharmacy as ph

def Pressed():
    # 위도 경도 지정
    test = ph.Pharmacy()
    test.request()
    print(test.pharmacy)

    map_osm = folium.Map(location=[37.3402849,126.7313189], zoom_start=13)
    # 마커 지정
    folium.Marker([37.3402849,126.7313189], popup='한국산업기술대').add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

window= Tk()
Button(window, text='folium 지도', command=Pressed).pack()
window.mainloop()
from tkinter import *
import folium
import webbrowser
import pharmacy as ph

def Pressed():
    # 위도 경도 지정
    test = ph.Pharmacy()
    test.request()

    print(test.pharmacy['LON'][1])
    print(test.pharmacy['LAT'][1])
    map_osm = folium.Map(location=[test.pharmacy['LON'][1], test.pharmacy['LAT'][1]], zoom_start=13)
    # 마커 지정
    folium.Marker([test.pharmacy['LON'][1], test.pharmacy['LAT'][1]],
                  popup='한국산업기술대').add_to(map_osm)
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

    #print(test.pharmacy['주소'][1])

    # html 파일로 저장

window= Tk()
Button(window, text='folium 지도', command=Pressed).pack()
window.mainloop()
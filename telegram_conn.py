import urllib.request
import urllib.parse
import urllib
import http.client
from bs4 import BeautifulSoup
conn = http.client.HTTPConnection("apis.data.go.kr")

SERVICE_KEY = urllib.parse.quote("6LhIfl4AUMeRlvkH0mimycui3rFJsijVvZWIHR4mt5/symnzRkA+Zi4WZJ8ietyQ/LnNBAKhnSirL3lRX7WllA==")

def request(LAT= 37.3897448, LON= 126.94961):
    conn.request("GET","/B552657/ErmctInsttInfoInqireService/getParmacyLcinfoInqire?serviceKey=" + SERVICE_KEY + "&WGS84_LON=" + str(LON) + "&WGS84_LAT=" + str(LAT))
    try:
        req = conn.getresponse()
        if req.status == 200:
            data = req.read().decode('utf-8')
            soup = BeautifulSoup(data, 'xml')
            if soup.find('resultCode').string == '00':
                info = []
                for i in soup.find_all('item'):
                    info.append(i.dutyName.string + " / " + i.dutyAddr.string + "\n" + i.dutyTel1.string + "\n" + "영업시간 " + i.startTime.string + "-" + i.endTime.string)
                return info
            else:
                print('Load Fail / Code : ' + soup.find('resultCode').string)
    except Exception as ex:
        print("Error", ex)
        return ["잠시후에 다시 시도해주세요"]
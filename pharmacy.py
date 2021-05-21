from typing import Sized
import pandas as pd
import urllib
import http.client
conn = http.client.HTTPConnection("apis.data.go.kr")

class Pharmacy:
    SERVICE_KEY = urllib.parse.quote("2ZPJttwEWTlLBUXFd85FaqaDuDsSw7BRwX5pChZ2epOCy+i0RjC5jcchv1CplZTKF/x2GiNPOC99KeY31otTEQ==")

    pharmacy = None
    index = 0

    def __init__(self):
        pass

    def request(self, add1 = "경기도", add2="시흥시"):
        # 데이터프레임 생성
        self.pharmacy = pd.DataFrame(columns=['주소', '약국 이름', '전화번호', 'ID', 'LON', 'LAT'])
        self.index = 0

        Q0 = urllib.parse.quote(add1)  # 주소 (시도)
        Q1 = urllib.parse.quote(add2)  # 주소 (시군구)

        # 두번 호출해서 총 40개를 받아옴
        conn.request("GET","/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=" + self.SERVICE_KEY 
        + "&Q0=" + Q0 + "&Q1=" + Q1 + "&ORD=NAME" + "&pageNo=1" + "&numOfRows=20")
        req = conn.getresponse()
        if req.status == 200:
            self.extractData(req.read().decode('utf-8'))
        else:
            print(req.status,req.reason)

        conn.request("GET","/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=" + self.SERVICE_KEY 
        + "&Q0=" + Q0 + "&Q1=" + Q1 + "&ORD=NAME" + "&pageNo=2" + "&numOfRows=20")
        req = conn.getresponse()
        if req.status == 200:
            self.extractData(req.read().decode('utf-8'))
        else:
            print(req.status,req.reason)


    # 정보를 데이터 프레임에 집어넣음
    def extractData(self, strXml):
        # 만약에 불러오기가 실패해서 비어있을 경우 종료
        if strXml == None:
            print('Fail, Empty!')
            return

        from xml.etree import ElementTree
        tree = ElementTree.fromstring(strXml)

        resultCode = tree.find('header').find('resultCode')
        if resultCode.text == '00':
            item = tree.iter('item')
            for i in item:
                self.pharmacy.loc[self.index] = [i.find('dutyAddr').text, i.find('dutyName').text, 
                i.find('dutyTel1').text, i.find('hpid').text, i.find('wgs84Lon').text, i.find('wgs84Lat').text]
                self.index+=1
        else:
            print('Load Fail / Code : ' + resultCode.text)
        

# 나중에 임포트 할 때 지우기!!
test = Pharmacy()
test.request()
print(test.pharmacy)
from typing import Sized
import pandas as pd
import urllib
import http.client
conn = http.client.HTTPConnection("apis.data.go.kr")

class Pharmacy:
    SERVICE_KEY = urllib.parse.quote("2ZPJttwEWTlLBUXFd85FaqaDuDsSw7BRwX5pChZ2epOCy+i0RjC5jcchv1CplZTKF/x2GiNPOC99KeY31otTEQ==")

    pharmacy = None

    num_of_pharm = None

    def __init__(self):
        pass
    
    def request_num(self, add1 = "제주특별자치도", num_list=["제주시", "서귀포시"]):
        self.num_of_pharm = {}
        Q0 = urllib.parse.quote(add1)  # 주소 (시도)

        for add2 in num_list:
            Q1 = urllib.parse.quote(add2)  # 주소 (시군구)

            conn.request("GET","/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=" + self.SERVICE_KEY 
            + "&Q0=" + Q0 + "&Q1=" + Q1 + "&ORD=NAME" + "&pageNo=0" + "&numOfRows=0")
            req = conn.getresponse()
            if req.status == 200:
                from xml.etree import ElementTree
                tree = ElementTree.fromstring(req.read().decode('utf-8'))
                resultCode = tree.find('header').find('resultCode')
                if resultCode.text == '00':
                    self.num_of_pharm[add2] = int(tree.find('body').find('totalCount').text)
            else:
                print(req.status,req.reason)


    def request(self, add1 = "경기도", add2="안양시"):
        # 데이터프레임 생성

        self.pharmacy = pd.DataFrame(columns=['주소', '약국 이름', '전화번호', 'ID', 'LON', 'LAT'])

        Q0 = urllib.parse.quote(add1)  # 주소 (시도)
        Q1 = urllib.parse.quote(add2)  # 주소 (시군구)

        conn.request("GET","/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=" + self.SERVICE_KEY 
        + "&Q0=" + Q0 + "&Q1=" + Q1 + "&ORD=NAME" + "&pageNo=1" + "&numOfRows=1000")
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
                lon = -1.0
                lat = -1.0
                if i.find('wgs84Lon') != None:
                    lon = float(i.find('wgs84Lon').text)
                if i.find('wgs84Lat') != None:
                    lat = float(i.find('wgs84Lat').text)

                if lon != -1 and lat != -1:
                    self.pharmacy.loc[len(self.pharmacy)] = [i.find('dutyAddr').text, i.find('dutyName').text, 
                    i.find('dutyTel1').text, i.find('hpid').text, lon, lat]
        else:
            print('Load Fail / Code : ' + resultCode.text)
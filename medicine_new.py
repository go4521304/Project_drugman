from typing import Sized
import pandas as pd
import urllib
import http.client
conn = http.client.HTTPConnection("apis.data.go.kr")

class Medicine:
    SERVICE_KEY = urllib.parse.quote("6LhIfl4AUMeRlvkH0mimycui3rFJsijVvZWIHR4mt5/symnzRkA+Zi4WZJ8ietyQ/LnNBAKhnSirL3lRX7WllA==")

    medicine = None
    index = 0

    TYPE = {'0': '&entpName=', '1': '&itemName=', '2': '&efcyQesitm='}

    def __init__(self):
        pass

    def request(self, type = '0', option = '유한양행'):
        # 데이터프레임 생성
        self.medicine = pd.DataFrame(columns=['업체명', '제품명', 'ID', '효능', '사용법', '주의사항 경고', '주의사항', '상호작용', '부작용', '보관법', '낱알 이미지'])
        self.index = 0

        # 옵션에 따라 쿼리 생성
        find_query = self.TYPE[type] + urllib.parse.quote(option)

        conn.request("GET","/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList?serviceKey=" + self.SERVICE_KEY 
        + "&pageNo=1" + find_query + "&numOfRows=20" + '&type=xml')
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
                self.medicine.loc[self.index] = [i.find('entpName').text, i.find('itemName').text, 
                i.find('itemSeq').text, i.find('efcyQesitm').text, i.find('useMethodQesitm').text, i.find('atpnWarnQesitm').text, i.find('atpnQesitm').text,
                i.find('intrcQesitm').text, i.find('seQesitm').text, i.find('depositMethodQesitm').text, i.find('itemImage').text]
                self.index+=1
        else:
            print('Load Fail / Code : ' + resultCode.text)
        

# 나중에 임포트 할 때 지우기!!
test = Medicine()
test.request()
print(test.medicine)
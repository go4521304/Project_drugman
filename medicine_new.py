from typing import Sized
import urllib
import http.client
conn = http.client.HTTPConnection("apis.data.go.kr")

class Medicine:
    SERVICE_KEY = urllib.parse.quote("6LhIfl4AUMeRlvkH0mimycui3rFJsijVvZWIHR4mt5/symnzRkA+Zi4WZJ8ietyQ/LnNBAKhnSirL3lRX7WllA==")

    medicine = []

    TYPE = {'0': '&entpName=', '1': '&itemName=', '2': '&efcyQesitm='}
    COLUMNS = ['업체명', '제품명', 'ID', '효능', '사용법', '주의사항 경고', '주의사항', '상호작용', '부작용', '보관법', '낱알 이미지']

    def __init__(self):
        pass

    def request(self, type = '0', option = '유한양행'):
        # 리스트로 생성
        self.medicine.clear()

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
                self.medicine.append({self.COLUMNS[0]:i.find('entpName').text, self.COLUMNS[1]:i.find('itemName').text, 
                self.COLUMNS[2]:i.find('itemSeq').text, self.COLUMNS[3]:i.find('efcyQesitm').text, self.COLUMNS[4]:i.find('useMethodQesitm').text,
                self.COLUMNS[5]: i.find('atpnWarnQesitm').text, self.COLUMNS[6]:i.find('atpnQesitm').text, self.COLUMNS[7]:i.find('intrcQesitm').text, 
                self.COLUMNS[8]:i.find('seQesitm').text, self.COLUMNS[9]:i.find('depositMethodQesitm').text, self.COLUMNS[10]:i.find('itemImage').text})
        else:
            print('Load Fail / Code : ' + resultCode.text)

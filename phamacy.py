import urllib
import http.client
conn = http.client.HTTPConnection("apis.data.go.kr")

serviceKey = urllib.parse.quote("2ZPJttwEWTlLBUXFd85FaqaDuDsSw7BRwX5pChZ2epOCy+i0RjC5jcchv1CplZTKF/x2GiNPOC99KeY31otTEQ==")
Q0 = urllib.parse.quote("서울특별시")  # 주소 (시도)
Q1 = urllib.parse.quote("강남구")  # 주소 (시군구)
QT = urllib.parse.quote("1")  # 월~일요일, 공휴일: 1~8
QN = urllib.parse.quote("삼성약국") # 기관명
ORD = urllib.parse.quote("NAME") # 순서
pageNo = urllib.parse.quote("1") # 페이지 번호
numOfRows = urllib.parse.quote("10") # 목록건수

conn.request("GET","/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=" + serviceKey 
+ "&Q0=" + Q0 + "&Q1=" + Q1 + "&QT=" + QT + "&QN=" + QN + "&ORD=" + ORD + "&pageNo=" + pageNo + "&numOfRows=" + numOfRows)
req = conn.getresponse()
print(req.status,req.reason)
print(req.read().decode('utf-8'))
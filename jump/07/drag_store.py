import requests
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire'
params ={'serviceKey' : 'ROAwUM52Kz+efjQmw0kFhGebke+XDkNLBgoIgosL3GaLBn9KStstxEsLbWS0M6AGxjRyEB3R1kIX+IdtCa5X4Q==', 'Q0' : '서울특별시', 'Q1' : '강남구', 'QT' : '2',  'ORD' : 'NAME', 'pageNo' : '1', 'numOfRows' : '10' }

response = requests.get(url, params=params)
xml_data = response.text


# XML 파싱
root = ET.fromstring(xml_data)

# 약국 목록 출력
print("약국 목록:")
for item in root.findall('.//item'):
    name = item.find('dutyName').text
    address = item.find('dutyAddr').text
    tel = item.find('dutyTel1').text
    open_time = item.find('dutyTime1s').text
    close_time = item.find('dutyTime1c').text
    
    print(f"이름: {name}")
    print(f"주소: {address}")
    print(f"전화번호: {tel}")
    print(f"영업시간: {open_time} ~ {close_time}")
    print("------")
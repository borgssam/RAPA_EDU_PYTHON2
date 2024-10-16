import requests
import xmltodict
import json

ENCODING_KEY = f"bCNhrOuzkyRgF0N%2FZvVwyKQTU1Cuzv%2FzcP%2F0SXhU5eMCCaMg3%2Bvm7RLDznnW17qOJhOmT0MJo87JMdnHa9lhfg%3D%3D"
DECODING_KEY = f"bCNhrOuzkyRgF0N/ZvVwyKQTU1Cuzv/zcP/0SXhU5eMCCaMg3+vm7RLDznnW17qOJhOmT0MJo87JMdnHa9lhfg=="
ENDPOINT_URL = f"http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire"

DATE2QT = {
    "월" : 1,
    "화" : 2,
    "수" : 3,
    "목" : 4,
    "금" : 5,
    "토" : 6,
    "일" : 7,
    "공휴일" : 8,
}

usr_city = input("시/군를 입력하세요!")
usr_ht = input("구를 입력하세요!")
usr_dt = input("요일을 입력하세요!")

params ={'serviceKey' : DECODING_KEY, 'Q0' : usr_city, 'Q1' : usr_ht, 'QT' : DATE2QT[usr_dt], 'ORD' : 'NAME', 'pageNo' : '1', 'numOfRows' : '100' }



response = requests.get(ENDPOINT_URL, params=params)

rsp_content = response.content.decode()
rsp_content_dict = xmltodict.parse(rsp_content)["response"]["body"]["items"]["item"]
for i, durgstore_data in enumerate(rsp_content_dict):
    print(f"{i+1}.{durgstore_data['dutyAddr']}\t{durgstore_data['dutyName']}")
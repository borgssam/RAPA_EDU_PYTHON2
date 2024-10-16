import requests
import xmltodict
import json

ENCODING_KEY = f"bCNhrOuzkyRgF0N%2FZvVwyKQTU1Cuzv%2FzcP%2F0SXhU5eMCCaMg3%2Bvm7RLDznnW17qOJhOmT0MJo87JMdnHa9lhfg%3D%3D"
DECODING_KEY = f"bCNhrOuzkyRgF0N/ZvVwyKQTU1Cuzv/zcP/0SXhU5eMCCaMg3+vm7RLDznnW17qOJhOmT0MJo87JMdnHa9lhfg=="
ENDPOINT_URL = f"http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService"

url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire'
params ={'serviceKey' : DECODING_KEY, 'Q0' : '서울특별시', 'Q1' : '금천구', 'QT' : '8', 'ORD' : 'NAME', 'pageNo' : '1', 'numOfRows' : '100' }

response = requests.get(url, params=params)

rsp_content = response.content.decode()
rsp_content_dict = xmltodict.parse(rsp_content)["response"]["body"]["items"]["item"]
for i, durgstore_data in enumerate(rsp_content_dict):
    print(f"{i+1}.{durgstore_data['dutyAddr']}\t{durgstore_data['dutyName']}\t{durgstore_data['dutyTime8s']}")
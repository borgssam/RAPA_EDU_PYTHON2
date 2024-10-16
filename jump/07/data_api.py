# Python3 샘플 코드 #

import requests
import json
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : 'ROAwUM52Kz+efjQmw0kFhGebke+XDkNLBgoIgosL3GaLBn9KStstxEsLbWS0M6AGxjRyEB3R1kIX+IdtCa5X4Q==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'JSON', 'base_date' : '20241016', 'base_time' : '0600', 'nx' : '55', 'ny' : '125' }

response = requests.get(url, params=params)
# print(response.content)
print(response.text)
# res = json.loads(response.text)
# print(res)
# 출력
# pretty_json = json.dumps(response.content, ensure_ascii=False, indent=4)
# print(pretty_json)


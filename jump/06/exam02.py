import requests

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : 'ROAwUM52Kz+efjQmw0kFhGebke+XDkNLBgoIgosL3GaLBn9KStstxEsLbWS0M6AGxjRyEB3R1kIX+IdtCa5X4Q==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20241015', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }

response = requests.get(url, params=params)
print(response.content)
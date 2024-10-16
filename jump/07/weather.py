import requests
import json
#풍향 각도 0~360도를 8방위로 변환
def deg_to_dir(deg):
    # 360도를 8등분하여 풍향을 문자열로 변환
    if deg >= 337.5 or deg < 22.5:
        return "북"
    elif 22.5 <= deg < 67.5:
        return "북동"
    elif 67.5 <= deg < 112.5:
        return "동"
    elif 112.5 <= deg < 157.5:
        return "남동"
    elif 157.5 <= deg < 202.5:
        return "남"
    elif 202.5 <= deg < 247.5:
        return "남서"
    elif 247.5 <= deg < 292.5:
        return "서"
    elif 292.5 <= deg < 337.5:
        return "북서"
    
#변수값
#서비스키
serviceKey = "ROAwUM52Kz%2BefjQmw0kFhGebke%2BXDkNLBgoIgosL3GaLBn9KStstxEsLbWS0M6AGxjRyEB3R1kIX%2BIdtCa5X4Q%3D%3D"
#위치좌표
nx='55'
ny='125'
#날짜시간
base_date = "20231016"
base_time = "0600"

#url
url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey={serviceKey}&numOfRows=60&pageNo=1&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"

# print(url)

#데이터요청해서 가져오기
response = requests.get(url,verify=False)
print(response.text)

#읽어온 데이터를 Json객체로 변환
res = json.loads(response.text)

information = dict()
for items in res['response']['body']['items']['item']:
  fcstDate = items['fcstDate']
  fcstTime = items['fcstTime']
  category = items['category']
  fcstValue = items['fcstValue']
  key = fcstDate+fcstTime
  if key not in information:
    information[key] = {}

  information[key][category] = fcstValue
sky_code = {1:'맑음    ', 3:'구름많음', 4:'흐림    '}
for key, values in information.items():
  info = ""
  for category, value in values.items():
    if category == 'PTY':
      category = '강수량'
    elif category == 'SKY':
      category = '날씨'
      value = sky_code[int(value)]
    elif category == 'T1H':
      category = '기온'
    elif category == 'REH':
      category = '습도'
    elif category == 'UUU':
      category = '동서바람속도'
    elif category == 'VVV':
      category = '남북바람속도'
    elif category == 'VEC':
      category = '풍향'
      value = deg_to_dir(float(value))
    elif category == 'WSD':
      category = '풍속(m/s)'
    elif category == 'LGT':
      category = '낙뢰'
    elif category == 'RN1':
      category = '시간당강수량'

    if len(info) > 0:
      info += ","
    info += f"{category}: {value} "

  print(f'{key}, {info}')


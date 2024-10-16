import requests
import json
import xmltodict
import folium

# 변수값
# 서비스키
serviceKey = "0vQOxUUn8z0N7MAb+/lyIFQGxM70zkpkFFzCXPIaMyvvx8zb9yNDOSAFavlXyNdwWOVvw8+dwG/m/jW/9sXLoQ=="
keys = ['금천구', '강남구', '서초구', '동작구', '구로구', '양천구', '영등포구', '관악구', '용산구', '서대문구', '마포구', '은평구', '종로구', '중구', '성북구', '동대문구', '중랑구', '노원구', '도봉구', '강북구', '광진구', '강동구', '송파구']
values = [[37.456736, 126.895373], [37.52579, 127.0483], [37.49093, 127.0329], [37.51871, 126.9364], [37.50237, 126.8890], [37.52007, 126.9549], [37.54240, 126.8402], [37.48467, 126.95158], [37.53804, 126.99139], [37.58567, 126.935710], [37.57003, 126.901911], [37.60675, 126.930212], [37.57615, 126.979013], [37.56798, 126.997514], [37.59342, 127.017215], [37.57792, 127.040116], [37.60961, 127.093117], [37.65664, 127.055918], [37.67214, 127.046219], [37.64278, 127.025320], [37.54104, 127.082621], [37.53246, 127.123722], [37.51803, 127.1056]]
district_office = dict(zip(keys, values))

district = '서초구'
url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire'
params ={'serviceKey' : {serviceKey}, 'Q0' : '서울특별시', 'Q1' : {district}}


response = requests.get(url, params=params)
xmlData = response.text
jsonStr = json.dumps(xmltodict.parse(xmlData), indent = 4)
dictionary = json.loads(jsonStr)


m = folium.Map(location=district_office.get(district), zoom_start=14, tiles='cartodbpositron')

# 구청의 위치 서클
folium.Circle(
    location=district_office.get(district),
    radius=100, # 원 크기
    color='#eb9e34', # 원 선 색상
    fill_color='red', # 원 내부 색상
    tooltip=district + '청'
).add_to(m)

for items in dictionary['response']['body']['items']['item']:
    lat = items['wgs84Lat']
    lon = items['wgs84Lon']
    name = items['dutyName']
    start_time = items['dutyTime1s']
    last_time = items['dutyTime1c']
    if (int(last_time) <= 1800): # 1800시 이전에 끝나면 파란색 마커
        folium.Marker([lat, lon], tooltip=name, popup='<b>Start</b>\n '+start_time+'\n<b>Close</b>\n'+last_time, icon=folium.Icon(icon = "plus", color = "blue")).add_to(m)
    else: # 1800이후면 빨간색 마커
        folium.Marker([lat, lon], tooltip=name, popup='<b>Start</b>\n '+start_time+'\n<b>Close</b>\n'+last_time,icon=folium.Icon(icon = "plus", color = "red")).add_to(m)



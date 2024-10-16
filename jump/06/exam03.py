import requests
serviceKey = "ROAwUM52Kz%2BefjQmw0kFhGebke%2BXDkNLBgoIgosL3GaLBn9KStstxEsLbWS0M6AGxjRyEB3R1kIX%2BIdtCa5X4Q%3D%3D" # 본인의 서비스 키 입력

nx = '55' # 예보 지점 x좌표
ny = '125' # 예보 지점 y좌표

from datetime import datetime, timedelta
# 알고 싶은 시간
base_date = "20241014" # 발표 일자
base_time = "1100" # 발표 시간
input_d = datetime.strptime(base_date + base_time, "%Y%m%d%H%M")
print(input_d)

# 실제 입력 시간
input_d = datetime.strptime(base_date + base_time, "%Y%m%d%H%M") - timedelta(hours=1)
print(input_d)

input_datetime = datetime.strftime(input_d, "%Y%m%d%H%M")
input_date = input_datetime[:-4]
input_time = input_datetime[-4:]

# url (최근 3일 내 데이터만 조회 가능)
url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey={serviceKey}&numOfRows=60&pageNo=1&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"
print(url)

import json
response = requests.get(url, verify=False)
print(response.text)
res = json.loads(response.text)

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
    
informations = dict()
for items in res['response']['body']['items']['item'] :
    cate = items['category']
    fcstTime = items['fcstTime']
    fcstValue = items['fcstValue']
    temp = dict()
    temp[cate] = fcstValue
    
    if fcstTime not in informations.keys() :
        informations[fcstTime] = dict()
#     print(items['category'], items['fcstTime'], items['fcstValue'])
#     print(informations[fcstTime])
    informations[fcstTime][cate] = fcstValue

# print(informations)
pyt_code = {0 : '강수 없음', 1 : '비', 2 : '비/눈', 3 : '눈', 5 : '빗방울', 6 : '진눈깨비', 7 : '눈날림'}
sky_code = {1 : '맑음', 3 : '구름많음', 4 : '흐림'}


for key, val in zip(informations.keys(), informations.values()) :
#     print(key, val)
    # val['LGT'] -- 낙뢰 
    template = f"""{base_date[:4]}년 {base_date[4:6]}월 {base_date[-2:]}일 {key[:2]}시 {key[2:]}분 {(int(nx), int(ny))} 지역의 날씨는 """ 
    
    
    # 맑음(1), 구름많음(3), 흐림(4)
    if val['SKY'] :
        sky_temp = sky_code[int(val['SKY'])]
#         print("하늘 :", sky_temp)
        template += sky_temp + " "
    
    # (초단기) 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)
    if val['PTY'] :
        pty_temp = pyt_code[int(val['PTY'])]
#         print("강수 여부 :",pty_temp)
        template += pty_temp
        # 강수 있는 경우
        if val['RN1'] != '강수없음' :
            # RN1 1시간 강수량 
            rn1_temp = val['RN1']
#             print("강수량(1시간당) :",rn1_temp)
            template += f"시간당 {rn1_temp}mm "
    
    # 기온
    if val['T1H'] :
        t1h_temp = float(val['T1H'])
#         print(f"기온 : {t1h_temp}℃")
        template += f" 기온 {t1h_temp}℃ "
    # 습도
    if val['REH'] :
        reh_temp = float(val['REH'])
#         print(f"습도 : {reh_temp}%")
        template += f"습도 {reh_temp}% "
    # val['UUU'] -- 바람
    
    # val['VVV'] -- 바람
    
    # 풍향/ 풍속
    if val['VEC'] and val['WSD']:
        vec_temp = deg_to_dir(float(val['VEC']))
        wsd_temp = val['WSD']
#         print(f"풍속 :{vec_temp} 방향 {wsd_temp}m/s")
        
    template += f"풍속 {vec_temp} 방향 {wsd_temp}m/s"
    print(template)


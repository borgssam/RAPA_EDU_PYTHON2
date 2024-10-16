from flask import Flask, render_template
import requests
import xml.etree.ElementTree as ET
import folium
from branca.element import Figure

# Flask 앱 생성
app = Flask(__name__)

# 서비스키 정의
serviceKey = "b7foN4ax7Md969cw7GMz1efbW7iAuvmgjJUQvkfnLowN8K3II0/M+Bj5rWkmtB02chYuLv/voP6GzYWqYRqc3w=="

# API에서 약국 데이터를 불러오는 함수
def get_pharmacy_data():
    url = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire'
    params = {
        'serviceKey': serviceKey,
        'Q0': '서울특별시',
        'Q1': '금천구',
        'ORD': 'NAME',
        'pageNo': '1',
        'numOfRows': '10'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        try:
            # XML 형식으로 파싱
            root = ET.fromstring(response.text)
            pharmacies = []

            # XML 데이터에서 필요한 정보 추출
            for item in root.findall(".//item"):
                pharmacy_info = {
                    "이름": item.find("dutyName").text if item.find("dutyName") is not None else "정보 없음",
                    "주소": item.find("dutyAddr").text if item.find("dutyAddr") is not None else "정보 없음",
                    "전화번호": item.find("dutyTel").text if item.find("dutyTel") is not None else "정보 없음",
                    "진료시간": {
                        "월요일": item.find("dutyTime1c").text if item.find("dutyTime1c") is not None else "정보 없음",
                        "화요일": item.find("dutyTime2c").text if item.find("dutyTime2c") is not None else "정보 없음",
                        "수요일": item.find("dutyTime3c").text if item.find("dutyTime3c") is not None else "정보 없음",
                        "목요일": item.find("dutyTime4c").text if item.find("dutyTime4c") is not None else "정보 없음",
                        "금요일": item.find("dutyTime5c").text if item.find("dutyTime5c") is not None else "정보 없음",
                        "토요일": item.find("dutyTime6c").text if item.find("dutyTime6c") is not None else "정보 없음",
                        "일요일": item.find("dutyTime7c").text if item.find("dutyTime7c") is not None else "정보 없음"
                    },
                    "경도": item.find("wgs84Lon").text if item.find("wgs84Lon") is not None else "정보 없음",
                    "위도": item.find("wgs84Lat").text if item.find("wgs84Lat") is not None else "정보 없음"
                }
                pharmacies.append(pharmacy_info)
            return pharmacies

        except ET.ParseError:
            return []
    else:
        return []




# Flask 라우팅 설정
@app.route('/')
def pharmacy_list():
    # API에서 약국 데이터를 가져오기
    pharmacies = get_pharmacy_data()
    # HTML 파일로 렌더링
    return render_template('pharmacy_info.html', pharmacies=pharmacies)
# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)

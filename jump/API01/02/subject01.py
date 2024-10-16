import requests
import xml.etree.ElementTree as et

url = "http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire"
params = {
    "serviceKey": "XdCGOTEHiXh6aaLlwLI9To6GiZfn9kgxq9dOepmBLS+10MXdO+pusfkGJP/b3le+LJijEAWkZ73O0wtULT6xeA==",
    "Q0": "서울특별시",
    "Q1": "금천구",
    "QZ": "C",
    "ORD": "NAME",
    "pageNo": "1",
    "numOfRows": "154",
}

response = requests.get(url, params=params)
xml_data = response.content.decode("utf-8")

with open("subject01.xml", "w", encoding="utf-8") as f:
    f.write(xml_data)

# XML 파싱
root = et.fromstring(xml_data)

# 결과를 저장할 리스트
result_list = []

# 모든 item 요소를 찾아 순회
for item in root.findall(".//item"):
    name = item.find("dutyName")
    if name is not None:
        name = name.text

    for i in range(1, 6):
        start_time = item.find(f"dutyTime{i}s")
        end_time = item.find(f"dutyTime{i}c")

        if start_time is not None and end_time is not None:
            if int(end_time.text) > 1800:  # 문자열을 정수로 변환하여 비교
                if name not in result_list:
                    result_list.append(name)
                break  # 하나라도 조건을 만족하면 다음 item으로

for item in result_list:
    print(item)

print(len(result_list))

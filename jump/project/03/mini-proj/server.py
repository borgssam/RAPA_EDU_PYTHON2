# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import json

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})  # 모든 도메인에서 접근 허용

# # JSON 파일 로드
# with open('서울교통공사_지하철혼잡도정보_20240331.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# @app.route('/get_schedule', methods=['GET'])
# def get_schedule():
#     departure_station = request.args.get('departure_station', '').strip()
#     desired_time = request.args.get('desired_time', '').strip()
#     line_number = request.args.get('line_number', '').replace('호선', '').strip()

#     print(f"출발역: {departure_station}, 호선: {line_number}, 시간: {desired_time}")

#     result = get_congestion(data, departure_station, "상선", line_number, desired_time)
#     return jsonify(result)

# def get_congestion(data, departure_station, line_type, line_number, time):
#     try:
#         # 시간 변환 및 로그 출력
#         print(f"요청된 시간: {time}")

#         if '시' in time:
#             parts = time.replace('분', '').split('시')
#             hour = int(parts[0])
#             minute = int(parts[1]) if len(parts) > 1 else 0
#         else:
#             raise ValueError("Invalid time format")

#         minute = 30 if 15 <= minute <= 44 else 0
#         if minute == 0 and hour < 23:
#             hour += 1

#         adjusted_times = [
#             f"{hour}시{minute:02d}분",
#             f"{hour - 1 if minute == 0 else hour}시{(minute - 30) % 60:02d}분",
#             f"{hour + 1 if minute == 30 else hour}시{(minute + 30) % 60:02d}분"
#         ]
        
#         print(f"찾는 시간 목록: {adjusted_times}")

#         results = {}
#         keys = ["comp", "bf_comp", "af_comp"]

#         # 데이터 매칭 로직 개선
#         for entry in data:
#             if (entry['출발역'].strip() == departure_station and
#                 entry['상하구분'].strip() == line_type and
#                 str(entry['호선']).strip() == line_number and
#                 entry['요일구분'].strip() == '평일'):
                
#                 print(f"매칭된 항목: {entry}")

#                 for key, adj_time in zip(keys, adjusted_times):
#                     if adj_time in entry:
#                         results[key] = entry[adj_time].strip()
#                         print(f"{adj_time}의 데이터: {entry[adj_time]}")

#         return results if results else {
#             "comp": "정보 없음", "bf_comp": "정보 없음", "af_comp": "정보 없음"
#         }
#     except ValueError as e:
#         print(f"시간 형식 오류: {e}")
#         return {"comp": "시간 형식 오류", "bf_comp": "N/A", "af_comp": "N/A"}

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)



from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # 모든 도메인에서 접근 허용

# JSON 파일 로드
with open('서울교통공사_지하철혼잡도정보_20240331.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

@app.route('/get_schedule', methods=['GET'])
def get_schedule():
    departure_station = request.args.get('departure_station', '').strip()
    desired_time = request.args.get('desired_time', '').strip()
    line_number = request.args.get('line_number', '').replace('호선', '').strip()

    print(f"출발역: {departure_station}, 호선: {line_number}, 시간: {desired_time}")

    result = get_congestion(data, departure_station, "상선", line_number, desired_time)
    return jsonify(result)

def convert_congestion(congestion_val):
    congestion_val = float(congestion_val)
    if congestion_val <= 25.0:
        return "원활"
    elif congestion_val <= 34.0:
        return "보통"
    elif congestion_val <= 60.0:
        return "복잡"
    else:
        return "지옥"


def get_congestion(data, departure_station, line_type, line_number, time):
    try:
        # 시간 변환 및 로그 출력
        print(f"요청된 시간: {time}")

        if '시' in time:
            parts = time.replace('분', '').split('시')
            hour = int(parts[0])
            minute = int(parts[1]) if len(parts) > 1 else 0
        else:
            raise ValueError("Invalid time format")

        minute = 30 if 15 <= minute <= 44 else 0
        if minute == 0 and hour < 23:
            hour += 1

        adjusted_times = [
            f"{hour}시{minute:02d}분",
            f"{hour - 1 if minute == 0 else hour}시{(minute - 30) % 60:02d}분",
            f"{hour + 1 if minute == 30 else hour}시{(minute + 30) % 60:02d}분"
        ]
        
        print(f"찾는 시간 목록: {adjusted_times}")

        results = {}
        keys = ["comp", "bf_comp", "af_comp"]

        # 데이터 매칭 로직 개선
        for entry in data:
            if (entry['출발역'].strip() == departure_station and
                entry['상하구분'].strip() == line_type and
                str(entry['호선']).strip() == line_number and
                entry['요일구분'].strip() == '평일'):
                
                print(f"매칭된 항목: {entry}")

                for key, adj_time in zip(keys, adjusted_times):
                    if adj_time in entry:
                        results[key] = convert_congestion(entry[adj_time].strip())
                        print(f"{adj_time}의 데이터: {entry[adj_time]}")

        return results if results else {
            "comp": "정보 없음", "bf_comp": "정보 없음", "af_comp": "정보 없음"
        }
    except ValueError as e:
        print(f"시간 형식 오류: {e}")
        return {"comp": "시간 형식 오류", "bf_comp": "N/A", "af_comp": "N/A"}

if __name__ == '__main__':
    app.run(debug=True, port=5001)




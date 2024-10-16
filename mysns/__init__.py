
from flask import Flask
from flask.templating import render_template
from flask import  request, jsonify, redirect, session, url_for
import requests
import json
import urllib.request

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is API 연동 Test Context!'

@app.route('/about')
def about():
    return render_template('about.html') 


@app.route('/search', methods=['GET', 'POST'])
def search():
    client_id = "4BXFs932fHZNNjmkbDf4"  # "YOUR_CLIENT_ID"
    client_secret = "s05_WG8QNf"  # "YOUR_CLIENT_SECRET"
   # POST 방식으로 요청이 들어왔을 경우
    if request.method == 'POST':
        query = request.form['query']  # 폼에서 'query'라는 입력 필드의 값을 가져옴
        encText = urllib.parse.quote(query)  # 검색어를 URL 인코딩하여 API에 전달할 수 있는 형태로 변환
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # Naver 블로그 검색 API URL에 검색어 추가

        # Naver API 요청 준비
        request_api = urllib.request.Request(url)  # 요청 객체 생성
        request_api.add_header("X-Naver-Client-Id", client_id)  # 클라이언트 ID를 요청 헤더에 추가
        request_api.add_header("X-Naver-Client-Secret", client_secret)  # 클라이언트 시크릿 키를 요청 헤더에 추가

        # API 호출
        response = urllib.request.urlopen(request_api)  # API로부터 응답 받기
        rescode = response.getcode()  # HTTP 응답 코드 확인

        # 응답이 200 (성공)이면 결과를 처리
        if rescode == 200:
            response_body = response.read()  # 응답 본문 읽기
            data = json.loads(response_body.decode('utf-8'))  # JSON 형식의 응답을 Python 딕셔너리로 파싱

            # 검색 결과를 템플릿에 전달하여 페이지에 렌더링
            return render_template('search.html', items=data['items'], query=query)  # 검색 결과를 search.html로 전달
        else:
            return f"Error Code: {rescode}"  # 에러 코드가 200이 아니면 에러 메시지 반환

    # GET 요청일 경우 검색 폼만 표시
    return render_template('search.html')  # 검색어 입력 폼만 표시

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True) 
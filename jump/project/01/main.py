from flask import Flask, request, jsonify, render_template
import requests


app = Flask(__name__, static_folder='static')

CLIENT_ID = 'q4oOdfIaFWVDOMtcu3hR'
CLIENT_SECRET = 'ViiMKGqq40' 

# Map the root URL '/' to the index function
@app.route('/')
def index():
    return render_template('index.html')

# 네이버 검색 API 호출 라우트
@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')
@app.route('/search/naver', methods=['GET'])
def search_naver():
    query = request.args.get('query')
    api_url = f"https://openapi.naver.com/v1/search/webkr.json?query={query}"
    
    headers = {
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'API 호출 실패'}), 500
if __name__ == '__main__':
    app.run(port=8000, debug=True)

    
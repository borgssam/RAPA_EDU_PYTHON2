import urllib.parse
from flask import Flask
from flask.templating import render_template
from flask import request
import requests
import json
import urllib.request

def create_app():
  app = Flask(__name__)

  @app.route('/')
  def home():
      return 'Hello, RAPA'
  
  @app.route('/about')
  def about():
     return render_template('about.html')

  @app.route('/search',methods=['GET','POST'])
  def search():
    client_id="PJBuo84Jx_pw40R2ze8I"
    client_secret = "jNzR0a8Ws5"
    if request.method == 'POST':
      print("search 요청받음-------------")
      query = request.form['query']
      print(query)
      encParam = urllib.parse.quote(query)
      url = "https://openapi.naver.com/v1/search/blog?query=" +encParam

      #Naver API 요청
      request_api = urllib.request.Request(url)
      request_api.add_header("X-Naver-Client-id", client_id)
      request_api.add_header("X-Naver-Client-Secret", client_secret)

      #API 요청(호출)
      response = urllib.request.urlopen(request_api)

      rescode = response.getcode()

      #응답 성공이면
      if rescode == 200:
         response_body = response.read()
         data = json.loads(response_body.decode('utf-8'))

         return render_template('search.html', items=data['items'], query=query)
      else:
         return f"Error : {rescode}"


    return render_template('search.html')
    
    

  return app
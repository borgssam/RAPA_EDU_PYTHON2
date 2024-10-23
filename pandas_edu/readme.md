Day 1
# 환경설정
  - 파이썬 설치
    www.python.org > 3.10.3 version
    add python to path 체크
    확인 python --version
  - vscode 설치
  - 가상환경
    python -m venv para3103
  - 가상환경 활성화
    c:\\edu\edu_python : rapa3102\Scripts\activate
  - 모듈설치
    (rapa3103) c:\edu\edu_pyton :  pip install -r requirements.txt    

  - vscode 확장팩
    python jupyter  

# 판다스 
  시리즈 : 인덱스를 가지고 있는 1차배열
  데이터프레임: 인덱스와 시리즈 집합으로 구성, 2차배열구조

  시리즈 : 리스트, 튜블 : 인덱스 지정 => 지정된 배열 
                          인덱스 미지정 => 수자 범위로
           딕셔너리 :    키 : 인덱스 ,  값 : 데이터

           시리즈 연산자 수자 : 숫자가 시리즈 각 요소 모두 적용계산
           시리즈 연산자 시리즈 : 인덱스 기준으로 적용계산, 한 쪽 인덱스가 없으면 NaN(결과)  

           원소선택: 인덱스 정수  [0], [2:4] [[2,4]]
                   : 인덱스 라벨 ['홍길동']  ['홍길동','강감찬'] [['홍길동','강감찬']]
  
  데이터 프레임 딕셔너리 
          dict = { '키1': [데이터1, 데이터2, 데이터3],'키2': [데이터1, 데이터2, 데이터3] }
          pd.DataFrame(dict )

          인덱스와 컬럼명 전체을 교체
          인덱스와 컬럼명 부분교체


          데이터프레임 연산자 수자 : 숫자가 시리즈 각 요소 모두 적용계산
          데이터프레임 연산자 데이터프레임 : 인덱스 기준으로 적용계산, 한 쪽 인덱스가 없으면 NaN(결과)  
          
Day 2          
# 데이터 입출력
  외부파일 입출력
    -csv     :  read_csv,   to_csv
    -json    :  read_json,  to_json
    -html    :  read_html,  to_html
    -excel   :  read_excel, to_excel

    해더포함여부: header
    인덱스 사용: index_col
  
# 기술분석
  자료 : auto-mpg
  df.head() : 처음 5행출력
  df.tail() : 마지막 5행 출력
  df.shape  : 열과 행의 크기
  df.info() : 각 열의 행의수, 타입
  df.describe() : 각열의 행의수, 평균, 표준편차, 최소, 1분위,중위,3분위, 최대

  통계함수
  df.mean() : 전체 컬럼 평균
  df['컬럼1','컬럼2'].mean() : 컬럼1,컬럼2의 평균
  df.median() : 전체컬럼 중간값
  df['컬럼1','컬럼2'].median() : 컬럼1,컬럼2의 중간값
  df.max() : 전체컬럼 최대값 (3분위 + (IQR*1.5) )
  df['컬럼1','컬럼2'].max() : 컬럼1,컬럼2의 최대값
  df.min() : 전체컬럼 최소값 (1분위 - (IQR*1.5) )
  df['컬럼1','컬럼2'].min() : 컬럼1,컬럼2의 최소값
  df.std() : 전체컬럼 표준편차
  df['컬럼1','컬럼2'].std() : 컬럼1,컬럼2의 표준편차
  df.corr() : 전체컬럼 상관계수
  df['컬럼1','컬럼2'].corr() : 컬럼1,컬럼2의 상관계



# 시각화
  - 판다스
    df.plot(kind='line, bar, barh, his, box, kde, area, pie, scatter')
  - matplotlib
    plt.plot(x축데이터, y축데이터) : 선그래프
    plt.fill_between(x축데이터, y축데이터) : 면적그래프
    plt.plot(kind='bar' , x축데이터, y축데이터) : 막대그래프
    plt.hist(x축데이터, y축데이터) : 히스토그램
    plt.scatter(x축데이터, y축데이터) : 산점도
    plt.pie(데이터시리즈) : 파이그래프
    plt.boxplot(x축데이터, y축데이터) : 박스플롯
    plt.kdeplot(x축데이터, y축데이터) : 커널밀도
  - seaborn
    sns.heatmap(상관계수행렬) : 히트맵(상관계수행렬)
    sns.barplot(데이터프래임) : 막대그래프
    sns.boxplot(데이터프래임) : 박스플롯
    sns.violineplot(데이터프래임) : 바이올린 플롯
    



          
                  

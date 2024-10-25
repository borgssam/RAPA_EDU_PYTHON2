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

Day 3 
데이터 전처리
이상치 : 다른값 확연히 차이나는 값, 데이터분석 왜곡 => 분석시 제외
  IQR:
     IQR : 3분위 - 1분위
     1분위 - (IQR*1.5) <  유효범위 < 3분위 + (IQR*1.5)

  Z-Score: 표준편차 단위
    +-1 : 68%
    +-2 : 95%
    +-3 : 99.7%

    이상치 식별할때 +-2, +-3 상용합니다.
   

결측치
  누락된 값 , 데이터분석 악영향 => 제거, 값대체(평균,중위값,최빈값,앞자료,뒤자료 등)
  isnull : 결측치 탐색
  dropna : 결측치 제거
  fillna : 결측치 값 대체
  fillna(method='ffill') : 결측치의 앞 자료로 대체
  fillna(method='bfill') : 결측치의 뒤 자료로 대체
  shift : 자료를 전체적으로 이동시킬때 사용

중복데이터
  duplicated() : 중복데이터 탐색
  drop_duplicates() : 중복데이터제거(keep 기본값이 first)
  drop_duplicates(keep='first') : 중복데이터 맨 앞 자료를 제외하고 제거
  drop_duplicates(keep='last')  : 중복데이터 맨 뒤 자료를 제외하고 제거
  drop_duplicates(keep=False)   : 중복데이터 모든자료를 제거


값조정
  표준화:
    - 단위조정
    - 표준정규분포화 : StandardSclaer  fit_transform
  정규화
    - MinMaxScaler  fit_transform

  더미변수
    라벨엔코더 : LabelEncoder() 
    오리, 토끼, 양 => 1,2,3

    원핫인코딩 : OneHotEncoder,get_dummies
    오리  토끼    양
    1      0      0
    0      1      0
    0      0      1

시리얼 데이터
  str, Timestamp, Period 

Day 4
함수매핑
  apply  : 데이터프레임의 열, 행
  map    : 시리즈
  pipe   : 데이터프레임, 체이닝


열재구성
  # 데이터프레임 생성
  data = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
  # 열 순서 변경
  data = data[['C', 'A', 'B']]

그룹연산
  df.groupby('컬럼명')
  통계함수도 상용합니다.
  agg() 메소드를 사용하여 그룹 연산을 수행한다

데이터프레임 합치기
  수평결합
     merge
     join  (교집합)
  수직결합
     concat

멀티인덱스
  df.index = pl.Multiindex.from_tuples([(1차인덱스,2차인덱스),(1차인덱스,2차인덱스)])

피벗
  # 데이터프레임 생성
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-01', '2021-01-02'],'Category': ['A', 'B', 'A'], 'Value': [1, 2, 3]})
  # 피벗 테이블 생성
    pivot_table = data.pivot(index='Date', columns='Category', values='Value')

  

    



          
                  

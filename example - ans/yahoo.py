3. 영화 추천 시스템 구축
목표: 사용자 데이터를 기반으로 영화 추천 시스템을 개발한다.
데이터: movies.csv ratings.csv

미션 내용:
데이터 분석: 영화 평점 데이터를 로드하고 분석한다.
기술 분석: 특정 영화의 평균 평점, 장르별 선호도 등을 pandas로 분석하여 시각화한다.
협업 필터링: 사용자 기반 또는 아이템 기반의 협업 필터링 알고리즘을 구현한다.
성능 평가: RMSE, MAE 등의 지표로 추천 시스템의 성능을 평가한다.

import pandas as pd
import numpy as np
import os

# data 디렉토리 생성
if not os.path.exists('./data'):
    os.makedirs('./data')

# ratings.csv 데이터 생성
ratings_data = {
    'userId': np.random.randint(1, 1000, size=10000),  # 1부터 999까지의 사용자 ID
    'movieId': np.random.randint(1, 2000, size=10000),  # 1부터 1999까지의 영화 ID
    'rating': np.random.uniform(1, 5, size=10000),  # 1부터 5까지의 평점
    'timestamp': np.random.randint(1_000_000_000, 1_100_000_000, size=10000)  # 임의의 타임스탬프
}

ratings_df = pd.DataFrame(ratings_data)
ratings_df.to_csv('./data/ratings.csv', index=False)  # CSV 파일로 저장
print("ratings.csv 파일 생성 완료!")

# movies.csv 데이터 생성
movies_data = {
    'movieId': np.arange(1, 2000),  # 1부터 1999까지의 영화 ID
    'title': [f'Movie {i}' for i in range(1, 2000)],  # 영화 제목 생성
    'genres': np.random.choice(['Action', 'Comedy', 'Drama', 'Horror', 'Romance'], size=1999)  # 임의의 장르
}

movies_df = pd.DataFrame(movies_data)
movies_df.to_csv('./data/movies.csv', index=False)  # CSV 파일로 저장
print("movies.csv 파일 생성 완료!")


import pandas as pd
import numpy as np
import os

# data 디렉토리 생성
if not os.path.exists('./data'):
    os.makedirs('./data')

# ratings.csv 데이터 생성
ratings_data = {
    'userId': np.random.randint(1, 1000, size=10000),  # 1부터 999까지의 사용자 ID
    'movieId': np.random.randint(1, 2000, size=10000),  # 1부터 1999까지의 영화 ID
    'rating': np.random.uniform(1, 5, size=10000),  # 1부터 5까지의 평점
    'timestamp': np.random.randint(1_000_000_000, 1_100_000_000, size=10000)  # 임의의 타임스탬프
}

ratings_df = pd.DataFrame(ratings_data)
ratings_df.to_csv('./data/ratings.csv', index=False)  # CSV 파일로 저장
print("ratings.csv 파일 생성 완료!")

# movies.csv 데이터 생성
movies_data = {
    'movieId': np.arange(1, 2000),  # 1부터 1999까지의 영화 ID
    'title': [f'Movie {i}' for i in range(1, 2000)],  # 영화 제목 생성
    'genres': np.random.choice(['Action', 'Comedy', 'Drama', 'Horror', 'Romance'], size=1999)  # 임의의 장르
}

movies_df = pd.DataFrame(movies_data)
movies_df.to_csv('./data/movies.csv', index=False)  # CSV 파일로 저장
print("movies.csv 파일 생성 완료!")


# CSV 파일 불러오기
ratings = pd.read_csv('./data/ratings.csv')  # 평점 데이터
movies = pd.read_csv('./data/movies.csv')    # 영화 데이터

# 특정 영화의 평균 평점 계산 (실제 존재하는 영화 제목 사용)
movie_title = 'Movie 1'  # 실제 존재하는 제목

# 해당 영화 ID 가져오기
movie_id_series = movies[movies['title'] == movie_title]['movieId']

if not movie_id_series.empty:
    movie_id = movie_id_series.values[0]  # 영화 ID 가져오기
    average_rating = ratings[ratings['movieId'] == movie_id]['rating'].mean()  # 평균 평점 계산
    print(f"{movie_title}의 평균 평점: {average_rating:.2f}")
else:
    print(f"{movie_title}이(가) movies 데이터프레임에 존재하지 않습니다.")

# 장르별 선호도 분석
# 장르 정보를 분리하여 데이터프레임 생성
genre_data = ratings.merge(movies, on='movieId')

# 각 장르의 평균 평점 계산
genre_preferences = genre_data.groupby('genres')['rating'].mean().reset_index()

print("\n장르별 평균 평점:")
print(genre_preferences)


import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rc('font', family='NanumGothic')  # 'NanumGothic'을 설치한 경우

# 그래프 다시 그리기
plt.figure(figsize=(10, 6))
sns.barplot(x='genres', y='rating', data=genre_preferences.sort_values(by='rating', ascending=False))
plt.title("장르별 평균 평점")
plt.xlabel("장르")
plt.ylabel("평균 평점")
plt.xticks(rotation=45)
plt.tight_layout()  # 그래프가 겹치지 않도록 조정
plt.show()

여기이후에만 수정하세요


import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 중복된 userId와 movieId 조합에 대해 평균 평점 사용
ratings_cleaned = ratings.groupby(['movieId', 'userId']).agg({'rating': 'mean'}).reset_index()

# 영화-사용자 행렬 생성 (pivot 테이블)
movie_user_matrix = ratings_cleaned.pivot(index='movieId', columns='userId', values='rating').fillna(0)

# 코사인 유사도 계산
similarity_matrix = cosine_similarity(movie_user_matrix)

# DataFrame으로 변환
similarity_df = pd.DataFrame(similarity_matrix, index=movie_user_matrix.index, columns=movie_user_matrix.index)

# 특정 영화에 대해 추천할 영화 찾기 (예: 'Toy Story (1995)')
movie_title = 'Toy Story (1995)'
movie_id = movies[movies['title'] == movie_title]['movieId'].values[0]
similar_movies = similarity_df[movie_id].sort_values(ascending=False)[1:6]  # 상위 5개 영화 추천

recommended_movie_ids = similar_movies.index
recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)]

print("추천 영화:")
print(recommended_movies[['title', 'genres']])

ratings.csv 파일 생성 완료!
movies.csv 파일 생성 완료!
Movie 1의 평균 평점: 2.88

장르별 평균 평점:
    genres    rating
0   Action  3.041725
1   Comedy  3.011745
2    Drama  2.961035
3   Horror  3.013725
4  Romance  3.001280

---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[17], line 19
     17 # 특정 영화에 대해 추천할 영화 찾기 (예: 'Toy Story (1995)')
     18 movie_title = 'Toy Story (1995)'
---> 19 movie_id = movies[movies['title'] == movie_title]['movieId'].values[0]
     20 similar_movies = similarity_df[movie_id].sort_values(ascending=False)[1:6]  # 상위 5개 영화 추천
     22 recommended_movie_ids = similar_movies.index

IndexError: index 0 is out of bounds for axis 0 with size 0
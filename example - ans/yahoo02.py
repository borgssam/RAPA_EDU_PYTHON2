import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV 파일에서 주식 데이터 불러오기
ticker = "AAPL"  # 분석할 종목 (예: 애플)
data = pd.read_csv(f"{ticker}_stock_data.csv", parse_dates=True, index_col='Date')

# 이동 평균선(MA) 계산
data['MA20'] = data['Close'].rolling(window=20).mean()  # 20일 이동 평균
data['MA50'] = data['Close'].rolling(window=50).mean()  # 50일 이동 평균

# 볼린저 밴드 계산
data['Upper Band'] = data['MA20'] + (data['Close'].rolling(window=20).std() * 2)
data['Lower Band'] = data['MA20'] - (data['Close'].rolling(window=20).std() * 2)

# 시각화
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['MA20'], label='20 Day MA', color='orange')
plt.plot(data['MA50'], label='50 Day MA', color='green')
plt.fill_between(data.index, data['Upper Band'], data['Lower Band'], color='gray', alpha=0.5, label='Bollinger Bands')
plt.title(f'{ticker} Stock Price and Technical Analysis')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

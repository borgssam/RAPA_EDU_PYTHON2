import pandas as pd
# 리스트로 시리즈 생성
s_list = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("리스트로 생성한 시리즈:")
print(s_list)
# 딕셔너리로 시리즈 생성
s_dict = pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400})
print("\n딕셔너리로 생성한 시리즈:")
print(s_dict)

'''
주식 데이터 읽어 시각화 -> 저장
yahoo 사이트 제공
pip install pandas_datareader
'''
from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ kosdaq.pickle, kospi.pickle 읽기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# https://github.com/pykwon/python 에서 다운받기 kosdaq.pickle, kospi.pickle
# pickle로 저장된 코스닥/코스피 종목 코드 읽기
kosdaq = pd.read_pickle("./kosdaq.pickle")
kospi = pd.read_pickle("./kospi.pickle")
print(kosdaq.head(10))
print(kospi.head(10))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
start_date = "2018-01-01"
tickers = ['003380.KQ', '251270.KS']

holding_df = data.get_data_yahoo(tickers[0], start_date)
print(holding_df.head(3), len(holding_df))

print()
net_df = data.get_data_yahoo(tickers[1], start_date)
print(net_df.head(3), len(net_df))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 읽은 자료 파일로 저장 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
holding_df.to_pickle('holding.pickle') # 저장
net_df.to_csv('new.csv') # 저장

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 시각화 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
plt.plot(net_df)
plt.show()

import seaborn as sns
sns.scatterplot(x = 'Open', y = 'Close', data=net_df) # net_df 파일 그래프로
plt.show()









print('경연대회 같은 곳을 나가면 어디서 데이터를 수집하고 가공을 하는지가 제일 중요하다')

# data.go.kr 사이트에서 어느 음식점 매출데이터와 날씨 데이터를 이용하여 강수 여부에 따른 매출의 평균에 차이를 검정

# 비가 올 때의 매출액
# 비가 안올 때의 매출액

# 집단 2개
# 귀무 : 강수량에 따른 매출액에 차이가 없다.
# 대립 : 강수량에 따른 매출액에 차이가 있다.

# 두개의 집단의 확률이 동일해야한다 등분산
# 공분산

import numpy as np
import pandas as pd
import scipy.stats as stats

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 자료 읽기1 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv",
                         dtype={'YMD':'object'}) # int를 오브젝으로 바꿈 (병합하기 위해서)
# 0   YMD     328 non-null    int64 -> 오브젝트
print(sales_data.head(3))
print(sales_data.info())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 자료 읽기2 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-','')) # tm에 2018-06-01 -> 20180601
print(wt_data.head(3))
print(wt_data.info())
#  1   tm      702 non-null    object 

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 날짜로 자료1,2를 병합 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm') # 왼쪽이 기준 (sales_data)
print(frame.head(3))
#         YMD    AMT  CNT  stnId        tm  ...  maxTa  sumRn  maxWs  avgWs  ddMes
# 0  20190514      0    1    108  20190514  ...   26.9    0.0    4.1    1.6    0.0
# 1  20190519  18000    1    108  20190519  ...   21.6   22.0    2.7    1.2    0.0
# 2  20190521  50000    4    108  20190521  ...   23.8    0.0    5.9    2.9    0.0

print(len(frame)) # 328

print(frame.columns)
# Index(['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn',
#        'maxWs', 'avgWs', 'ddMes'],
#       dtype='object')

data = frame.iloc[:, [0, 1, 7, 8]] # 'YMD', 'AMT', 'maxTa', 'sumRn'
print(data.head(3), len(data)) # 원하는 열만 가져오기, 328
print(data.isnull().sum()) # 결측치 없음

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 독립표본 t검정 : 강수 여부에 매출액의 평균에 차이가 있는가? 경고 무시 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(data['sumRn'] > 0) # False, False ...

# data['rain_yn'] = (data['sumRn'] > 0).astype(int) # 비옴:1, 비안옴:0
# print(data.head(3))

# print(True * 1, False * 1) # 1 0
data['rain_yn'] = (data.loc[:, ('sumRn')] > 0) * 1 

print(data.head(3))
#         YMD    AMT  maxTa  sumRn  rain_yn
# 0  20190514      0   26.9    0.0        0
# 1  20190519  18000   21.6   22.0        1
# 2  20190521  50000   23.8    0.0        0

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 시각화 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
import matplotlib.pyplot as plt

sp = np.array(data.iloc[:, [1, 4]])
print(sp[:2]) # [[    0     0]  [18000     1]] 이해를 돕기위해서

tg1 = sp[sp[:, 1] == 0, 0] # 비가 안올때의 매출액
tg2 = sp[sp[:, 1] == 1, 0] # 비가 올때의 매출액

print(tg1[:3])
print(tg2[:3])

# plt.plot(tg1)
# plt.show()
# plt.plot(tg2)
# plt.show()

# plt.boxplot([tg1, tg2], notch = True, meanline = True, showmeans = True)
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 두 집단의 각 평균  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('비 안올 때 : ', np.mean(tg1), '비 올 때 : ', np.mean(tg2))
# 비 안올 때 :  761040.2542 vs 757331.5217

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정규성 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(len(tg1), len(tg2)) # 236 92
print(stats.shapiro(tg1). pvalue) # 0.05604 > 0.05 만족
print(stats.shapiro(tg2). pvalue) # 0.88273 > 0.05 만족

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 등분산성 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(stats.levene(tg1, tg2).pvalue) # 0.71234 > 0.05 만족

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 귀무가설 채택 or 귀무가설 기각 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(stats.ttest_ind(tg1, tg2, equal_var = True))
# Ttest_indResult(statistic=0.10109828602924716, pvalue=0.919534587722196)
# 해석 : pvalue=0.91953 > 0.05 이므로 귀무가설 채택
# 강수량에 따른 매출액의 평균에 차이는 없다










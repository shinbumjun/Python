print('******두 집단 평균 또는 비율 차이 검정')
# 두 집단의 가설검정 – 실습 시 분산을 알지 못하는 것으로 한정하겠다.
# 선행 조건 : 정규성, 등분산성

# 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.

# 두개의 집단이 확률이 동일해야한다 등분산
# 공분산

print('실습1) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정')
# 귀무 : 남녀 간의 파이썬 시험 평균에 차이가 없다.
# 대립 : 남녀 간의 파이썬 시험 평균에 차이가 있다.

import numpy as np
import pandas as pd
from numpy import average
from scipy import stats

male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

print(average(male), ' ', average(female)) # 83.8 vs 72.24

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정규성, 등분산성은 생략 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
two_sample = stats.ttest_ind(male, female) # 두 개의 표본에 대해 곡립표본 t검정
print(two_sample)
# Ttest_indResult(statistic=1.233193127, pvalue=0.2525076844)
# 해석 : pvalue = 0.2525076844 > 0.05 이므로 귀무 채택

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('실습2) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv')
data = pd.read_csv("../testdata/two_sample.csv")
print(data.head(3))
#    no  gender  method  survey  score
# 0   1       1       1       1    5.1
# 1   2       1       2       0    NaN
# 2   3       1       1       1    4.7

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 원하는 열만 표현 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
ms = data[['method', 'score']]
print(ms.head(3))
#    method  score
# 0       1    5.1
# 1       2    NaN
# 2       1    4.7

m1 = ms[ms['method'] == 1] # 방법1
m2 = ms[ms['method'] == 2] # 방법2

score1 = m1['score']
score2 = m2['score']
# print(score1)
# print(score2)

# 참고 : df.isnull().sum()

# sco1 = score1.fillna(0) # NaN으로 0으로 채우기
# sco2 = score2.fillna(0) # NaN으로 0으로 채우기
sco1 = score1.fillna(score1.mean()) # NaN으로 평균으로 채우기
sco2 = score2.fillna(score2.mean()) # NaN으로 평균으로 채우기

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정규성 (0.05보다 크면 만족) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(stats.shapiro(sco1)) # pvalue=0.36799
print(stats.shapiro(sco2)) # pvalue=0.67141

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정규성 시각화 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.histplot(sco1, kde = True)
# sns.histplot(sco2, kde = True)
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 등분산성 확인 : 0.05 보다 크면 만족 (pvalue만 보이게) 방법은 다양하다 (0.05보다 크면 만족) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(stats.levene(sco1, sco2).pvalue) # 0.45684 (제일 많이 사용)
print(stats.fligner(sco1, sco2).pvalue) # 0.44323
print(stats.bartlett(sco1, sco2).pvalue) # 0.26789 비모수 검정 (30개 이하일때)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정규성과 등분산성을 만족 or 불만족 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
result = stats.ttest_ind(sco1, sco2, equal_var=True) # 등분산성 만족 o
# result = stats.ttest_ind(sco1, sco2, equeal_var=False) # 등분산성 만족 x
print('검정통계량t :%.5f, p-value:%.5f'%result)
# 해석 : p-value:0.84505 > 0.05 이므로 귀무채택
print('결론 : 두 가지 교육방법에 따른 평균시험 점수에 차이가 없다') 

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정규성 만족 못한 경우 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
stats.mannwhitneyu(sco1, sco2) # 표본의 크기가 다를 때
# stats.wilcoxon(sco1, sco2) # 표본의 크기가 같을 때





















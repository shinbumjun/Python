# anal5 마지막
'''
ANOVA(분산분석)
***세 집단 이상의 평균의 차이를 검정
전제조건 : 독립성, 정규성, 불편성(등분산성)
독립변수 : 범주형, 종속변수 : 연속성
f-value = 그룹간분산 / 그룹내분산
# 집단과 분산이 집단 내 분산보다 충분히 큰 것인가를 파악하는 것.
종속변수의 변화(분산) 폭이 독립변수에 의해 주로 기안하는지를 파악하는 것.

참고) 독립성(학년과 나이x), 정규성(볼록한 그래프), 등분산성(두개의 집단의 확률이 동일해야한다)
'''

# 세 개 이상의 모집단에 대한 가설검정 – 분산분석
# ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고 요인
# 에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.
# *** 서로 독립인 세 집단의 평균 차이 검정

# 하나의 요인에 속한 집단이 복수 : 일원분산분석(one-way anova)
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv') 

# 귀무 : 세 가지 교육방법에 따른 교육생 실기시험의 평균에 차이가 없다
# 대립 : 세 가지 교육방법에 따른 교육생 실기시험의 평균에 차이가 있다

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
import statsmodels.api as sm

data = pd.read_csv("../testdata/three_sample.csv")
print(data.head(3), len(data)) # 80
#    no  method  survey  score
# 0   1       1       1     72
# 1   2       3       1     87
# 2   3       2       1     78

print(data.describe()) # 종합

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('boxplot으로 이상치를 확인')
import matplotlib.pyplot as plt
# plt.boxplot(data.score)
# plt.hist(data.score)
# plt.show()

data = data.query('score <= 100') # 스코어가 100이하 (아웃라이너)
print(data.describe()) # 종합

# plt.hist(data.score)
# plt.show()
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('등분산 확인 : 만족하면 anove, 만족하지 않으면 welch_anova')
print('등분산을 만족하지 않으면 데이터 가공을 생각할 수도 있다 - 표준화, 정규화, transformation(자연log를 씌움)')
result = data[['method', 'score']]
# print(result)
m1 = result[result['method'] == 1]
m2 = result[result['method'] == 2]
m3 = result[result['method'] == 3]
score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print('등분산성 확인 : ', stats.levene(score1, score2, score3).pvalue) # 0.113228506 > 0.05 만족

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('정규성 확인')
print(stats.shapiro(score1))
print(stats.shapiro(score2))
print(stats.shapiro(score3))

print('2개씩 보는 방법')
print(stats.ks_2samp(score1, score2))
print(stats.ks_2samp(score1, score3))
print(stats.ks_2samp(score2, score3))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('독립성 확인 : 상관관계 등으로 확인')

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('교육방법별 건수 : 교차표')
data2 = pd.crosstab(index = data['method'], columns = 'count')
data2.index = ['방법1', '방법2', '방법3']
print(data2)
# col_0  count
# 방법1       26
# 방법2       28
# 방법3       24

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('교육방법별 만족여부 건수 : 교차표')
data3 = pd.crosstab(data.method, data.survey)
data3.index = ['방법1', '방법2', '방법3']
data3.columns = ['만족', '불만족']
print(data3)
#      만족  불만족
# 방법1   9   17
# 방법2  10   18
# 방법3   8   16

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('f통계량을 얻기 위해 회귀분석 모델을 사용') # 최소제곱법으로 절편과 기울기

lm = ols('data["score"] ~ C(data["method"])', data = data).fit() # C(독립벼변수...) : 범주형임을 알림
table = sm.stats.anova_lm(lm, typ = 1)
print(table) # 분산 분석표
#                      df        sum_sq     mean_sq         F     PR(>F)
# C(data["method"])   2.0     28.907967   14.453984  0.062312  0.939639 - 처리
# Residual           75.0  17397.207418  231.962766       NaN       NaN - 오차

# df(자유도), sum_sq(처리제곱합), mean_sq(처리제곱평균), F
# p-value : 0.939639 > 0.05 이므로 귀무 채택. 세 가지 교육방법에 따른 교육생 실기시험의 평균에 차이가 없다.
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
import numpy as np
print(np.mean(score1), np.mean(score2), np.mean(score3))
# 67.38(집단1) 68.35(집단2) 68.875(집단3) 평균의 차이가 있나? 

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('사후 검정(Post Hoc Test) : 분산분석은 세 개 이상의 집단에 평균에 차이 유무만을 알려줌')
print('세 개 이상의 집단 각각의 집단 간 평균의 차이를 알고 싶은 경우') # 차이가 날 경우 보는것이 좋음

from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_result = pairwise_tukeyhsd(data.score, groups = data.method)
print(turkey_result) # 차이가 없으면 False

turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show() # 겹치면 평균의 차이가 없다는것이다











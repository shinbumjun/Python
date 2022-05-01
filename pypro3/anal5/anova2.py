# 분산분석
# 강남구에 있는 GS 편의점 3개지역 알바생의 급여에 대한 평균차이를 검정 

# 귀무 : GS 편의점 3개지역 알바생의 급여에 대한 평균차이가 없다
# 대립 : GS 편의점 3개지역 알바생의 급여에 대한 평균차이가 있다

import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt

# data = pd.read_csv("../testdata/group3.txt", header=None) # 헤더가 없는 데이터
# print(data) # <class 'pandas.DataFrmae'>
# print(data.describe()) # 종합

data = np.genfromtxt("../testdata/group3.txt", delimiter=",")
print(data[:3], type(data)) # <class 'numpy.ndarray'>로 읽기
# [[243.   1.]
#  [251.   1.]
#  [275.   1.]]
print(data.shape) # (22, 2)

# 세 개의 집단에 급여 평균 
gr1 = data[data[:, 1] == 1, 0]
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('평균') 
print(gr1, ' ', np.mean(gr1)) # 평균 316.625
print(gr2, ' ', np.mean(gr2)) # 평균 256.444
print(gr3, ' ', np.mean(gr3)) # 평균 278.0

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('정규성')
print(stats.shapiro(gr1).pvalue)
print(stats.shapiro(gr2).pvalue)
print(stats.shapiro(gr3).pvalue)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('등분산성')
print(stats.levene(gr1, gr2, gr3).pvalue) # 자주 사용하는것 모수 검정 방법 levene
print(stats.bartlett(gr1, gr2, gr3).pvalue) # 표본의 수가 적으므로 비모수 검정 방법 bartlett

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('데이터 분포 시각화')
# plt.boxplot([gr1, gr2, gr3])
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('일원분산분석 방법1 : anova_lm')
df = pd.DataFrame(data, columns = ['pay', 'group'])
print(df.head(2))

lmodel = ols('pay ~ C(group)', data = df).fit() # C(독립벼변수...) : 범주형임을 알림
print(anova_lm(lmodel, type = 1))
# PR(>F) 0.043589 < 0.05 이므로 귀무 기각. GS 편의점 3개지역 알바생의 급여에 대한 평균차이가 있다.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('일원분산분석 방법2 : anova_lm')
# 일원분산분석 방법2 : f_oneway, scipy가 제공
f_statistic, pvalue = stats.f_oneway(gr1, gr2, gr3)
print('f_statistic : ', f_statistic) # f_statistic :  3.7113359882669763
print('pvalue : ', pvalue) # pvalue :  0.043589334959178244

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('사후 검정')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_reult = pairwise_tukeyhsd(endog = df.pay, groups = df.group)
print(turkey_reult)
#  Multiple Comparison of Means - Tukey HSD, FWER=0.05  
# ======================================================
# group1 group2 meandiff p-adj    lower    upper  reject
# ------------------------------------------------------
#    1.0    2.0 -60.1806 0.0354 -116.6056 -3.7555   True
#    1.0    3.0  -38.625 0.3217 -104.8246 27.5746  False
#    2.0    3.0  21.5556 0.6706  -43.2141 86.3252  False

turkey_reult.plot_simultaneous(xlabel="mean", ylabel='group')
plt.show()









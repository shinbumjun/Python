'''
# 온도라는 요인 하나에 그룹 3개
'''
# data.go.kr 사이트에서 어느 음식점 매출데이터와 날씨 데이터를 이용하여 온도 높낮이에 따른 매출의 평균에 차이를 검정

# 온도가 더울 때의 매출액, 보통일 때, 낮을 때의 매출액

# 귀무 : 매출액은 온도에 영향이 없다.
# 대립 : 매출액은 온도에 영향이 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 자료 읽기1 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv",
                         dtype={'YMD':'object'}) # int를 오브젝으로 바꿈 (병합하기 위해서)

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
print(len(frame))
print(frame.columns)

data = frame.iloc[:, [0, 1, 7, 8]] # 'YMD', 'AMT', 'maxTa', 'sumRn'
print(data.head(3), len(data)) # 원하는 열만 가져오기, 328
print(data.isnull().sum()) # 결측치 없음

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('일변 최고온도를 구간 설정') 

print(data.maxTa.describe()) # 종합
import matplotlib.pyplot as plt
# plt.boxplot(data.maxTa)
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
data['ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 38], labels = [0, 1, 2]) # 오류 잡을 필요없음 : SettingWithCopyWarning: 
# 1구간(추움), 2구간(보통), 3구간(더움) - 2개씩 묶어서
print(data.head(3), ' ', data['ta_gubun'].unique())
#         YMD    AMT  maxTa  sumRn ta_gubun
# 0  20190514      0   26.9    0.0        2
# 1  20190519  18000   21.6   22.0        1
# 2  20190521  50000   23.8    0.0        1   [2, 1, 0]
# Categories (3, int64): [0 < 1 < 2]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('상관분석') 
print(data.corr())
#             AMT     maxTa     sumRn
# AMT    1.000000 -0.660066 -0.080907
# maxTa -0.660066  1.000000  0.119268 -> 음의상관 관계
# sumRn -0.080907  0.119268  1.000000 -> 음의상관 관계

x1 = np.array(data[data.ta_gubun == 0].AMT)
x2 = np.array(data[data.ta_gubun == 1].AMT)
x3 = np.array(data[data.ta_gubun == 2].AMT)
print(x1[:3]) # 추울때 매출액
# [1050500  770000 1054500]
print(x2[:3]) # 더울때 매출액
# [ 18000  50000 274000]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('등분산성')
print(stats.levene(x1, x2, x3)) # pvalue=0.03900 < 0.05 (등분산성 만족x)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('정규성')
print(stats.ks_2samp(x1, x2).pvalue) # 만족 x
print(stats.ks_2samp(x1, x3).pvalue) # 만족 x
print(stats.ks_2samp(x2, x3).pvalue) # 만족 x

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('세 그룹의 매출액 평균')
spp = data.loc[:, ['AMT', 'ta_gubun']]
print(spp.groupby('ta_gubun').mean())
#                    AMT
# ta_gubun              
# 0         1.032362e+06 -> 추울때 더 잘 팔림
# 1         8.181069e+05
# 2         5.537109e+05

print(pd.pivot_table(spp, index = ['ta_gubun'], aggfunc='mean'))
#                    AMT
# ta_gubun              
# 0         1.032362e+06
# 1         8.181069e+05
# 2         5.537109e+05

print(spp[:3])
#      AMT ta_gubun
# 0      0        2
# 1  18000        1
# 2  50000        1

sp = np.array(spp)
group1 = sp[sp[:, 1] == 0, 0]
group2 = sp[sp[:, 1] == 1, 0]
group3 = sp[sp[:, 1] == 2, 0]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('매출액 시각화')
plt.boxplot([group1, group2, group3])
plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('일원분산분석')
print(stats.f_oneway(group1, group2, group3))
# F_onewayResult(statistic=99.1908012029983, pvalue=2.360737101089604e-34)
# pvalue=2.360737101089604e-34 < 0.05 이므로 귀무가설 기각. 매출액은 온도에 영향이 있다.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('정규성 만족 x') 
print(stats.kruskal(group1, group2, group3)) # kruskal-Wallis test
# pvalue=2.360737101089604e-34 < 0.05 이므로 귀무가설 기각. 매출액은 온도에 영향이 있다.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('Anaconda Prompt -> pip install pingouin')
print('등분산성 만족 x')
from pingouin import welch_anova
print(welch_anova(data = data, dv='AMT', between='ta_gubun'))
# pvalue = 7.907874e-35 < 0.05 이므로 귀무가설 기각. 매출액은 온도에 영향이 있다

# 해석 : 날씨(온도 : 더움, 보통, 추움)에 의해 매출액의 차이가 있다.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('사후 검정')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_reult = pairwise_tukeyhsd(endog = spp['AMT'], groups = spp['ta_gubun'], alpha=0.05)
print(turkey_reult)
#        Multiple Comparison of Means - Tukey HSD, FWER=0.05       
# =================================================================
# group1 group2   meandiff   p-adj    lower        upper     reject
# -----------------------------------------------------------------
#      0      1 -214255.4486   0.0  -296755.647 -131755.2503   True
#      0      2 -478651.3813  -0.0 -561484.4539 -395818.3088   True
#      1      2 -264395.9327  -0.0 -333326.1167 -195465.7488   True

turkey_reult.plot_simultaneous(xlabel="mean", ylabel='group')
plt.show()












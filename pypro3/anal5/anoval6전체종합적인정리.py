'''
# jikwon 테이블의 자료로 chi2, t-test, ANOVA 정리
'''
import MySQLdb
import pickle
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from numba.core.typing.context import Rating

try: # DB읽기
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('읽기 오류 : ', e)

conn = MySQLdb.connect(**config)
cursor = conn.cursor()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('교차분석(이원카이제곱검정 : 각 부서 : 범주형(독립)와 직원평가점수 : 범주형(종속) 간의 관련성 분석')

# 귀무 : 각 부서와 직원평가점수 간에 관련이 없다.
# 대립 : 각 부서와 직원평가점수 간에 관련이 있다.

df = pd.read_sql("select * from jikwon", conn)
print(df.head(3))
#    jikwon_no jikwon_name  buser_num  ... jikwon_ibsail  jikwon_gen jikwon_rating
# 0          1         홍길동         10  ...    2008-09-01           남             a
# 1          2         한송이         20  ...    2010-01-03           여             b
# 2          3         이순신         20  ...    2010-03-03           남             b

buser = df['buser_num'] # 부서
rating = df['jikwon_rating'] # 점수

# 가설검증 정설을 무로 돌리고 새로운 의견을 반영

ctab = pd.crosstab(buser, rating) # 교차표
print(ctab)

chi, p, df, exp = stats.chi2_contingency(ctab)
print('chi:{}, p:{}, df:{}'.format(chi, p, df)) # 
# chi:7.339285714285714, p:0.2906064076671985, df:6
# p:0.290606 > 0.05 이므로 귀무가설 채택. 대립은 받아들일 수 없다. 
# 귀무 : 각 부서와 직원평가점수 간에 관련이 없다.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('차이분석(t-검정 : 10, 20번 부서(범주형:독립)와 평균 연봉(연속형:종속) 간의 차이 분석')

# 귀무(영가설, H0) : 두 부서 간 연봉평균은 차이가 없다.
# 대립(연구, H1) : 두 부서 간 연봉평균은 차이가 있다.

df_10 = pd.read_sql("select buser_num, jikwon_pay from jikwon where buser_num=10", conn)
df_20 = pd.read_sql("select buser_num, jikwon_pay from jikwon where buser_num=20", conn)
buser10 = df_10['jikwon_pay']
buser20 = df_20['jikwon_pay']

print('평균 : ', np.mean(buser10), ' ', np.mean(buser20))
# 평균 :  5414.285714285715   4908.333333333333

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
t_result = stats.ttest_ind(buser10, buser20)
print(t_result)
# Ttest_indResult(statistic=0.4585177708256519, pvalue=0.6523879191675446)
# 해석 : pvalue=0.652 > 0.05 귀무가설 채택. 두 부서 간 연봉평균은 차이가 없다.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('분산분석(ANOVA : 각 부서(요인 1개:부서, 4그룹이 존재):범주형(독립)와 평균 연봉(연속형:종속) 간의 차이 분석')
df3 = pd.read_sql("select buser_num, jikwon_pay from jikwon", conn)
buser = df3['buser_num']
pay = df3['jikwon_pay']

gr1 = df3[df3['buser_num'] == 10]['jikwon_pay']
gr2 = df3[df3['buser_num'] == 20]['jikwon_pay']
gr3 = df3[df3['buser_num'] == 30]['jikwon_pay']
gr4 = df3[df3['buser_num'] == 40]['jikwon_pay']
print(gr1.head(3))
# 0     9900
# 9     3700
# 12    4900

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
import matplotlib.pyplot as plt
# plt.boxplot([gr1, gr2, gr3, gr4])
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('방법1번')
f_sta, pv = stats.f_oneway(gr1, gr2, gr3, gr4)
print('f value(검정 통계량) : ', f_sta) # 0.41244 > 0.05 이므로 귀무 채택
print('p value : ', pv) # 0.74544 > 0.05 이므로 귀무 채택

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('사후검정(귀무 채택이기 때문에 의미는 없지만 해보기)')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(df3.jikwon_pay, df3.buser_num, alpha = 0.05)
print(tukey)
#    Multiple Comparison of Means - Tukey HSD, FWER=0.05    
# ==========================================================
# group1 group2  meandiff p-adj    lower      upper   reject
# ----------------------------------------------------------
#     10     20 -505.9524 0.9588 -3292.2114 2280.3066  False
#     10     30  -85.7143 0.9998  -3217.199 3045.7705  False
#     10     40  848.2143 0.9202 -2823.7771 4520.2056  False
#     20     30  420.2381 0.9756 -2366.0209 3206.4971  False
#     20     40 1354.1667 0.6937 -2028.2234 4736.5568  False
#     30     40  933.9286  0.897 -2738.0628 4605.9199  False

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
tukey.plot_simultaneous()
plt.show() # 다겹친거 확인

















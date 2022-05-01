print('*****두 집단 이하의 평균 또는 비율 차이 검정')

'''
t분포는 표본평균을 이용해 정규분포의 평균을 해석할 때 사용한다.
독립변수 : 범주형
종속변수 : 연속형

단일 모집단의 평균에 대한 가설검정(one samples t-test)
하나의 집단에 대한 표본평균이 예측된 평균(모집단의 평균)과 같은지를 검정.

단일 모집단의 평균에 대한 가설검정(one samples t-test)
예제 1,2,3

1. 정규성, 귀무채택 or 귀무기각, 그래프 확인

[참고]
py가설검정.pdf 
'''
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('연습1) 어느 남성 집단의 평균 키는 177이다. 남성 집단의 표본 데이터를 추출해 평균차이 검정')
# 귀무 : 남성 집단의 평균 키는 177이다.
# 대립 : 남성 집단의 평균 키는 177이 아니다. (양측검정) 
# 대립 : 남성 집단의 평균 키는 177 보다 크다 (작다). (단측검정)

one_sample = [167.0, 182.7, 169.6, 176.8, 185.0]
print(np.array(one_sample).mean()) # 샘플데이터 176.21999 vs 177 평균에 차이가 있는가?
# 데이터의 정규성 확인
print(stats.shapiro(one_sample))
# pvalue=0.540051 > 0.05 이므로 정규성 만족

# 검정 수행
result = stats.ttest_1samp(one_sample, popmean = 177)
print('t값:%.3f, v-value:%.3f'%result) # t값:-0.221, v-value:0.836 (소수3 자리까지만)
# 해석 : p-value:0.836 > 0.05 이므로 귀무가설 채택.

print()
result2 = stats.ttest_1samp(one_sample, popmean=165) # 모집단의 평균 키가 165
print('t값:%.3f, p-value:%.3f'%result2)
# 해석 : p-value:0.033 < 0.05 이므로 귀무가설 기각.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('실습 예정 2) A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정)')
print('A중학교 1학년 1반 학생들의 시험결과는 늘 80이라고 알려져 있다.')

# 귀무 : A중학교 1학년 1반 학생들의 국어 시험결과 평균은 80이다.
# 대립 : A중학교 1학년 1반 학생들의 국어 시험결과 평균은 80이 아니다.

data = pd.read_csv("../testdata/student.csv")
print(data.head(3))
#     이름  국어 영어 수학
# 0  박치기  90  85  55
# 1  홍길동  70  65  80
# 2  김치국  92  95  76

print(data['국어'].mean()) # 72.9 vs 80 차이가 있느냐?
print(data.describe()) # 종합

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정규성 (확인하는 이유 : 중앙 집중 그래프인지?)ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(stats.shapiro(data.국어)) # pvalue=0.012959 < 0.05 정규성 만족x

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 귀무채택 or 귀무기각 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(stats.ttest_1samp(data.국어, popmean = 80))
# pvalue=0.1985605 > 0.05 이므로 귀무 채택, 수집된 데이터는 우연히 발생된 자료이다.
print(stats.ttest_1samp(data.국어, popmean = 60))
# pvalue=0.0256878 < 0.05 이므로 귀무 기각

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('실습 예제 3) 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv')
print('여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.')
print('표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.')

# 귀무 : 여아 신생아 몸무게의 평균은 2800(g)이다.
# 대립 : 여아 신생아 몸무게의 평균은 2800(g) 보다 크다.

data = pd.read_csv("../testdata/babyboom.csv")
print(data.head(3)) # gender:1 여아, gender:2 남아
#    time  gender  weight  minutes
# 0     5       1    3837        5
# 1   104       1    3334       64
# 2   118       2    3554       78

fdata = data[data.gender == 1]
print(fdata.head(3), len(fdata))
print(np.mean(fdata.weight)) # 3132 vs 2800(귀무) 차이?

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정규성 확인 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(stats.shapiro(fdata.iloc[:,2])) # pvalue=0.017984 < 0.05 정규성 만족x
# print(stats.shapiro(fdata.weight))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 시각화(그래프 보기1) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
sns.displot(fdata.iloc[:, 2], kde = True)
plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 시각화(그래프 보기2) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
stats.probplot(fdata.iloc[:, 2], plot = plt) # Q-Q plot
plt.show() # 커브를 그리는 모양은 정규성에 적합하지 않는다

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 귀무채택 or 귀무기각 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(stats.ttest_1samp(fdata.weight, popmean = 2800))
# pvalue=0.0392 < 0.05 이므로 귀무가설을 기각하고 대립가설을 채택








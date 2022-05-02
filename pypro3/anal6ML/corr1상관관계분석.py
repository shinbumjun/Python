'''
상관관계 분석
두 개 이상의 확률변수(연속형) 간에 어떤 관계가 있는지 분석하는 것
공분산을 표준화 한 것을 상관계수(r)라고 한다.

공분산 : 선형 관계(변수2개 x,y그래프)
상관계수 : 공분산을 표준화한 것 (대표적으로 피어슨의 상관계수)
'''
import pandas as pd # 판다스
import numpy as np # 넘파이
import matplotlib.pyplot as plt # 시각화

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('한글 깨짐방지')
plt.rc('font', family= 'malgun gothic')

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('DataFrame 타입으로')
df= pd.DataFrame({'id1':(1,2,3,4,5), 'id2':(2,3,-1,7,9)})
print(df)
print(df.cov()) # 공분산 : 음의상관 관계 (고정)
print(df.corr()) # 상관계수 : 음의상관 관계 

# plt.scatter(df.id1,df.id2) # 시각화
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('파일 자료를 읽어 상관분석')
data = pd.read_csv("../testdata/drinking_water.csv") # 자료 읽기
print(data.head(3), len(data)) # 264행
#    친밀도  적절성  만족도
# 0    3    4    3
# 1    3    3    2
# 2    4    4    4 

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('데이터 살펴보기')
print(data.info())
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('데이터 요약')
print(data.describe()) 

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('공분산')
print(np.cov(data.친밀도, data.적절성))
print(np.cov(data.친밀도, data.만족도))

print(data.cov()) # 공분산 : 양의상관 관계

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('상관계수(공분산 표준화)')
print(np.corrcoef(data.친밀도, data.적절성))
print(np.corrcoef(data.친밀도, data.만족도))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('선형회귀하기 위해서 (피어슨 상관계수)')
print(data.corr()) # 상관계수
print(data.corr(method='pearson')) # ***피어슨 상관계수 : 정규성, 연속형(등간, 비율 척도)
# print(data.corr(method='spearman')) # 서열척도, 비선형
# print(data.corr(method='kendall')) # 서열척도, 비선형

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('만족도만 보기(특정)')
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False)) # ascending : 데이터 정렬하기

# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print('시각화')
# data.plot(kind='scatter', x='만족도', y='적절성')
# plt.show()
#
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print('산점도 행렬보기')
# from pandas.plotting import scatter_matrix 
# attr = ['친밀도','적절성','만족도']
# scatter_matrix(data[attr])
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('hitmap : 흐릴수록 상관관계가 강한것')
import seaborn as sns
# sns.heatmap(data.corr())
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('heatmap에 텍스트 표시 추가사항 적용해 보기 (경고는 신경x)')
# https://github.com/pykwon/python/blob/master/hitmap%EC%B6%94%EA%B0%80.txt
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()














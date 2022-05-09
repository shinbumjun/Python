'''
# Advertising.csv : 여러 매체를 통한 광고비 사용에 따른 판매량 추정치 얻기 
'''
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
plt.rc('font', family = 'malgun gothic')

advdf = pd.read_csv("../testdata/Advertising.csv", usecols=[1,2,3,4])
print(advdf.head(3), advdf.shape) # (200, 4)
#       tv  radio  newspaper  sales
# 0  230.1   37.8       69.2   22.1
# 1   44.5   39.3       45.1   10.4
# 2   17.2   45.9       69.3    9.3

print('상관계수(r) :\n', advdf.loc[:,['sales', 'tv']].corr()) # 0.782
print('상관계수(r) :\n', advdf.loc[:,['sales', 'newspaper']].corr()) # 0.228
print('상관계수(r) :\n', advdf.loc[:,['sales', 'radio']].corr()) # 0.576

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('단순 선형회귀 (tv)')
lm = smf.ols(formula = 'sales ~ tv', data = advdf).fit()
print(lm.summary()) # 설명력 0.610
print('설명력 : ', lm.rsquared)
print('p값 : ', lm.pvalues[1])

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print('시각화')
# plt.scatter(advdf.tv, advdf.sales)
# plt.xlabel('tv')
# plt.ylabel('sales')
# x = pd.DataFrame({'tv':[advdf.tv.min(), advdf.tv.max()]})
# y_pred = lm.predict(x)
# plt.plot(x, y_pred, c = 'red')
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('미지의 tv 광고비에 따른 상품 판매량 추정')
x_new = pd.DataFrame({'tv':[220.12, 55.66, 10]})
pred_new = lm.predict(x_new)
print('상품 판매량 추정치 : ', pred_new.values)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(advdf.corr()) # sales와의 상관관계 : tv > radio > newspaper
lm_mul = smf.ols(formula = 'sales ~ tv + radio + newspaper', data = advdf).fit()
print(lm_mul.summary()) # Adj. R-squared:0.896, p-value:1.58e-96 < 0.05 유의한 모델
# newspaper p-value:0.860 > 0.05이므로 독립변수에서 제거를 고려

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('newspapers는 모델의 성능에 영향을 주지 못하는 변수')
lm_mul = smf.ols(formula = 'sales ~ tv + radio', data = advdf).fit()
print(lm_mul.summary()) # Adj. R-squared:0.896, p-value:1.58e-96 < 0.05 유의한 모델

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('새로운 독립변수 값으로 종속변수 sales를 예측해서 추정치를 얻기')
x_new2 = pd.DataFrame({'tv':[200.12, 55.66, 10], 'radio':[30.3, 40.4, 50.5]})
pred_new2 = lm.predict(x_new2)
print('상품 판매량 추정치2 : ', pred_new2.values)
# 상품 판매량 추정치2 :  [16.54562603  9.67848296  7.50795995]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('*****선형회귀분석의 기존 가정 충족 조건*****')
# 선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다.
# 정규성 : 잔차항이 정규분포를 따라야 한다.
# 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
# 등분산성 : 그룹간의 분산이 유사해야 한다. 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.
# 다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('잔차항 구하기 (실제값  - 예측값 )')
fitted = lm_mul.predict(advdf.iloc[:, 0:2]) # tv radio
# print(fitted) # 예측값
residual = advdf['sales'] - fitted
print(np.mean(residual)) # 5.511147094239277e-15 0에 근사

import seaborn as sns
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('선형성 : 예측값과 잔차의 분포가 유사')
sns.regplot(fitted, residual, lowess = True, line_kws = {'color':'red'}) # 선형회귀모델의 적합성을 그릴때 사용
plt.plot([fitted.min(), fitted.max()], [0,0], color='gray')
plt.show()
# 선형성을 만족하지 못함 : 다항회귀(비선형) 모델을 추천 - ploynomialFeatures


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('정규성 : 잔차가 정규분포를 따르는지 확인 Q-Q plot')
import scipy.stats

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('정규성을 만족하지 않음 : 데이터에 대해 표준화, 정규화, log를 씌우는 작업을 시도')
sr =scipy.stats.zscore(residual)
(x, y), _ = scipy.stats.probplot(sr)
sns.scatterplot(x, y)
plt.plot([-3, 3], [-3, 3], '--', color ='gray')
plt.show()

print('shapiro test : ', scipy.stats.shapiro(residual))
# ShapiroResult(statistic=0.9180378317832947, pvalue=4.190036317908152e-09)
# pvalue=4.190036317908152e-09 < 0.05이므로 정규성을 만족하지 않음

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('독립성 : 잔차가 자기상관을 따르는지 확인 Durbin-Watson 0 ~ 4----')
# Durbin-Watson:2.081 : 독립성은 만족(2에 근사하면 만족)

print('\n등분산성 : 잔차의 분산이 일정해야함')
sr = scipy.stats.zscore(residual)
sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess =True, line_kws = {'color':'red'})
plt.show()
# 등분산성 만족 못함 : 비선형인지 확인, 이상값 확인, 정규성 확인
# 정규성은 만족하나 등분산성은 만족하지 못한 경우 가중회귀(weighted regression)분석

print('\n다중공선성 : 독립변수들 간에 강한 상관관계 확인')
from statsmodels.stats.outliers_influence import variance_inflation_factor
# VIF(Variable Inflatin Factors : 분산 팽창 계수) 값 확인 : 10을 넘으면 다중공산성을 의심
print(variance_inflation_factor(advdf.values, 1)) # tv
print(variance_inflation_factor(advdf.values, 2)) # radio
# 12.570312383503682
# 3.1534983754953845

vifdf = pd.DataFrame() # DataFrame으로 확인하기
vifdf['vif_value'] = [variance_inflation_factor(advdf.values, i) for i in range(1, 3)]
print(vifdf)
#    vif_value
# 0  12.570312
# 1   3.153498

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print("참고 : 극단치(이상치) 확인 - Cook's distance")
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm_mul).cooks_distance # 극단값을 나타내는 지표 반환 
print(cd.sort_values(ascending=False).head())
# 130    0.258065
# 5      0.123721
# 35     0.063065
# 178    0.061401
# 126    0.048958
# dtype: float64

import statsmodels.api as sm
sm.graphics.influence_plot(lm_mul, criterion = 'cooks')
plt.show()

print(advdf.iloc[[130, 5, 35, 178, 126]])
#         tv  radio  newspaper  sales
# 130    0.7   39.6        8.7    1.6
# 5      8.7   48.9       75.0    7.2
# 35   290.7    4.1        8.5   12.8
# 178  276.7    2.3       23.7   11.8
# 126    7.8   38.9       50.6    6.6













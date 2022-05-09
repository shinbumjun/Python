'''
# *선형회귀 : mtcar dataset (단순 선형회귀, 다중 선형회귀 - 예측, 추정치구하기)
'''
import statsmodels.api
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('한글 깨짐방지')
plt.rc('font', family= 'malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)
print(mtcars.columns)
print(mtcars.describe())

print(mtcars.corr())
print(np.corrcoef(mtcars.hp, mtcars.mpg)) # -0.77616837
print(np.corrcoef(mtcars.wt, mtcars.mpg)) # -0.86765938

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel('마력수')
# plt.ylabel('연비')
# slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1)
# plt.plot(mtcars.hp, mtcars.hp * slope + intercept, 'r')
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('단순 선형회귀 - ols')
result = smf.ols('mpg ~ hp', data = mtcars).fit()
# print(result.summary())
print(result.summary().tables[1]) # 기울기랑 절편만 확인

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('예측 : 음의 상관관계!')
print('마력수 110에 대한 연비 예측 : ', -0.0682  * 110 + 30.0989) # 22.5969
print('마력수 50에 대한 연비 예측 : ', -0.0682  * 50 + 30.0989) # 26.6889

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('다중 선형회귀')
result2 = smf.ols('mpg ~ hp + wt', data = mtcars).fit() # hp와 wt는 독립변수로써 문제가 없다
print(result2.summary())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('**예측')
print('마력수 110 + 차체 무게 5에 대한 연비 예측 : ', (-0.0318 * 110) + (-3.8778 * 5) + 37.2273) # 14.3403

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('추정치 구하기 : predict')
result3 = smf.ols('mpg ~ wt', data = mtcars).fit()
print('결정계수 : ', result3.rsquared) # 0.7528
print('pvalue : ', result3.pvalues[1]) # 1.2939587013504974e-10
pred = result3.predict() # 학습 데이터로 예측
print(pred)

print(mtcars.mpg[0]) # 21.0
print(pred[0]) # 23.282610646808628

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('DataFrame에 실제값과 예측값 기억')
data = {
    'mpg':mtcars.mpg,
    'mpg_pred':pred
    
}

df = pd.DataFrame(data)
print(df)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('새로운 차체무게로 연비 예측')
print('차체 무게 여러개')
new_wt = pd.DataFrame({'wt':[6, 3, 1]})
new_pred2 = result3.predict(new_wt)
print('예상 연비 : \n', new_pred2)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
from pandas import DataFrame


mtcars_wt = float(input('차체무게 : '))
new_pred = result3.predict(pd.DataFrame(mtcars_wt))
print('차체 무게:{}일 때 예상연비는 {}'.format(mtcars_wt[0], new_pred[0]))











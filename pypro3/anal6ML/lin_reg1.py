'''
회귀분석방법 확인 : 맛보기 3가지 (make_regression, LinearRegression, ols) 선형회귀 모델

잔차 제곱합이 최소가 되는 추세선을 만들고 이를 통해 독립변수(feature)가 종속변수(label, class)에 얼마나 
영향을 주는지 인과관계를 분석
두 개 이상의 변수는 상관관계가 있어야 하고, 나아가서는 인과관계가 있어야 한다.
정량적인 모델을 생성

https://cafe.daum.net/flowlife/SBU0/51
'''
import statsmodels.api as sm
from sklearn.datasets import make_regression # 매트릭스
import numpy as np

np.random.seed(12)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('모델 맛보기1 : make_regression을 사용. model 생성 x')
x, y, coef = make_regression(n_samples = 50, n_features = 1, bias = 100, coef = True)
print(x)
print(y)
print(coef) # 기울기 : 89.47430739278907(동적), 절편 : 100     y = wx + b
print('예측값 : ', coef * -1.70073563 + 100)
print('실제값 : ', -52.17214291)

print('예측값 : ', coef * -0.67794537 + 100)
print('실제값 : ', 39.34130801)

# 참고 : 머신러닝은 귀납적 추론방식을 따른다.

xx = x
yy = y

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('모델 맛보기2 : LinearRegression을 사용. model 생성 o')
from sklearn.linear_model import LinearRegression
model = LinearRegression()
fit_model = model.fit(xx, yy) # 학습데이터로 모형 추정(training) : 절편, 기울기 얻음
print('slope : ', fit_model.coef_) # 89.47430739
print('bias : ', fit_model.intercept_) # 100.0   y = 89.47430739 * x + 100.0
print('모델이 예측한 값(수식) : ', 89.47430739 * -1.70073563 + 100.0)
y_new = fit_model.predict(xx[[0]])
print('모델이 예측한 값(method) : ', y_new[0])

print('미지의 x에 대한 새로운 예측값 : ', fit_model.predict([[66]]))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('모델 맛보기3 : ols를 사용. model 생성 o')
import statsmodels.formula.api as smf
import pandas as pd
x1 = xx.flatten() # 차원 축소(메트릭스를 
y1 = yy

print(x1.shape, ' ', y.shape) # (50,)   (50,)

data = np.array([x1, y1])
df = pd.DataFrame(data.T)
print(df.head(3))
#           0           1
# 0 -1.700736  -52.172143
# 1 -0.677945   39.341308
# 2  0.318665  128.512356

model2 = smf.ols(formula = 'y1 ~ x1', data = df).fit()
print(model2.summary())
# Intercept : 100.0000, slope : 89.4743

# 예측값 확인 함수
print('모델이 예측한 값(method) : ', y_new[0])
print(x1[:2]) # [-1.70073563 -0.67794537]

new_df = pd.DataFrame({'x1':[-1.70073563, -0.67794537]}) # 기존자료로 예측값 확인
new_pred = model2.predict(new_df)
print('모델이 예측한 값(method) : \n', new_pred)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('전혀 새로운 독립변수에 대한 예측 결과 보기')
new2_df = pd.DataFrame({'x1':[7, -2.345]}) # 새로운 자료로 예측값 확인
new2_pred = model2.predict(new2_df)
print('모델이 예측한 값(method) : \n', new2_pred)
















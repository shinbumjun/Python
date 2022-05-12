'''
sklearn 모듈의 분류 모델의 상당수는 출력결과가 연속형인 예측 처리도 가능 

데이터에 따라 최적의 모델은 분석가가 찾는것
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor # 랜덤포레스트
from sklearn.datasets import load_boston # 분류결과
from sklearn.metrics import r2_score # 투표

boston = load_boston()

dfx = pd.DataFrame(boston.data, columns = boston.feature_names)
dfy = pd.DataFrame(boston.target, columns = ['MEDV'])
df = pd.concat([dfx, dfy], axis = 1)
print(df.head(3), df.shape) # (506, 14)

print(df.corr()) # 상관관계 분석

cols = ['MEDV', 'RM', 'LSTAT']
# sns.pairplot(df[cols])
# plt.show()

x = df[['LSTAT']] # 2차원
y = df['MEDV'] # 1차원

import numpy as np
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('실습 1: DecisionTreeRegressor') # 나무
model = DecisionTreeRegressor(criterion = 'mse').fit(x, y)
print('predict : ', model.predict(x)[:5])
print('real : ', np.array(y[:5]))
print('결정계수(R2) : ', r2_score(y, model.predict(x)))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('실습 2: RandomForestRegressor') # 숲
model2 = RandomForestRegressor(n_estimators = 1000, criterion = 'mse', random_state = 123).fit(x, y)
print('predict : ', model2.predict(x)[:5])
print('real : ', np.array(y[:5]))
print('결정계수(R2) : ', r2_score(y, model2.predict(x)))
















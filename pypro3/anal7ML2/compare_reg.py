'''
sklearn이 지원하는 예측모델 (연속형)
'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor 
from sklearn.metrics import r2_score

adver = pd.read_csv("../testdata/Advertising.csv", usecols=[1,2,3,4]) # 원하는 칼럼만
print(adver.head(2))
#       tv  radio  newspaper  sales
# 0  230.1   37.8       69.2   22.1
# 1   44.5   39.3       45.1   10.4

x = np.array(adver.loc[:, 'tv':'newspaper'])
print(x[:2]) # 매트릭스
# [[230.1  37.8  69.2]
#  [ 44.5  39.3  45.1]]

y = np.array(adver.sales)
print(y[:2])
# [22.1 10.4]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('LinearRegression으로')
lmodel = LinearRegression().fit(x, y)
lpred = lmodel.predict(x)
print('LinearRegression pred : ', lpred[:5])
print('r2_score : ', r2_score(y, lpred)) # 설명력 : 0.897

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('KNeighborsRegressor으로')
kmodel = KNeighborsRegressor(n_neighbors = 3).fit(x, y)
kpred = lmodel.predict(x)
print('KNeighborsRegressor pred : ', kpred[:5])
print('r2_score : ', r2_score(y, kpred)) # 설명력 : 0.968

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('RandomForestRegressor으로')
rmodel = RandomForestRegressor(n_estimators = 100, criterion='mse').fit(x, y)
rpred = rmodel.predict(x)
print('RandomForestRegressor으로 pred : ', rpred[:5])
print('r2_score : ', r2_score(y, rpred)) # 설명력 : 0.997

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('XGBRegressor으로')
xmodel = XGBRegressor(n_estimators = 100, criterion='mse').fit(x, y)
xpred = xmodel.predict(x)
print('XGBRegressor으로 pred : ', xpred[:5])
print('r2_score : ', r2_score(y, xpred)) # 설명력 : 0.999







'''
나이브베이즈 모델 : 베이지 정리를 이용
'''
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

x = np.array([1,2,3,4,5])
x = x[:, np.newaxis] # 메트릭스
print(x)
y = np.array([1,3,5,7,9])

model = GaussianNB().fit(x, y)
print(model)
pred = model.predict(x)
print(pred)
print('acc : ', metrics.accuracy_score(y, pred)) # 실제값과 예측값

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('새로운 값으로 분류')
new_x = np.array([[0.5],[2],[7],[12],[0.1]])
new_pred = model.predict(new_x)
print('new_pred : ', new_pred)
# [1 3 9 9 1]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('-one-hot encoding')
print('1. np.eye()')
x = '1,2,3,4,5'
x = x.split(',')
x = np.eye(len(x))
print(x)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('2. OnewHotEncoder 사용') # 이것을 많이 사용
x= '1,2,3,4,5'
x = x.split(',')
x = np.array(x)
x = x[:, np.newaxis]
one_hot = OneHotEncoder(categories = 'auto')
x2 = one_hot.fit_transform(x).toarray()
print(x2)
y = np.array([1,3,5,7,9])

model2 = GaussianNB().fit(x2, y)
print(model2)
pred2 = model2.predict(x2)
print(pred2)

# 아직까지는 랜덤포레스트, 부스트가 중요















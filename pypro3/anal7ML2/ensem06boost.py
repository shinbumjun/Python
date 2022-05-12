'''
XGBoost는 Gradient Boosting 알고리즘을 분산 환경에서도 실행할 수 있도록 구현해 놓은 라이브러로 
Regression, Classification 문제를 모두 지원하며, 성능과 자원 효율이 좋아서 인기 있는 알고리즘이다.
RandomForest와 마찬가지로 XGBoost는 여러 개의 Decision Tree를 조합해서 사용하는 Ensemble 알고리즘이다.

[설치]
pip install xgboost
pip install lightgbm

brest_cancer dataset 사용
'''
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

import xgboost as xgb

from xgboost import plot_importance
from lightgbm import LGBMClassifier
import matplotlib.pyplot as plt

dataset = load_breast_cancer()
x_feature = dataset.data
y_label = dataset.target

# print(dataset.feature_names)

cancer_df = pd.DataFrame(data = x_feature, columns = dataset.feature_names)
pd.set_option('max_columns', None)
print(cancer_df.head(2), cancer_df.shape) # (569, 30)
print(dataset.target_names) # ['malignant' 'benign']
print(np.sum(y_label == 0)) # malignant : 212 (양성)
print(np.sum(y_label == 1)) # benign : 357 (악성)

x_train, x_test, y_train, y_test = train_test_split(x_feature, y_label, test_size = 0.2, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = xgb.XGBClassifier(booster='gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train) # 선형일 경우
# model = LGBMClassifier(booster='gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train) # 데이터 많을때 사용(성능 좋음, 시각화는 안됨)
print(model)

pred = model.predict(x_test)
print('예측값 : ', pred[:10]) # [0 1 1 1 1 1 1 1 1 0]
print('실제값 : ', y_test[:10]) # [0 1 1 1 1 1 0 1 1 0]

from sklearn import metrics
print('분류 정확도 : ', metrics.accuracy_score(y_test, pred)) # 0.947
print('분류 보고서 : ', metrics.classification_report(y_test, pred))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
fig, ax = plt.subplots(figsize = (10, 12))
plot_importance(model, ax = ax)
plt.show()



























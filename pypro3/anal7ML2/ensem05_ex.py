'''
[Randomforest 문제1] 
kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)

dataset은 winequality-red.csv 

https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv

Input variables (based on physicochemical tests):
 1 - fixed acidity
 2 - volatile acidity
 3 - citric acid
 4 - residual sugar
 5 - chlorides
 6 - free sulfur dioxide
 7 - total sulfur dioxide
 8 - density
 9 - pH
 10 - sulphates
 11 - alcohol
 Output variable (based on sensory data):
 12 - quality (score between 0 and 10)
 
[참고]
https://cafe.daum.net/flowlife/SBU0/44
'''
# [Randomforest 문제1]
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# dataset은 winequality-red.csv
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import model_selection

df = pd.read_csv("../testdata/winequality-red.csv")
print(df.head(3), df.shape)
print(df.isnull().any())

df_x = df.drop(['quality'], axis=1) # 독립변수로 사용. quality를 제외한 나머지 칼람
df_y = df['quality'] # 종속변수로 사용

print(df_y.unique()) # [5 6 7 4 8 3]
print(df_x.columns) # ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', ...

train_x, test_x, train_y, test_y = train_test_split(df_x, df_y)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

model = RandomForestClassifier(criterion='entropy', n_estimators=500)
model.fit(train_x, train_y)
pred = model.predict(test_x)

from sklearn.metrics import accuracy_score
print('acc: ', accuracy_score(test_y, pred)) # acc: 0.7075

# 독립변수 중 중요 변수 확인
print()
import matplotlib.pyplot as plt
import numpy as np

print('특성(변수) 중요도: {}'.format(model.feature_importances_))

def plot_importance_func(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel("attr importance")
    plt.ylabel("attr")
    plt.show()

plot_importance_func(model)


'''
[Randomforest 문제2]
중환자 치료실에 입원 치료 받은 환자 200명의 생사 여부에 관련된 자료다.
종속변수 STA(환자 생사 여부)에 영향을 주는 주요 변수들을 이용해 검정 후에 해석하시오. 
모델 생성 후 입력자료 및 출력결과는 Django를 사용하시오.

예제 파일 : https://github.com/pykwon  ==>  patient.csv

<변수설명>
  STA : 환자 생사 여부 (0:생존, 1:사망)
  AGE : 나이
  SEX : 성별
  RACE : 인종
  SER : 중환자 치료실에서 받은 치료
  CAN : 암 존재 여부
  INF : 중환자 치료실에서의 감염 여부
  CPR : 중환자 치료실 도착 전 CPR여부
  HRA : 중환자 치료실에서의 심박수
참고 : 중요 변수 알아보기

print('특성(변수) 중요도 :\n{}'.format(model.feature_importances_))
def plot_feature_importances(model):   # 특성 중요도 시각화
    n_features = x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), x.columns)
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1, n_features)
    plt.show()
    plt.close()

plot_feature_importances(model)
'''
'''
[Randomforest 문제2]
중환자 치료실에 입원 치료받은 환자 200명의 생사여부에 관련된 자료다.
종속변수 STA에 영향을 주는 변수들을 찾아내어 검정 후에 해석하시오.
예제 파일 : https://github.com/pykwon ==> patient.csv

<변수설명>
STA : 환자생사여부
AGE : 나이
SEX : 성별
RACE : 인종
SER : 중환자 치료실에서 받은 치료
CAN : 암 존재 여부
INF : 중환자 치료실에서의 감염 여부
CPR : 중환자 치료실 도착전 CPR여부
HRA : 중환자 치료실에서의 심박수
'''
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pt_data = pd.read_csv('../testdata/patient.csv')
print(pt_data.head(2))

# 결측치
# print(pt_data.isnull().any()) # 결측치 하나도 없음

# 독립변수 / 종속변수 설정
x = pt_data.iloc[:, 2:] # 독립변수 STA를 제외한 나머지
print(x[:2])
y = pt_data['STA']
print(y[:2])

# train / test
train_x, test_x, train_y, test_y = train_test_split(x,y)

# 모델 생성
model = RandomForestClassifier(criterion='entropy', n_estimators=500, random_state=0)
model.fit(train_x, train_y)
pred = model.predict(test_x)

print('예측값 : ', pred[:5])
print('실제값 : ', np.array(test_y[:5]))

# 분류 정확도
from sklearn.metrics import accuracy_score
print('분류 정확도 : ', accuracy_score(test_y, pred))

print('특성(변수) 중요도 :\n{}'.format(model.feature_importances_))

# 특성 중요도 시각화
def plot_feature_importances(model):
    n_features = x.shape[1]
    # bar 차트(horizon)
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), x.columns)
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1, n_features)
    plt.show()
    plt.close()

plot_feature_importances(model)






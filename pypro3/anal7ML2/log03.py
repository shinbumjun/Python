'''
LogisticRegression 클래스 사용
pima-indians-diabetes dataset
'''
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd
import array

# 피마 인디언 당뇨병 데이터 세트는 아래와 같이 구성되어있다.
# Pregnancies: 임신 횟수
# Glucose: 포도당 부하 검사 수치
# BloodPressure: 혈압(mm Hg)
# SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm)
# Insulin: 혈청 인슐린(mu U/ml)
# BMI: 체질량지수(체중(kg)/키(m))^2
# DiabetesPedigreeFunction: 당뇨 내력 가중치 값
# Age: 나이
# Outcome: 클래스 결정 값(0 또는 1)

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/pima-indians-diabetes.data.csv"
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI' , 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv(url, names = names)
print(df.head(3), df.shape) # (768, 9)

arr = df.values
x = arr[:, 0:8]
print(x[:3], x.shape) # [[  6.    148.     72.     35.      0.     33.6     0.627  50.   ] ... (768, 8)
y = arr[:, 8]
print(y[:3], y.shape) # [1. 0. 1.] (768,)
# x 값은 메트릭스 y 값은 벡터

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
                                                                    test_size = 0.33, random_state = 7)
print(x_train.shape, x_test.shape) # (514, 8) (254, 8)
 
'''
model = LogisticRegression()
model.fit(x_train, y_train)
print('예측값 : ', model.predict(x_test[:5])) # 예측값 :  [0. 1. 1. 0. 0.]
print('실제값 : ', y_test[:5]) # 실제값 :  [0. 1. 1. 0. 1.]
print((model.predict(x_test) != y_test).sum()) 
# 254개 중 54개 틀림
print('test로 분류 정확도 : ', model.score(x_test, y_test))
print('train으로 분류 정확도 : ', model.score(x_train, y_train))
# test로 분류 정확도 :  0.7874015748031497
# train으로 분류 정확도 :  0.77431906614786

from sklearn.metrics import accuracy_score
pred = model.predict(x_train)
print('분류 정확도 : ', accuracy_score(y_train, pred)) 
# 분류 정확도 :  0.77431906614786

# 모델의 분류 성능이 목표치에 도달했다면 모델을 저장 후 저장된 모델로 분류 결과 예측
pickle.dump(model, open('pima_model.sav', 'wb'))
'''

model = pickle.load(open('pima_model.sav', 'rb'))
print('test로 분류 정확도 : ', model.score(x_test, y_test))
# test로 분류 정확도 :  0.7874015748031497
# [[ 1.   90.   62.   12.   43.   27.2   0.58 24.  ]]

print(x_test[:1]) # 분류는 원하는 새로운 데이터라고 가정
print('분류 예측 : ', model.predict(x_test[:1])) # 분류 예측 :  [0.]











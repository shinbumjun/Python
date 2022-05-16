'''
weather dataset으로 비 유무 처리용 나이브베이즈 분류 모델
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('데이터 확인')
df = pd.read_csv("../testdata/weather.csv")
print(df.head(3))
print(df.info())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('내일날씨 값 변경')
x = df[['MinTemp', 'MaxTemp', 'Rainfall']]
label = df['RainTomorrow'].map({'Yes':1, 'No':0})
print(x[:3])
print(label[:3])

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('train / test')
train_x, test_x, train_y, test_y = train_test_split(x, label, random_state = 0)

gmodel = GaussianNB()
gmodel.fit(train_x, train_y)

pred = gmodel.predict(test_x)
print('예측값 : ', pred[:10])
print('실제값 : ', test_y[:10].values)
# 예측값 :  [0 0 0 0 0 0 0 0 0 0]
# 실제값 :  [0 0 1 0 1 1 1 0 0 0]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('정확도 보기 (분류 보고서)')
print('acc : ', accuracy_score(test_y, pred))
print('report : \n', metrics.classification_report(test_y, pred))




















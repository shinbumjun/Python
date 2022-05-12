'''
***데이터 가공 연습 (전처리 과정) 스토리있게~
# titanic dataset으로 LogisticRegression, DecisionTreeClassifier, RandomForestClassifier 처리

1. LogisticRegression
2. DecisionTreeClassifier
3. RandomForestClassifier

딥러닝말고도 고전적인 데이터 분석 사용하기 
어떤 모델이 좋은지 확인해보고 사용하기
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv")
print(df.head(2), df.head)
df.drop(columns = ['PassengerId', 'Name', 'Ticket'], inplace = True) # 불필요한 것 삭제
print(df.info())
pd.set_option('display.max_columns', 300)
print(df.describe()) # 요약
print(df.info())
print(df.isnull().sum()) # Age:177 ,Cabin:687, Embarked:2 null인 갯수

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('Null 처리 : 0또는 평균 또는 제거 또는 임의의 값으로 대체')
df['Age'].fillna(df['Age'].mean(), inplace = True) # 평균으로 대체
df['Cabin'].fillna('N', inplace = True) # N으로 대체
df['Embarked'].fillna('N', inplace = True) # N으로 대체
print(df.isnull().sum())
print(df.head(2), df.shape) # (891, 9)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('object type : Sex, Cabin, Embarked 애네들의 상태를 별도 확인') # 특징을 파악해서 
print('Sex : ', df['Sex'].value_counts()) # male:577, female:314
print('Cabin : ', df['Cabin'].value_counts())
df['Cabin'] = df['Cabin'].str[:1] # 첫글자
# print(df.head(5))
print('Cabin : ', df['Cabin'].value_counts())
print('Embarked : ', df['Embarked'].value_counts())
print(df.head(5))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('성별이 생존확률에 어떤 영향을 가했는가?')
print(df.groupby(['Sex', 'Survived'])['Survived'].count())
# Sex     Survived
# female  0            81 -> 사망
#         1           233 -> 생존
# male    0           468 -> 사망
#         1           109 -> 생존
print('승객은 남자가 많지만 생존자는 여자가 더 많다~ 왜그럴까?')
print('여자 생존율 : ', 233 / (81 + 233)) # 0.742
print('남자 생존율 : ', 109 / (468 + 109)) # 0.18

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화 : 성별 생존확률')
# sns.barplot(x = 'Sex', y='Survived', data = df, ci = 95) # 95의 신뢰
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화 : 성별, Pclass별 생존확률')
# sns.barplot(x = 'Pclass', y='Survived', hue ='Sex', data = df, ci = 95) # 95의 신뢰
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('나이별 생존 확률')
print(df['Age'])
def age_category_func(age):
    msg = ''
    if age <= -1:msg = 'unknown'
    elif age <= 5:msg = 'baby'
    elif age <= 18:msg = 'teenager'
    elif age <= 65:msg = 'adult'
    else: msg = 'elder'
    return msg

df['Age_category'] = df['Age'].apply(lambda a: age_category_func(a)) # 함수를 실행하는 함수   
# print(df.head(10))
    
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화 : 성별 나이별 생존확률')
# sns.barplot(x = 'Age_category', y='Survived', hue = 'Sex', data = df,
#             order = ['unknown','baby', 'teenager', 'adult', 'elder'])
# plt.show()    
    
del df['Age_category'] # 필요없는 카테고리 지우기 
    
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('Dummy 변수 : 문자열 -> 숫자 (범주형)')
from sklearn import preprocessing    
    
def label_incode_func(datas):    
    cols = ['Cabin', 'Sex', 'Embarked']
    for c in cols:
        la = preprocessing.LabelEncoder().fit(datas[c])
        datas[c] = la.transform(datas[c])
    return datas

df = label_incode_func(df)
print(df.head(3), type(df))
print(df['Cabin'].unique()) # [7 2 4 6 3 0 1 5 8]
print(df['Sex'].unique()) # [1 0]
print(df['Embarked'].unique()) # [3 0 2 1]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('데이터 가공 ...')
from sklearn.model_selection import train_test_split
feature_df = df.drop(['Survived'], axis = 'columns')
label_df = df['Survived']
print(feature_df.head(3)) # 여기있는 것들이 
#    Pclass  Sex   Age  SibSp  Parch     Fare  Cabin  Embarked
# 0       3    1  22.0      1      0   7.2500      7         3
# 1       1    0  38.0      1      0  71.2833      2         0
# 2       3    0  26.0      0      0   7.9250      7         3

print(label_df.head(3)) # 여기에 영향을 준다
# 0    0
# 1    1
# 2    1

x_train, x_test, y_train, y_test = train_test_split(feature_df, label_df, test_size = 0.2, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (712, 8) (179, 8) (712,) (179,)

from sklearn.linear_model import LogisticRegression # 사이클런 리니어 모델 
from sklearn.tree import DecisionTreeClassifier # 사이클런 트리
from sklearn.ensemble import RandomForestClassifier # 사이클런 랜덤포레스트
from sklearn.metrics import accuracy_score

logmodel = LogisticRegression(solver = 'lbfgs', max_iter=500).fit(x_train, y_train) # 학습과 테스트가 있는데 학습
demodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier().fit(x_train, y_train)

logpredict = logmodel.predict(x_test)
print('LogisticRegression acc : {0:.5f}'.format(accuracy_score(y_test, logpredict)))
depredict = demodel.predict(x_test)
print('DecisionTreeClassifier acc : {0:.5f}'.format(accuracy_score(y_test, depredict)))
rfpredict = rfmodel.predict(x_test)
print('RandomForestClassifier acc : {0:.5f}'.format(accuracy_score(y_test, rfpredict)))

# RandomForestClassifier가 제일 성능이 좋은걸로 알고있지만 
# 데이터마다 최적의 모델이 있는 것처럼 지금은 LogisticRegression 모델이 제일 좋다

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('\nGridSearchCV')
from sklearn.model_selection import GridSearchCV

# min_samples_split : 노드 분할 최소 샘플 수는 ?
# mon_samples_leaf : 리프 노드 최소 샘플 수는 ? 
# ...
params = {'max_depth':[2,3,5,10,15], 'min_samples_split':[2,3,5], 'min_samples_leaf':[1,5,8]}

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('DecisionTreeClassifier')
grid_clf = GridSearchCV(demodel, param_grid = params, scoring='accuracy', cv = 5)
grid_clf.fit(x_train, y_train)
print(grid_clf.best_params_)
print(grid_clf.best_score_)
best_clf = grid_clf.best_estimator_ # 최적의 모델 얻기
bestPredict = best_clf.predict(x_test)
print('DecisionTreeClassifier acc : {0:.5f}'.format(accuracy_score(y_test, bestPredict))) # 0.80447

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('RandomForestClassifier') 
grid_clf2 = GridSearchCV(rfmodel, param_grid = params, scoring='accuracy', cv = 5)
grid_clf2.fit(x_train, y_train)
print(grid_clf2.best_params_)
print(grid_clf2.best_score_)
best_clf2 = grid_clf2.best_estimator_ # 최적의 모델 얻기
bestPredict2 = best_clf2.predict(x_test)
print('RandomForestClassifier acc : {0:.5f}'.format(accuracy_score(y_test, bestPredict2))) # 0.78771

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('RandomForestClassifier 학습량 많고 성능좋다 하지만 titanic dataset로는 DecisionTreeClassifier가 더 최적의 모델이다')







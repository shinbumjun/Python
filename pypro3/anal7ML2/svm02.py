'''
SVM으로 XOR 분류 처리 연산 처리 

신경망은 뉴런을 늘려주는것인데 
svm.SVC() 차원을 올려서 사용 (더 정확하다)
후에 딥러닝이 나와서 밀려났다
'''
x_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

x_df = pd.DataFrame(x_data)
feature = np.array(x_df.iloc[:, 0:2])
label = np.array(x_df.iloc[:, 2])
print(feature)
print(label) # 실제값 : ...

# model = LogisticRegression()
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('신경망은 뉴런을 늘려주는것인데 svm.SVC() 차원을 올려서 사용 (더 정확하다) 후에 딥러닝이 나와서 밀려났다')
model = svm.SVC()
model.fit(feature, label)
pred = model.predict(feature)
print('예측값:', pred) # 예측값 : ...

print('정확도 : ', metrics.accuracy_score(label, pred)) # 0.5









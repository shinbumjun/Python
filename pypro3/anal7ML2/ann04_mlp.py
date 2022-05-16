# MLP : 다층신경망 - 선형 / 비선형 예측 모델이 가능
import numpy as np

from sklearn.neural_network import MLPClassifier

from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('지도학습')
# label = np.array([0,0,0,1]) # and
# label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor -> 하나의 노드만으로는 xor 0.5만 나온다


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('참고 : https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html')
# ml = MLPClassifier(hidden_layer_sizes = 30, activation = 'relu',
#                    solver='adam', learning_rate_init = 0.01).fit(feature, label)

ml = MLPClassifier(hidden_layer_sizes = (10, 10, 10), activation = 'relu',
                   solver='adam', learning_rate_init = 0.01).fit(feature, label)
                   
print(ml)

pred = ml.predict(feature)
print('pred : ', pred)
print('acc : ', accuracy_score(label, pred))
















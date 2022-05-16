'''
인공신경말 : 단층 신경망(뉴런 또는 노드가 1개) - Perceptron (지도학습)
input data * 가중치의 합에 대해 임계값(활성화함수)을 이항 분류가 가능
'''
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
# [[0 0]
#  [0 1]
#  [1 0]
#  [1 1]]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('지도학습')
# label = np.array([0,0,0,1]) # and
# label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor -> 하나의 노드만으로는 xor 0.5만 나온다


ml = Perceptron(max_iter=4, eta0 = 0.1).fit(feature, label) # max_iter 학습량
print(ml)
pred = ml.predict(feature)
print('pred : ', pred)
print('acc : ', accuracy_score(label, pred))





























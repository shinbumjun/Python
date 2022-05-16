'''
MLP : 다층신경망 - 선형 / 비선형 예측 모델이 가능
breast_cancer dataset
'''
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

x = cancer['data']
y = cancer['target']
print(x[:2])
print(y[:2])
print(cancer.target_names) # ['malignant' 'benign']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 42, test_size = 0.3)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('표준화')
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
scaler.fit(x_test)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
print(x_train[:1])

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('max_iter = 10 (기울기가 0인 y값 찾기), learning_rate_init = 1 : 1씩 내려감')
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(30, 10),max_iter = 10, 
                    learning_rate_init = 0.1, solver='adam', random_state=1, verbose=1) # verbose=1 진행과정 보임
mlp.fit(x_train, y_train)

pred = mlp.predict(x_test)

print('예측값  : ', pred[:10]) # [1 0 0 1 1 0 0 0 0 1]
print('실제값  : ', y_test[:10]) # [1 0 0 1 1 0 0 0 1 1]
print('acc(train) : ', mlp.score(x_train, y_train)) # 0.9874371859296482
print('acc(test) : ', mlp.score(x_test, y_test)) # 0.9766081871345029










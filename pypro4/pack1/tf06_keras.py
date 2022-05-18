'''

'''
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('XOR 게이트 논리 모델을 생성 후 처리')
print('1. 데이터 셋 생성')
x = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
y = np.array([0, 1, 1, 0])

print(x) # feature
print(y) # label(class)



# model = Sequential([
#     Dense(input_dim = 2, units=1),
#     Activation('sigmoid')
# ])


# model = Sequential()
# model.add(Dense(units = 5, input_dim = 2)) # 입력 2개, 출력 5개, Dense(for대체), 활성화 함수로 relu
# model.add(Activation('relu'))
# model.add(Dense(units = 1)) # 5개 -> 1개로 들어오고
# model.add(Activation('sigmoid')) # 이진분류에는 sigmoid


model = Sequential()
model.add(Dense(units=5, input_dim = 2, activation='relu'))
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))


model.compile(optimizer = 'adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x, y, epochs=100, batch_size = 1, verbose = 0) 
# epochs 100번 학습, batch_size 1개풀고 답마추고~, verbose 중간과정
loss_metrics = model.evaluate(x, y)
print('loss_metrics : ', loss_metrics)

pred = (model.predict(x) > 0.5).astype('int32')
# print('예측결과 : ', pred)
print('예측결과 : ', pred.flatten())


print('history : ', history.history) # dist타입으로 row가 보인다
print('loss : ', history.history['loss'])
print('acc : ', history.history['accuracy'])


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('학습 진행 중 loss, acc를 시각화')
# import matplotlib.pyplot as plt
# plt.plot(history.history['loss'], label='train loss')
# plt.plot(history.history['accuracy'], label='train accuracy')
# plt.xlabel('epochs')
# plt.legend(loc = 'best')
# plt.show()


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('상세하게 확인')
print(model.layers)
print(model.summary()) # 상세하게
# print(model.weights)




















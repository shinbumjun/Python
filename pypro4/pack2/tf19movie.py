'''
영화 리뷰 데이터(imdb dataset)로 이진분류 (이항)

[참고]
https://wikidocs.net/24586
'''
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import imdb

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape) # (25000,) (25000,) (25000,) (25000,)
print('훈련용 리뷰 개수 : {}'.format(len(x_train))) # 훈련용 리뷰 개수 : 25000
print('테스트용 리뷰 개수 : {}'.format(len(x_test))) # 테스트용 리뷰 개수 : 25000
num_classes = len(set(y_train))
print('카테고리 : {}'.format(num_classes)) # 카테고리 : 2
print(set(y_train)) # {0, 1}

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('라벨링된 실제 영문자료 확인')
word_ind = imdb.get_word_index() # {1:'good job .....', ...}
print(word_ind) # {'fawn': 34701, 'tsukino': 52006, ...
# print(word_ind.items()) # dict_items([('fawn', 34701), ('tsukino', 52006), ...

reverse_word_index = dict([(value, key) for (key, value) in word_ind.items()])
print(reverse_word_index) # {34701: 'fawn', 52006: 'tsukino', ...
print(reverse_word_index.get(x_train[0][2])) # you
decode_review = ' '.join([reverse_word_index.get(i) for i in x_train[24999]])
print(decode_review)
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('데이터 준비 : feature : one-hot encoding 25000 by 10000')
print(x_train[:1])

def vector_seq(sequences, dim = 10000):
    results = np.zeros((len(sequences), dim))
    for i, seq in enumerate(sequences): # enumerate 데이터가 있는 지역에만 1
        results[i, seq] = 1.
    return results 

x_train = vector_seq(x_train)
print(x_train[:1], x_train.shape) # [[0. 1. 1. ... 0. 0. 0.]] (25000, 10000)
x_test = vector_seq(x_test)

y_train = np.asarray(y_train).astype('float32')
y_test = np.asarray(y_test, 'float32')
print(y_train) # [1. 0. 0. ... 0. 1. 0.]

# 가공 끝 -> 모델 만들기

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('model')
from keras import models, layers, regularizers
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10000,),
                kernel_regularizer = regularizers.l2(0.0001))) # 10000개 -> 16나감
model.add(Dense(32, activation='relu'))
model.add(Dropout(rate=0.3)) # 오버피팅 방지를 목적으로 
model.add(Dense(16, activation='relu'))
model.add(Dropout(rate=0.3)) # 오버피팅 방지를 목적으로 
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
print(model.summary())

# 훈련시 검증데이터(validation data) 사용
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
print(len(x_val), len(partial_x_train))  # 10000 15000
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

history = model.fit(partial_x_train, partial_y_train, epochs=30, 
                    batch_size = 512, validation_data=(x_val, y_val), verbose = 2)

print('모델 성능 평가 : ', model.evaluate(x=x_test, y=y_test))

print('모델 성능 평가 : ', model.evaluate(x=x_test, y=y_test))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')

history_dict = history.history
print(history_dict.keys())
loss = history_dict['loss']
val_loss = history_dict['val_loss']
epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'bo', label = 'train loss')
plt.plot(epochs, val_loss, 'r-', label = 'validation loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

acc = history_dict['acc']
val_acc = history_dict['val_acc']

plt.plot(epochs, acc, 'bo', label = 'train acc')
plt.plot(epochs, val_acc, 'r-', label = 'validation acc')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend()
plt.show()

pred = model.predict(x_test[:5])
print('실제값:', y_test[:5])
print('예측값:', np.where(pred > 0.5, 1, 0).flatten())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('과적합 방지')
# 1) train/test split, train-validation/test split
# 2) 가중치 규제(regularization)이다.
#    가중치 규제란 말 그대로 가중치의 값이 커지지 않도록 제한 하는 기법이다.
#    가중치를 규제하면 모델의 일반화 성능이 올라간다.
#    regularizers를 이용해서 L1, L2 규제
#    L1 규제는 손실 함수에 가중치의 절대값인 L1 노름(norm)을 추가 한다.
#    L2 규제는 손실 함수에 가중치에 대한 L2 노름(norm)의 제곱을 더한다.
# 3) Dropout : 훈련하는 동안 층의 일부 노드를 훈련해서 제외
# 4) Batch Normalization
# 5) train data를 늘림
# 기타 ...










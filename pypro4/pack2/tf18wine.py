'''
wine dataset : 레드와 화이트 와인 분류
'''
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

wdf = pd.read_csv("../testdata/wine.csv", header = None)
print(wdf.head(2))
print(wdf.info())
print(wdf.iloc[:, 12].unique()) # [1 0]
print(len(wdf[wdf.iloc[:, 12] == 0])) # 0 -> 4898 
print(len(wdf[wdf.iloc[:, 12] == 1])) # 1 -> 1599

dataset = wdf.values
x = dataset[:, 0:12]
y = dataset[:, -1]
print(x[:1])
print(y[:1])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 12)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('model') 
model = Sequential()
model.add(Flatten()) # 차원을 축소해주는 class
model.add(Dense(32, input_dim=12, activation = 'relu'))
model.add(Dense(16, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# print(model.summary())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('fit() 전에 모델 정확도') 
loss, acc = model.evaluate(x_train, y_train)
print('훈련 전 모델 성능 : {5.2f}'.format(acc * 100))

print()
early_stop = EarlyStopping(monitor='val_loss', patience = 5)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('학습 중 model 저장')
import os
MODEL_DIR = "./wine_model/"
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

# modelPath = MODEL_DIR + "{epoch:02}_{loss:.3f}.hdf5"
modelPath = MODEL_DIR + "wine_model.hdf5" # 가장 베스트 모델만 저장  

chkPoint =  ModelCheckpoint(filepath=modelPath, monito='loss', save_best_only=True)

history = model.fit(x_train, y_train, epochs = 1000, batch_size = 64,
                    validation_split = 0.2,
                    callbacks = [early_stop, chkPoint], verbose = 2)

loss, acc = model.evaluate(x_test, y_test)
print('훈련 후 모델 성능 : {5.2f}'.format(acc * 100))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('내가 직접 성능 좋은 모델을 판단해 저장 한다면 model.save("파일명.h5") - 그러나 ModelCheckpoint가 있다.')

print('history 관련')
vloss = history.history['val_loss']
print('vloss : ', vloss, len(vloss))
loss = history.history['loss']
print('loss : ', loss, len(loss))
acc = history.history['accuracy']
print('acc : ', acc, len(acc))
vacc = history.history['val_accuracy']
print('vacc : ', vacc, len(vacc))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
epoch_len = np.arange(len(acc))
plt.plot(epoch_len, vloss, c='red', label='val_loss')
plt.plot(epoch_len, loss, c='blue', label='loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()

epoch_len = np.arange(len(acc))
plt.plot(epoch_len, vloss, c='red', label='val_loss')
plt.plot(epoch_len, loss, c='blue', label='loss')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend(loc='best')
plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('예측')
print('베스트 모델이 저장되었으므로 더 이상의 학습은 진행x')
print('베스트 모델을 읽어 새로운 데이터에 분류 작업')
from keras.models import load_model
mymodel = load_model('wine_model/wine_model.hdf5')
new_data = x_test[:5, :]
print(new_data)
pred = mymodel.predict(new_data)
print('분류 결과:', np.where(pred > 0.5, 1, 0).flatten())





























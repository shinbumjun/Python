# wine dataset  레드와 화이트분류, 1
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Input, Flatten
from keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os


wd = pd.read_csv("../testdata/wine.csv", header=None)
print(wd.head(2))
print(wd.info())
print(wd.iloc[:, 12].unique())      #  [1 0]  이진분류     
print(len(wd[wd.iloc[:, 12]==0]))    # 4898
print(len(wd[wd.iloc[:, 12]==1]))    # 1599 

data = wd.values
x = data[:, 0:12]
y = data[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)

model = Sequential()
model.add(Flatten())       # 2차원을 1차원으로 줄세울떄, 
model.add(Dense(32, input_dim=12, activation= 'relu'))
model.add(Dense(16, activation= 'relu'))
model.add(Dense(8, activation= 'relu'))
model.add(Dense(1, activation= 'sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
print(model.summary)

# fit() 전에 모델 정확도
loss, acc = model.evaluate(x_train, y_train)
print('훈련 전 모델성능 : {:5.2f}%' .format(acc * 100))

print('\n 학습 시작------------------------- ')
early = EarlyStopping(monitor='loss', patience=5)

### 학습 주 model 저장  import os 
MODEL_DIR = "./wine_model/"
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)
#model_path = MODEL_DIR + "{epoch :02}_{loss:.3f}.hdf5"   베스트 모델 다
model_path = MODEL_DIR + "wine_model.hdf5"    # 계속 덮어써서 마지막 모델만 남음 
ckp = ModelCheckpoint(filepath=model_path, monitor='loss', save_best_only=True)   
    
history = model.fit(x_train, y_train, epochs=500, batch_size=64, callbacks =[early, ckp],
                    validation_split=0.2, verbose=0)              # batch 기본값은 32

loss, acc = model.evaluate(x_test, y_test)
print('훈련 후 모델성능 : {:5.2f}%' .format(acc * 100))

# 내가 직접 성능좋은 모델을 판단해 저장 한다면 model.save("파일명.h5") 

## history 관련
vloss = history.history['val_loss']
print('val_loss :', vloss, len(vloss))
loss = history.history['loss']
print('loss :', loss, len(loss))
acc = history.history['acc']
print('acc :', acc, len(acc))
vacc = history.history['val_acc']
print('val_acc :', vacc, len(vacc))


## 시각화
epoch_len = np.arange(len(acc))
plt.plot(epoch_len, vloss, c ='red', label='val_loss')
plt.plot(epoch_len, loss, c='blue', label='loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()

plt.plot(epoch_len, vacc, c ='red', label='val_acc')
plt.plot(epoch_len, acc, c='blue', label='acc')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend(loc='best')
plt.show()

## 예측 
# 베스트 모델이 저장되었으므로 더이상 학습 진행 필요없다
# 베스트 모델을 읽어 새로운 데이터에 대한 분류 진행
from keras.models import load_model
my = load_model('wine_model/wine_model.hdf5')
new = x_test[:5, :]
pred = my.predict(new)
print('분류 결과 :', np.where(pred > 0.5, 1, 0).flatten())
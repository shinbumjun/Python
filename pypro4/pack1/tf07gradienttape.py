'''
선형회귀 모델 생성 : 
'''
import tensorflow as tf
import numpy as np

opti = tf.keras.optimizers.SGD() # RMSProp, Adam
w = tf.Variable(tf.random.normal((1,))) # 튜플로 줌
b = tf.Variable(tf.random.normal((1,)))
print(w.numpy())
print(b.numpy())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('모델')
@tf.function # 제약사항 참고
def train_step(x, y): 
    with tf.GradientTape() as tape:
        hypo = tf.add(tf.multiply(w, x), b)
        loss = tf.reduce_mean(tf.square(tf.subtract(hypo, y)))
    grad = tape.gradient(loss, [w, b]) # 편미분이 수행    
    opti.apply_gradients(zip(grad, [w, b])) # 경사하강법
    return loss

x = [1.,2.,3.,4.,5.] # feature
y = [1.2,2.0,3.0,3.5,5.5] # label
print(np.corrcoef(x, y)) # 0.974 : 양의 상관관계

w_val = [] # w 값의 변수
cost_val = [] #cost 값의 변수
for i in range(101):
    loss_val = train_step(x, y)
    cost_val.append(loss_val.numpy())
    w_val.append(w.numpy())
    if i % 10 == 0:
        print(loss_val)

print(cost_val)
print(w_val)



import matplotlib.pyplot as plt
plt.plot(w_val, cost_val, 'o')
plt.xlabel('w')
plt.ylabel('cost')
plt.show()


print('cost가 최소일때 w값 : ', w.numpy())
print('cost가 최소일때 b값 : ', b.numpy())


y_pred = tf.multiply(x, w) + b  # y=wx+b
print('예측값 : ', y_pred.numpy())
print('실제값 : ', y)


plt.plot(x, y, 'ro', label='real')  # 실제값
plt.plot(x, y_pred, 'b-', label='pred')    # 예측값
plt.xlabel('x')
plt.ylabel('y')
plt.show()


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('미지의 새로운 값으로 y를 예측')
new_x = [3.5, 9.0]
new_pred = tf.multiply(x, w) + b
print('새로운 값으로 y를 예측 : ', new_pred.numpy())















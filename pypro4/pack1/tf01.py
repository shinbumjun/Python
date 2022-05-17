'''
DeepLearning library : TensorFlow
'''
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('텐서플로우의 이해')
import tensorflow as tf
print((tf.__version__))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('상수 정의')
print(1, type(1))
print([1], type([1]))
print(tf.constant(1), type(tf.constant(1))) # scalar, 0 D tensor
print(tf.constant([1])) # vector, 1 D tensor
print(tf.constant([[1]])) # matrix, 2 D tensor

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('연산')
a = tf.constant([1, 2])
b = tf.constant([3, 4])
c = a + b # numpy 연산과 동일 (같은 열 더함)
print(c, type(c)) 
c = tf.add(a, b) # 텐플로우의 add를 사용해도됨
print(c, type(c))
# d = tf.constant([3])
# d = tf.constant(3)
d = tf.constant([[3]])

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('broadcast 연산')
e = c + d 
print(e)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('실수화')
print(7, type(7))
print(tf.convert_to_tensor(7, dtype=tf.float32))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('')
print(tf.cast(7, dtype=tf.float32))
print(tf.constant(7.0))
print(tf.constant(7, dtype=tf.float32))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('')
import numpy as np
arr = np.array([1, 2, 3])
print(arr ,type(arr))
tfarr = tf.add(arr, 5) # numpy + tensorflow = tensorflow
print(tfarr)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('numpy type으로 형변환')
print(tfarr.numpy()) # numpy type으로 형변환 (강제)
print(np.add(tfarr, 3)) # numpy type으로 형변환 (자동)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('')
list(tfarr.numpy())



















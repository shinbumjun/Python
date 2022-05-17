'''
연산자, 함수

add, subtract, multiply, divide
삼항연산
'''
import numpy as np
import tensorflow as tf

f1 = lambda : tf.constant(1)
print(f1())
f2 = lambda : tf.constant(2)
a = tf.constant(3)
b = tf.constant(4)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('case 조건')
result = tf.case([(tf.less(a, b), f1)], default = f2) # if (a < b) return 1 else return 2
print(result.numpy())


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('관계 / 논리 연산')
print(tf.equal(1, 2).numpy())
print(tf.not_equal(1, 2))
print(tf.less(1, 2))
print(tf.greater(1, 2))
print(tf.greater_equal(1, 2))

print(tf.logical_and(True, False).numpy()) # False
print(tf.logical_or(True, False).numpy()) # True
print(tf.logical_not(True, False).numpy()) # False


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('tf.reduce...')
ar = [[1, 2], [3, 4]]
print(tf.reduce_sum(ar))
print(tf.reduce_mean(ar)) # 전체평균
print(tf.reduce_mean(ar, axis = 0)) # 열기준
print(tf.reduce_mean(ar, axis = 1)) # 행기준














'''
constant : 텐서를 직접 기억
Variable : 텐서가 저장된 주소를 참조

@tf.function 사용할때 제약사항 알아두기~

[주요함수]
https://cafe.daum.net/flowlife/S2Ul/6
'''

import tensorflow as tf
import numpy as np

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('기본은 floar32')
node1 = tf.constant(3, tf.float32)
node2 = tf.constant(4.0)
print(node1)
print(node2)
imsi = tf.add(node1, node2)
print(imsi)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('위랑 결과값 같음')
node3 = tf.Variable(3, dtype=np.float32)
node4 = tf.Variable(4.0)
print(node3)
print(node4)
imsi2 = tf.add(node3, node4)
print(imsi2)

node4.assign_add(node3)
print(node4)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('')
a = tf.constant(5)
b = tf.Variable(10)
c = tf.multiply(a, b)
print(c, c.numpy())

result = tf.cond(a < b, lambda:tf.add(10, c), lambda:tf.square(a))
print('result : ', result.numpy())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('')
# v = tf.Variable(1)
v = tf.Variable(2)

@tf.function # 오토그래프 기능
def find_next_odd():
    v.assign(v + 1)
    if tf.equal(v % 2, 0):
        v.assign(v + 10)

find_next_odd()
print(v.numpy())
print(type(find_next_odd))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('')
def func1(): # 1 ~ 3까지 증가
    imsi = tf.constant(0) # imsi = 0
    su = 1
    for _ in range(3):
        # imsi = tf.add(imsi, su)
        # imsi = imsi + su
        imsi += su
    return imsi

kbs = func1()
print(kbs.numpy(), ' ', np.array(kbs))


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('')

@tf.function
def func2(): # 1 ~ 3까지 증가
    # imsi = tf.constant(0) # imsi = 0
    global imsi
    su = 1
    for _ in range(3):
        # imsi = tf.add(imsi, su)
        # imsi = imsi + su
        imsi += su
    return imsi

mbc = func2()
print(kbs.numpy(), ' ', np.array(mbc))


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('오토그래프가 있을경우 Variable을 밖에다가 작성')
imsi = tf.Variable(0) # 밖에 작성
@tf.function # 기능을 넣을 경우
def func3():
    # imsi = tf.Variable(0) # 오토그래프를 사용할 경우 밖에
    su = 1
    for _ in range(3):
        imsi.assign_add(su) # o
        # imsi = imsi + su # x
        # imsi += su # x
    return imsi

sbs = func3()
print(sbs.numpy(), ' ', np.array(sbs))


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('3단 구구단 출력')
print('@tf.function 출력은 담당하지 않고 연산만 담당한다')

# @tf.function 
def gugu1(dan):
    su = tf.constant(0) # su = 0
    for _ in range(9):
        su = tf.add(su, 1)
        # print(su)
        # print(su.numpy())
        print('{}*{}={:2}'.format(dan, su, dan * su))
gugu1(3)


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('4단 구구단 출력')
# @tf.function
def gugu2(dan):
    for i in range(1, 10):
        result = tf.multiply(dan, i) # tf.multiply() : 요소곱, tf.matmul() : 행렬곱
        print('{}*{}={:2}'.format(dan, i, result))
        
gugu2(4)



































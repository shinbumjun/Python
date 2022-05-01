# numpy
# tip : append, insert, delete
# tip : arange 차원만들기
# tip : concatenate : 배열 결합, split : 배열 분할

import numpy as np

aa = np.eye(3)
print(aa)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''

bb = np.c_[aa, aa[2]] # 2열(세번째)과 동일한 열 추가
print(bb)
'''
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 1.]]
'''
cc = np.r_[aa, [aa[2]]] # 2행(세번째) 추가
print(cc)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]
 [0. 0. 1.]]
'''

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ append, insert, delete ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
a = [1,2,3]
b = np.append(a, [4, 5])
print(b) # [1 2 3 4 5]

c = np.insert(a, 2, [6, 7]) # 2번째(3번째)에서부터 추가
print(c) # [1 2 6 7 3]

d = np.delete(a, 1) # 1번째(2번째) 삭제
print(d) # [1 3]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ arange : 차원만들기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
aa = np.arange(1, 10).reshape(3, 3)
print(aa)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

bb = np.arange(10, 19).reshape(3, 3) # 2차원
print(bb)
'''
[[10 11 12]
 [13 14 15]
 [16 17 18]]
'''

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ append : 행, 열 방향으로 벡터 추가 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
cc = np.append(aa, bb) # append
print(cc) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18]

cc = np.append(aa, bb, axis = 0) # 행 방향으로 벡터 추가
print(cc)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]
 [13 14 15]
 [16 17 18]]
'''

cc = np.append(aa, bb, axis = 1) # 열 방향으로 벡터 추가
print(cc)
'''
[[ 1  2  3 10 11 12]
 [ 4  5  6 13 14 15]
 [ 7  8  9 16 17 18]]
'''

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ delete : 삭제 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(np.delete(aa, 1)) # [1 3 4 5 6 7 8 9]
print(np.delete(aa, 1, axis = 0)) # 1행(2행) 삭제
print(np.delete(aa, 1, axis = 1)) # 1열(2열) 삭제

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 조건연산 where(조건, 참, 거짓) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
x = np.array([1,2,3])
y = np.array([4,5,6])
condData = np.array([True, False, True])
result = np.where(condData, x, y)
print(result) # [1 5 3]

aa = np.where(x >= 2) # 2이상 참인것만
print(x[aa]) # [2 3]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ concatenate : 배열 결합, split : 배열 분할 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
kbs = np.concatenate([x, y]) # 배열 결합
print(kbs) # [1 2 3 4 5 6]
v1, v2 = np.split(kbs, 2) # 배열 분할
print(v1) # [1 2 3]
print(v2) # [4 5 6]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ vsplit(행), hsplit(열) : 분열 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
a = np.arange(1, 17).reshape(4, 4)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
'''
print(a)
x1, x2 = np.hsplit(a, 2) # 2열로 각각
print(x1)
'''
[[ 1  2]
 [ 5  6]
 [ 9 10]
 [13 14]]
'''
print(x2)
'''
[[ 3  4]
 [ 7  8]
 [11 12]
 [15 16]]
'''
x1, x2 = np.vsplit(a, 2) # 2행으로 각각
print(x1)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
print(x2)
'''
[[ 9 10 11 12]
 [13 14 15 16]]
'''

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 복원 / 비복원 추출 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
li = np.array([1,2,3,4,5,6,7])

print('복원 추출')
for _ in range(5):
    print(li[np.random.randint(0, len(li) - 1)], end = ' ')

print('\n비복원 추출')
import random
print(random.sample(list(li), k = 5))
print(random.sample(range(1, 46), k = 6))

print('비복원 추출')
print(list(np.random.choice(range(1, 46), 6))) 

print('복원 추출')
print(list(np.random.choice(range(1, 46), 6, replace = True))) 

print('선택 확률')
arr = 'air book cat d e f god'
arr = arr.split(' ')
print(arr)
print(np.random.choice(arr, 3, p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4])) # 선택 확률















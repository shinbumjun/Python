# 1. numpy 기본 이해 
# tip1 : list와 numpy의 배열 비교
# tip2 : numpy로 배열을 만들면 같은 공간(주소)에서 실행, Python List는 새롭게 객체를 생성한다
# tip4 : *인덱싱, 슬라이싱 이해가 필요
# tip4 : *차원에 대한 이해가 필요

import numpy as np

print(np.__version__) # 버젼 1.20.3

s = 'tom'

ss = ['tom', 'james', 'oscar']
print(ss, type(ss)) # 타입 : <class 'list'> 

ss2 = np.array(ss)
print(ss2, type(ss2)) # 타입 : <class 'numpy.ndarray'>

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ list/ndarray 기억상태 구분 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
li = list(range(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li)
print(id(li[0]), id(li[1])) # 2231992215856 2231992215888 주소가 다르다

print(li * 10) # 곱하기가 되지않고 10번 반복된다
# print('-' * 10)

print()
for i in li:
    print(i * 10, end = ' ')

print()
print([i * 10 for i in li])

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ list와 numpy의 비교 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ') # list to ndarray
num_arr = np.array(li)
print(num_arr)
print(id(num_arr[0]), id(num_arr[1])) # 1714221156880 1714221156880 주소가 같다
print(num_arr * 10) # for 문장을 돌리지 않았는데 곱하기가 되었다

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 배열은 타입이 일치 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# a = np.array([1,2,3]) # 데이터는 상위 타입를 따름, 배열이기 때문에 타입이 일치해야한다
# int -> float -> complex -> str
a = np.array([1,2,3])
print(a, type(a), a.dtype, a.shape, a.ndim, a.size)
# [1 2 3], <class 'numpy.ndarray'>, int32 (3,), 1차원, 3개
print(a[0]) # 인덱싱
print(a[1:3]) # 슬라이싱
print(a[-1])

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 2차원 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
b = np.array([[1,2,3,],[4,5,6]]) # 2차원
print(b, type(b), b.dtype, b.shape, b.ndim, b.size)
print(b[0]) # 인덱싱, 0행
print(b[1:3]) # 슬라이싱
print(b[-1]) # -1행
print(b[0,0], b[1,1]) # 0행 0열, 1행 1열
print(b[[0]]) # 0행

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 행렬 채우기(0,1,full) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
c = np.zeros((2,2)) # 0으로
print(c)

d = np.ones((1,2)) # 1로
print(d)

e = np.full((2,2), fill_value = 7) # 7로 전부 채우기
print(e)

f = np.eye(3) # 단위행렬 생성
print(f)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 난수 : 균등분포, 정규분포 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(np.random.rand(5), np.mean(np.random.rand(5))) # 균등분포 (균일하게)
print(np.random.randn(5), np.mean(np.random.randn(5))) # 정규분포 (평균을 기준으로 좌우 대칭)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 고정 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
np.random.seed(1)
print(np.random.randn(2, 3))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 1차원, 2차원, 3차원 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(np.random.randint(10, size = 6)) # 1차원
print(np.random.randint(10, size = (3, 4))) # 2차원
print(np.random.randint(10, size = (3, 4, 5))) # 3차원

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ list, np배열 비교 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(list(range(0, 10))) # list의 배열
print(np.arange(10)) # np의 배열

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 인덱싱, 슬라이싱 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
a = np.array([1, 2, 3, 4, 5])
print(a[1:5:2]) # 초기값:끝값:증감값

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[:]) # 모두
print(a[1:])
print(a[-1:]) # 마지막행
print(a[0], a[0][0], a[0, 0], a[[0]]) # 0행, 0행0열, 0행0열, 2차원 0행
# [1 2 3 4] 1 [[1 2 3 4]]
print(a[1:, 0:2]) # 1행에서 0행 1열

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ***서브 배열 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
b = a[:2, 1:3] # 1열에서 1행 2열
print(b)
# [[2 3]
#  [6 7]]

print(b[0,0])
print(b[0,1])
print()
b[0, 0] = 88
print(b)

print()
print(a)

print()
c = a[:2, 1:3].copy() # 배열 사본 복사
print(c)
c[0, 0] = 99
print()
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ [],() 순서o, {} 순서x, 차원의 이해 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
a = np.array([[1,2,3],[4,5,6],(7,8,9)]) 
# 안에 내용이 리스트[]나 튜플은 가능(), set{}는 안됨(순서가 없어서)
print(a.shape) # (3, 3)
r1 = a[1, :] # 인덱싱, 1차원 [4 5 6] (3,), 1차원은 요소수만
r2 = a[1:2, :] # 슬라이싱, 2차원 [[4 5 6]] (1, 3), 1행에서2행까지 ,2차원은 1행 3열
print(r1, r1.shape)
print(r2, r2.shape)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 인덱싱용 배열 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a.shape) # (4, 3)
print(a)
b = np.array([0,2,0,1]) # a 배열 인덱싱용 배열
print(b, b.shape) # [0 2 0 1] (4,)

print()
print(np.arange(4))
print(a[np.arange(4), b]) # 1행0열-2행2열-3행0열-4행1열 (열은 +1)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 참, 거짓 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
bool_idx = (a > 10)
print(bool_idx)

print(a[bool_idx]) # 참인 것만 나옴 [11 12]
print(a[a > 10])









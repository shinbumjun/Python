# 배열 연산
# tip : 더하기, 빼기, 곱하기, 나누기 연산
# tip : 내적 연산
# tip : Brcadcasting 연산
 
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64) # 실수로 만들고 싶을떄
print(x, x.dtype)
y = np.arange(5, 9).reshape((2, 2)) # 차원바꾸기 2행 2열
y = y.astype(np.float64)
print(y, y.dtype)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 연산하기 (더하기, 빼기, 곱하기, 나누기) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(x + y) # 더하기
print(np.add(x,y))

print()
print(x - y)
print(np.subtract(x, y)) # 빼기

print()
print(x * y)
print(np.multiply(x, y)) # 곱하기

print()
print(x / y)
print(np.divide(x, y)) # 나누기

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 벡터 내적 연산 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
v = np.array([9, 10]) # 1차원
w = np.array([11, 12]) # 1차원
print(v * w) # [ 99 120]

print()
print(v.dot(w)) # 벡터 내적 연산 v[0] * w[0] + v[1] * w[1] = 219
print(np.dot(v, w))
# 유사도

print()
print(x.dot(v)) # 2차원 1차원 
print(np.dot(x, v))
# x[0,0] * x[0] + x[0,1] * v[1]   x[1,0] * x[0] + x[1,1] * v[1]
# [29. 67.]


print()
print(x.dot(y)) # 2차원 2차원
print(np.dot(x, y))
# [[19. 22.]
#  [43. 50.]]

print()
print(x)
print(np.sum(x)) # 10.0
print(np.sum(x, axis = 0)) # 열에 대한 합 [4. 6.]
print(np.sum(x, axis = 1)) # 행에 대한 합 [3. 7.]

print()
print(x)
print(x.T) # 전치 : 행과 열을 바꿔준다
print(x.transpose())
print(x.swapaxes(0, 1))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ***Brcadcasting 연산 : 크기가 다른 배열 간 연산을 하면 작은 배열이 큰 배열의 크기에 자동으로 맞춰져 연산ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
x = np.arange(1, 10).reshape(3, 3) # 1차원 -> 2차원 
print(x)
y = np.array([1,2,3])
print(x + y)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ file io(저장, 읽기) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
datas = np.arange(0, 10, 2)
print(datas) # [0 2 4 6 8]

np.save('test1', datas) # binary 형식으로 저장 : save
np.savetxt('test2.txt', datas) # txt 형식으로 저장 : savetxt

mydatas = np.loadtxt('test2.txt') # 읽기 : loadtxt
print(mydatas) # [0. 2. 4. 6. 8.]






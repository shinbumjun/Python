'''
최소제곱해를 선형 행렬 방정식으로 얻기
회귀분석 이해하기
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3])
y = np.array([-1,0.2,0.5,2.1])

# plt.plot(x,y,'o',label='Original data', markersize=10)
# plt.grid()
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A) # 4 * 2

import numpy.linalg
w, b = np.linalg.lstsq(A,y)[0] # 최소자승법(내부적으로 편미분 사용)
print('w:', w, ',b:', b)
# w: 0.9599999999999999 ,b: -0.9899999999999993
# 단순선형회귀식 : y = 0.9599999999999999 * x + -0.9899999999999993

# x값 넣고 y값 알아내기
print('예측값 : ', 0.9599999999999999 * 0 + -0.9899999999999993)
print('예측값 : ', 0.9599999999999999 * 1 + -0.9899999999999993)
print('예측값 : ', 0.9599999999999999 * 2 + -0.9899999999999993)
print('예측값 : ', 0.9599999999999999 * 3 + -0.9899999999999993)

print('미지의 예측값 : ', 0.9599999999999999 * 10 + -0.9899999999999993)

plt.plot(x, y, 'o', label='Original data',markersize=10)
plt.plot(x, y*x + b, 'r', label='Fitted line')
plt.grid()
plt.legend()
plt.show()



















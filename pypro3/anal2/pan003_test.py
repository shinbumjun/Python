# Pandas의 DataFrame 관련 연습문제
# https://cafe.daum.net/flowlife/SBU0/10

from pandas import Series, DataFrame
import numpy as np

'''
pandas 문제 1)
  a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
     np.random.randn(9, 4)
     
  b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오

  c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
'''
df = DataFrame(np.random.randn(9, 4)) # 테이블 구성
df.columns = ['No1', 'No2', 'No3', 'No4'] # 칼럼에 이름주기
print(df)
print(df.mean(axis=1)) # 각 컬렴의 평균

# a = np.random.randn(9, 4)
# df = DataFrame(np.arange(36).reshape(9, 4), index=['1','2','3','4','5','6','7','8','9'], columns=['No1', 'No2', 'No3', 'No4'])
# print(df)

'''
pandas 문제 2)

numbers
a
10
b
20
c
30
d
40

a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.
b) c row의 값을 가져오시오.
c) a, d row들의 값을 가져오시오.
d) numbers의 합을 구하시오.
e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.  
'''
s1 = Series([10,20,30,40], index = ['a','b','c','d']) # Series 값, index 키
s1.columns = ['numbers'] # 칼럼에 이름주기
print(s1)

# a
# c row의 값
# a, d row들의 값
print(s1.sum(axis=0)) # 열의합 : 100
print(s1 * s1) # numbers의 값들을 각각 제곱
   
#s2 = DataFrame(s1, columns=['numbers','floats'], index = ['a','b','c','d']) # 칼럼 추가 f
#print(s2)



# 참고
# df = DataFrame(np.arange(4).reshape(4, 1), index=['a','b','c','d'], columns=['numbers']) # 테이블 구성
# print(df)
#    numbers
# a        0
# b        1
# c        2
# d        3  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
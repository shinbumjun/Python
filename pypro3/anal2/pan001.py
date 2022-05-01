'''
Pandas : 고수준의 자료 구조(Series, DataFrame)를 지원. 데이터 분석용 자료 관리를 위한 다양한 함수 제공
축약 연산, SQL 처리, 시계영 데이터 처리, 시각화 ...

tip : 타입이 일치
'''
import pandas as pd
from pandas import Series
import numpy as np

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ Pandas -> Series ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# Series : 일련의 데이터를 담을 수 있는 1차원 배열과 비슷한 자료구조를 가지며, 색인을 지원함

obj = Series([3, 7, -5, 4]) 
# list, tuple type 가능. TypeError:'set' type is unordered (set은 순서가 없어서 불가)
print(obj, type(obj))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 생성 시 색인을 지정 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
obj2 = Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd']) 
print(sum(obj2), obj2.sum(), np.sum(obj2)) # 합 구하기
print(obj2.values) # 중요 [3 7 -5 4]
print(obj2.index)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 인덱싱, 슬라이싱 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(obj2)
print(obj2[1]) # 7
print(obj2['b']) # 지정된 색인을 찾아서 값을 출력 : 7
print(obj2[['b']])

print(obj2[['a', 'b']]) # 인덱스명(값), 타입
print(obj2['a':'b'])

print(obj2[2]) # -5
print(obj2[1:4])
print(obj2[[2, 1]])
print(obj2 > 1)
print('a' in obj2) # a인 인덱스값이 있는지 True

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ dict type으로 Series 객체 생성 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
names = {'mouse':5000, 'keyboard':25000, 'monitor':'550000'}
print(names)
obj3 = Series(names) # Series으로 변수에 담기
print(obj3) # object타입

obj3.index = ['마우스', '키보드', '모니터'] # 인덱스명 바꾸기
print(obj3)

print(obj3['마우스']) # 마우스인 인덱스 값 출력

obj3.name = '상품가격' # Name: 상품가격 
print(obj3)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ [중요]DataFrame ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# DataFrame : 표 모양(2차원)의 자료구조로 여러 개의 칼럼(열)을 갖는다
from pandas import DataFrame
df = DataFrame(obj3) # DataFrame으로 변경
print(df, type(df)) # class 'pandas.core.frame.DataFrame'

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ Local, 데이터베이스, 파일, 웹 등에서 얻을수 있다 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
data = {
    'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
    'nai':[23, 25, 33, 30, 35],
}
print(data, type(data)) # dict 타입

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
frame = DataFrame(data) # DataFrame으로 변경
print(frame, type(frame))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(frame['irum'], type(frame['irum']))
print(frame.irum)

print(DataFrame(data, columns=['juso', 'irum','nai'])) # 칼럼 순서 변경

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 칼럼 추가 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
frame2 = DataFrame(data, columns=['irum', 'nai', 'juso', 'tel'], index = ['a','b','c','d','e']) # 칼럼 추가
# frame2.column = ['irum', 'nai', 'juso', 'tel']
# frame2.index = ['a','b','c','d','e']
print(frame2)

frame2['tel'] = "111-1111" # 모든 행에 적용
print(frame2)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 변수 : val(넣기) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
val = Series(['222-2222', '333-3333','444-4444'], index = ['b', 'c', 'e']) # 인덱스, 값
print(val)
frame2['tel'] = val # tel칼럼에 val내용을 넣음
print(frame2)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ transpose 전치 - 행열의 위치를 변경 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(frame2.T) # transpose 전치 - 행열의 위치를 변경

print(frame2.values)
print(frame2.values[0,1]) # 23
print(frame2.values[0:2]) # 행0에서 행1까지

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 변수 : frame3(삭제) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
frame3 = frame2.drop('d') # 행 삭제 axis=0
# frame3 = frame2.drop('d', axis=0)
print(frame3)

frame4 = frame2.drop('tel', axis=1) # 열 삭제 axis=1
print(frame4)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 변수 : frame2(오름차운, 내림차순), 순위 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(frame2) # 기본(오름차운)
print(frame2.sort_index(axis=0, ascending=False)) # 내림차순(행 단위)
print(frame2.sort_index(axis=1, ascending=True)) # 내림차순(열 단위)
print(frame2.rank(axis = 0)) # 순위

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 변수 : frame2(갯수) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(frame2['juso'].value_counts()) # 주소별 갯수


data = {
    'juso':['강남구 역삼동','중구 신당동','강남구 대치동'],
    'inwon':[23,25,15]
}
fr = DataFrame(data)
print(fr)

result1 = Series([ju.split()[0] for ju in fr.juso]) # 0번째
print(result1.values)
print(result1.value_counts())

result2 = Series([ju.split()[1]for ju in fr.juso])
print(result2)



















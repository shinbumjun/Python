'''
Pandas : 응용하면서 보기
'''
from pandas import Series, DataFrame
data = Series([1,3,2], index = (1,4,2))
print(data)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 변수 : data2(순서 재배치) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
data2 = data.reindex((1,2,4)) # 행 순서 재배치
print(data2)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 변수 : data3(대체) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
data3 = data2.reindex([0,1,2,3,4,5]) # 대응 값이 없는 인덱스는 결측값이 됨
print(data3)

data3 = data2.reindex([0,1,2,3,4,5], fill_value = 777) # 대응 값이 없는 인덱스는 777로 채워짐
print(data3)

data3 = data2.reindex([0,1,2,3,4,5], method = 'ffill') # NaN 앞 값으로 현재 NaN을 대체
data3 = data2.reindex([0,1,2,3,4,5], method = 'pad')
print(data3)

data3 = data2.reindex([0,1,2,3,4,5], method = 'bfill') # NaN 뒷 값으로 현재 NaN을 대체
data3 = data2.reindex([0,1,2,3,4,5], method = 'backfill')
print(data3)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 테이블 만들기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
import numpy as np
df = DataFrame(np.arange(12).reshape(4, 3), index=['1월','2월','3월','4월'], columns=['강남', '강북', '서초'])
print(df)
#     강남  강북  서초
# 1월   0   1   2
# 2월   3   4   5
# 3월   6   7   8
# 4월   9  10  11

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 조건에 따른 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(df['강남']) # 강남 열만 
print(df['강남'] > 3) # 강남 열에서 3초과만 True, False
print(df[df['강남'] > 3]) # 조건에 부합하는 

df[df < 3] = 0 # 3미만 값들은 0으로
print(df)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 슬라이싱 관련 메소드 : loc() 라벨 지원, iloc() 숫자 지원 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(df['강남'])
# 복수 인덱싱
print(df.loc['3월']) # 3월 행
print(df.loc['3월',]) # 3월 행
print(df.loc['3월', :]) # 3월 행

print(df.loc[:'3월']) # 3월 이하행 모든 열 출력
print(df.loc[:'3월',['서초']])

print()
print(df.iloc[2]) # 2행 출력
print(df.iloc[2, :]) # 2행 출력
print(df.iloc[:3]) # 3미만 행 출력
print()
print(df.iloc[:3, 2]) # 3미만 행, 2열 출력
print()
print(df.iloc[1:3, 1:3]) # 행(1행~2행), 열(1열~2열)
#     강북  서초
# 2월   4   5
# 3월   7   8

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ [중요]연산 (구조) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
s1 = Series([1,2,3], index = ['a','b','c']) # Series 값, index 키
s2 = Series([4,5,6,7], index = ['a','b','d','c'])
print(s1)
print(s2)

print(s1+s2) # 인덱스명 끼리 연산 -, *, /
print(s1.add(s2)) # # 인덱스명 끼리 연산 sub, mul, div

print()
df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('kbs'), index = ['서울','대전','부산'])
df2 = DataFrame(np.arange(12).reshape(4,3), columns=list('kbs'), index = ['서울','대전','제주','광주'])
print(df1)
print(df2)

print(df1 + df2) # -, *, / 
print(df1.add(df2, fill_value = 0)) # NaN은 0으로 채움 sub, mul, div





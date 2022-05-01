# 함수
from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[1.4, np.nan],[7, 4.5], [np.NaN, np.NAN], [0.5, -1]])
df.columns = ['one', 'two'] # 칼럼에 이름주기
print(df)

print(df.drop(1)) # 1(2)행 삭제
print(df.isnull()) # null값은 True 아닌값은 False
print(df.notnull()) # null값은 False 아닌값은 True
print(df.dropna()) # [중요]NaN이 있는 행 삭제

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ dropna 사용 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(df.dropna(how='any')) # 열 값 중 하나라도  NaN인 경우 행 삭제
print(df.dropna(how='all')) # 열 값 모두가 NaN인 경우 행 삭제

print(df.dropna(subset=['one'])) # 특정열 값 중 NaN인 경우 행 삭제
print(df.dropna(axis='rows')) # NaN이 포함된 행 삭제
print(df.dropna(axis='columns')) # NaN이 포함된 열 삭제

print(df.fillna(0)) # NaN을 0으로 채우기, 평균 또는 대표값으로 채울 수도 있다


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 합, 평균 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(df)
print(df.sum())
print(df.sum(axis=0)) # 열의 합

print(df.mean(axis=1)) # 행의 평균

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 합, 평균 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(df.max(axis=0))
print(df.idxmax())
print(df.describe()) # 요약 통계량
print(df.info())

words = Series(['봄','여름','봄'])
print(words.describe())
# words.info() # AttributeError: 'Series' object has no attribute 'info'

















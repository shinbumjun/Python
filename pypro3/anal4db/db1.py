# Local Database 연동 후 DataFrame으로 저장
import sqlite3

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 테이블 만들기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
sql = "create table if not exists mytab(product varchar(10), maker varchar(10), weight real, price integer)"

conn = sqlite3.connect(":memory:")
# conn = sqlite3.connect("testdb")
conn.execute(sql) # execute 실행하다
conn.commit() 

stmt = "insert into mytab values(?,?,?,?)" # 바인딩

data1 = ('신상1', '롯데리아', 45, 5000) # insert 데이터 넣기
conn.execute(stmt, data1) # 실행하다

data2 = ('신상2', '맥도날드', 55, 5500) # insert 데이터 넣기
conn.execute(stmt, data2) # 실행하다

cursor = conn.execute("select * from mytab")
rows = cursor.fetchall()
# cursor.fetchall()
# 이 메서드는 쿼리 결과 집합의 모든(또는 나머지 모든) 행을 가져오고 튜플 목록을 반환합니다. 
# 더 이상 사용 가능한 행이 없으면 빈 목록을 반환합니다.

for a in rows:
    print(a)
# ('신상1', '롯데리아', 45.0, 5000)
# ('신상2', '맥도날드', 55.0, 5500)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ DataFrame으로 출력 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
import pandas as pd
df1 = pd.DataFrame(rows, columns = ['product', 'maker', 'weight', 'price']) # 열 제목 
print(df1)
#   product maker  weight  price
# 0     신상1  롯데리아    45.0   5000
# 1     신상2  맥도날드    55.0   5500

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ html으로 출력 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
df2 = pd.read_sql("select * from mytab", conn)
# print(df2)

print(df2.to_html())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ DataFrame을 DB로 저장 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# 데이터 만들기
data = {
    'product':['연필','볼펜'], # 열이름, 행
    'maker':['모나미','모나미'],
    'weight':[1.5, 2.3],
    'price':[500, 1000]
}

frame = pd.DataFrame(data) # DataFrame 타입으로 만들기
print(frame)
#   product maker  weight  price
# 0      연필   모나미     1.5    500
# 1      볼펜   모나미     2.3   1000

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ append (추가) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
frame.to_sql("mytab", con=conn, if_exists='append', index=False)
df3 = pd.read_sql("select * from mytab", conn)
print(df3)
#      product maker  weight  price
# 0     신상1  롯데리아    45.0   5000
# 1     신상2  맥도날드    55.0   5500
# 2      연필   모나미     1.5    500
# 3      볼펜   모나미     2.3   1000

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ count ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(pd.read_sql("select count(*) as count from mytab", conn))
#    count
# 0      4






















'''
# Database 연동 프로그래밍
# 개인용 database : sqlite3 - 파이썬에 기본 모듈로 제공
'''

import sqlite3
print(sqlite3.sqlite_version) # 3.36.0

print()
# conn = sqlite3.connect('exam.db') # [중요]DB와 연결, 데이터베이스 만들기 (물리적으로 파일명 만들기)
conn = sqlite3.connect(':memory:') # 실험용 - ram에  생성

try:
    cur = conn.cursor() # [중요]SQL문 실행
    
    # cur.execute("""create table if not exists friends(name text, phone text, addr text)""")
    cur.execute("create table if not exists friends(name text, phone text, addr text)") # 테이블이 만들어짐
    # varchar(10), char(10) 차이점, test (게시판글쓰기)
    cur.execute("insert into friends values('홍길동', '111-1111', '서초1동')")
    cur.execute("insert into friends values(?,?,?)",('신기루','222-2222','서초2동'))
    
    inputData = ('신선한','333-2222','서초2동')
    cur.execute("insert into friends values(?,?,?)", inputData)
    
    conn.commit()
    
    cur.execute("select * from friends")
    # print(cur.fetchone()) # 한개만 읽기
    print(cur.fetchall()) # 여러개 읽기
    
    print()
    cur.execute("select name, addr, phone from friends")
    for r in cur:
        print(r[0], r[1], r[2])
    
except Exception as e:
    print('err : ', e)
    conn.rollback()
    
finally:
    cur.close() 
    conn.close()
    
































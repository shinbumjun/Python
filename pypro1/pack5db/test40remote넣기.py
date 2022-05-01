'''
원격 데이터 베이스 연동
'''
import MySQLdb

# Python 드라이버로 연결하기 예)
# import MySQLdb
# conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
# print(conn)
# conn.close

# dict타입
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}


try:
    conn = MySQLdb.connect(**config) # dict타입은 **로 받는다, 로컬이 아니라 리누트이기 때문에 구체적으로 작성
    cursor = conn.cursor()
    
#    print('insert ---') # 신상, 단가 ,값
    # isql = "insert into sangdata(code, sang, su, dan) values(10, '신상', 5, 5000)"
    # isql = "insert into sangdata(code, sang, su, dan) values(%s, %s, %s, %s)"
#    isql = "insert into sangdata values(%s, %s, %s, %s)"
#    sql_data= (10, '신상', 5, 5000) # 가독성을 위해서...
    # sql_data= 10, '신상', 5, 5000
#    cursor.execute(isql, sql_data) # tip : insert가 성공하면 1를 받는다
#    conn.commit() # commit을 해줘야한다
    # [추가]
    # 10 신상 5 5000 
    
#    print('update ---')
#    usql = "update sangdata set sang=%s,su=%s where code=%s"
#    sql_data = ('얼죽아', 30, 10) # 상품명, 수량, 코드
#    cou = cursor.execute(usql, sql_data)
#    print('cou : ', cou) # 성공하면 1 -> 2번째 실행시 0
#    conn.commit()
    # [수정]
    # 10 얼죽아 30 5000
    
    print('delete ---')
    input_code = '10'
    # dsql = "delete from sangdata where code=" + input_code # secure coding 가이드 라인에 위배
    
    # dsql = "delete from sangdata where code=%s"
    # cou = cursor.execute(dsql, (input_code,)) # 튜플
    dsql = "delete from sangdata where code='{0}'".format(input_code)
    
    cou = cursor.execute(dsql) # 성공하면 1
    conn.commit() #
    if cou > 0: # 리턴값을 받아서 사용할 수 있다
        print('삭제 성공')
    else:
        print('삭제 실패')
    # 삭제 성공 -> 두번째 삭제 실패  
    
    
    print()
    print('select ---')
    sql = "select code, sang, su, dan from sangdata" # *이것보단 칼럼명 구체적으로 작성하는게 좋음
    cursor.execute(sql)
    
    # 취향1
    for data in cursor.fetchall():
        # print(data)
        print('%s %s %s %s' %data)
        
        # [출력]
        # 1 장갑 3 10000
        # 2 벙어리장갑 2 12000
        # 3 가죽장갑 10 50000
        # 4 가죽점퍼 5 650000
        
    """    
    print()
    # 취향2
    for data in cursor:
        print(data[0], data[1], data[2], data[3])
        
    print()
    # 취향3    
    for(code, sang, su, dan) in cursor: # 칼럼명은 아니지만 가독성을 위해서...
        print(code, sang, su, dan)
     
    print()
    # 취향4   
    for(a, kbs, mbc, dan) in cursor:
        print(a, kbs, mbc, dan)    
    """  
    
except Exception as e: # MySQLdb.connections.Error : 에러메세지를 구체적으로
    print('err : ', e)
    conn.rollback() # commit이 아니면 rollback되어야 한다
finally:
    cursor.close()
    conn.close()

# 추가하고 한번더 실행할 경우 에러 발생 
# err :  (1062, "Duplicate entry '10' for key 'PRIMARY'") : db가 알려주는 에러











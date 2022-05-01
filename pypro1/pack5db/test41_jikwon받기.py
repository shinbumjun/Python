'''
# 키보드로 부서번호를 입력하여 해당 부서의 jikwon 자료 출력
'''
import MySQLdb

"""
# 별도의 파일을 만들고 읽어서 써야함, dict타입의 객체, 노출되면 안돼는 정보
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
"""

import pickle
with open('mydb.dat', 'rb') as obj:
    config = pickle.load(obj)

def chulbal(): # 출발
    try:
        # import...하여서 불러와서 사용
        conn = MySQLdb.connect(**config) # dict타입은 **로 받는다
        cursor = conn.cursor()
        
        buser_no = input('부서번호 입력:') # 부서번호 입력
        # sql문이 길어질 경우 이렇게 사용, 주석의 의미도 갖는다
        sql = """
            select jikwon_no, jikwon_name, buser_num, jikwon_pay
            from jikwon
            where buser_num={0}
        """.format(buser_no) # 키보드에 입력한 내용을 format을 이용하여 넣는다 
        # print(sql)
        
        """
        SELECT 명령을 위해 SQL 문을 따로 변수에 넣어주고 
        cursor.execute(sql) 을 사용해 SQL를 실행합니다.
        실행한 결과를 fetchall()을 이용해 받아옵니다.
        """
        cursor.execute(sql)
        
        """
        fetchall() : 모든 데이터를 한 번에 가져올 때 사용
        fetchone() : 한 번 호출에 하나의 행만 가져올 때 사용
        fetchmany(n) : n개만큼의 데이터를 가져올 때 사용
        
        """
        datas = cursor.fetchall() 
        # print(datas)
        # print(len(datas))
        if len(datas) == 0: # 부서가 없을 경우
            print(buser_no + '번 부서는 없어요')
            return
        
        for jikwon_no, jikwon_name, buser_num, jikwon_pay in datas: # 가독성을 위해
            print(jikwon_no, jikwon_name, buser_num, jikwon_pay)
            
        print('인원수 :' + str(len(datas))) # 인원수
    
    except Exception as e:
        print('err : ', e)
        
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    chulbal()














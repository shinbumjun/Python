'''
pandas 문제 5)

 MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.

     - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
     - DataFrame의 자료를 파일로 저장
     - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
     - 부서명, 직급으로 교차테이블을 작성(crosstab)
     - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
     - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
     
     [해설]
     inner join이용
     dataframe 타입으로 만들고 파일로 저장
     
     crosstab 이용
     
     직원별 담당 고객자료 : sql문 활용, 직원별 join(레프트조인, 라이트조인, 인어조인 정확히 알것)
     하나를 읽기
     
     부서명별 연봉의 평균 가로 막대
     
     데이터가 많을때는 산포도
     데이터가 없을때는 막대그래프
     
'''
import MySQLdb
import pickle
import numpy as np # 고속 연산, ndarray를 지원
import pandas as pd # 고수준의 자료 구조(Series, DataFrame)를 지원
import matplotlib.pyplot as plt # 그래프
import csv
plt.rc('font', family='malgun gothic') # 폰트설정 
plt.rcParams['axes.unicode_minus'] = False  # 음수 값 깨짐 방지

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ DB연결 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
try:
    with open('mydb.dat',mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결오류:',e)
    
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 문제풀이 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')    
try:
    conn = MySQLdb.connect(**config) 
    # config : 구성
    # ** : 파라미터 명을 같이 보낼 수 있다. config는 딕셔너리 형태로 전달된다.

    cursor = conn.cursor()
    sql = """
        select jikwon_no,jikwon_name,buser_name,jikwon_pay,jikwon_jik
        from jikwon inner join buser
        on buser_num = buser_no
    """
    # buser_num = buser_no인 사원의 ...출력
    # 하나의 테이블로 원하는 칼럼정보를 참조할 수 없는 경우 관련된 테이블을 논리적으로
    # 결합하여 원하는 칼럼 정보를 참조하는 방법을 JOIN 이라고 한다
    
    cursor.execute(sql)
    # cursor를 사용하면 결과가 일반적으로는 튜플 형태로 리턴이된다
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ DataFrame 타입 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    df = pd.DataFrame(cursor.fetchall(), columns=['사번','이름','부서명','연봉','직급'])
    # print(df) # 총30
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ DataFrame의 자료를 파일로 저장 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    # with open('jik_data2.csv',mode='w',encoding="UTF-8") as fobj:
    #     write = csv.writer(fobj)
    #     for r in cursor:
    #         write.writerow(r)


    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 부서명별 연봉의 합, 연봉의 최대/최소값을 출력 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    df = pd.read_sql(sql, conn)
    df.columns = ['번호','이름','부서','연봉','직급']
    print(df)
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 부서명별 연봉의 합 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(df.groupby(['부서'])['연봉'].sum())
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 부서명별 연봉의 최대값 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('부서명별 연봉의 최대값', df.groupby(['부서'])['연봉'].max())
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 부서명별 연봉의 최소값 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('부서명별 연봉의 최소값', df.groupby(['부서'])['연봉'].min())
    
    
    
    # 여기서부터
    
    
    
    # print('부서명별 연봉의 최소값 :',df.groupby(['부서'])['연봉'].mean())
# - 부서명, 직급으로 교차테이블을 작성(crosstab)
    ctab = pd.crosstab(df['부서'],df['직급'], margins=True)
    print(ctab)
    
# - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    print('df.index :', df.index)  # RangeIndex(start=0, stop=30, step=1)
    for i in range(1, len(df.index) - 1):
        sql2 = """
        select gogek_no,gogek_name,gogek_tel  
        from gogek inner join jikwon
        on gogek_damsano=jikwon_no
        where jikwon_no={}
        """.format(str(df.index[i]))
        #print(sql2)
        cursor.execute(sql2)
        result = cursor.fetchone()
        if result == None:
            print(df['이름'][i + 1], '담당고객 X')
        else:
            print(df['이름'][i + 1], '직원담당고객')
            df2 = pd.read_sql(sql2, conn)
            df2.columns = ['고객번호','고객명','고객전화']
            df2.set_index('고객번호', inplace = True)
            print(df2)
    
# - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    jik_ypay = df.groupby(['부서'])['연봉'].mean()
    print(jik_ypay, type(jik_ypay)) # Series

    plt.barh(range(len(jik_ypay)), jik_ypay,alpha = 0.5)
    plt.xlabel('연봉')
    plt.yticks([0,1,2,3], labels=['관리부', '영업부', '전산부', '총무부'])
    plt.ylabel('부서별')
    plt.show()

except Exception as e:
    print('처리오류:',e)
finally:
    cursor.close()
    conn.close()







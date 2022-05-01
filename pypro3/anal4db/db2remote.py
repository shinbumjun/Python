'''
원격DB(MariaDB)와 연동 처리 : DataFrame
'''
import MySQLdb # Python에서 MySQL 데이터베이스 서버에 연결하기 위한 인터페이스
import pickle # 텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장하는 것
import numpy as np # 고속 연산, ndarray를 지원
import pandas as pd # 고수준의 자료 구조(Series, DataFrame)를 지원
import matplotlib.pyplot as plt # 그래프
import csv
# from trio import _wait_for_object

plt.rc('font', family="malgun gothic") # 폰트설정

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ DB연결 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결 오류 : ', e)
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql) # cursor를 사용하면 결과가 일반적으로는 튜플 형태로 리턴이된다
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 출력 1 : console 출력 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    for (a,b,c,d,e,f) in cursor:
        print(a,b,c,d,e,f)
        # 1 홍길동 총무부 이사 남 9900
        # 2 한송이 영업부 부장 여 8800   
        # ...         
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 출력 2 : DataFrame ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')  
    df1 = pd.DataFrame(cursor.fetchall(), columns = ['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_jik', 'jikwon_gen', 'jikwon_pay'])
    print(df1.head(2))  
    #         jikwon_no jikwon_name buser_name jikwon_jik jikwon_gen  jikwon_pay
    # 0          1         홍길동        총무부         이사          남        9900
    # 1          2         한송이        영업부         부장          여        8800
        
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 출력 3 : csv file로 저장 (jik_data.csv 생성) - 인코딩(한글은 깨져서 보임) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')  
    with open('jik_data.csv', mode='w', encoding="UTF-8") as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r) # 저장
            
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ jik_data.csv(엑셀) 읽기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    df2 = pd.read_csv("jik_data.csv", header=None, names = ['번호', '이름', '부서', '직급', '성별', '연봉']) # 읽기    
    print(df2.head(2))    
    #    번호   이름   부서  직급 성별    연봉
    # 0   1  홍길동  총무부  이사  남  9900
    # 1   2  한송이  영업부  부장  여  8800
    
    df = pd.read_sql(sql, conn)
    df.columns = ['번호', '이름', '부서', '직급', '성별', '연봉'] # 열이름
    print(df.head(3)) 
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ DataFrame에 저장된 자료로 기술통계, 추론통계 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(df[:3]) # 3행 출력
    print(df[:-27]) # 뒤에 27개를 제외, 3행 출력
    
    print('건수:', len(df)) # df 문자열 : 30
    print('건수:', df['이름'].count()) # 이름의 갯수 : 30 
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 직급별 인원수 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('직급별 인원수 : ', df['직급'].value_counts())
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 부서별 인원수 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('부서별 인원수 : ', df['부서'].value_counts())
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 연봉 평균 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('연봉 평균 : ', df.loc[:, '연봉'].sum() / len(df)) # 연봉 평균 : 5305.0
    print('연봉 평균 : ', df.loc[:, '연봉'].mean()) # 연봉 평균 : 5305.0
    print('연봉 표준편차 : ', df.loc[:, '연봉'].std()) # 연봉 표준편차 : 2069.6222377275885
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 연봉 전체 설명 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(df.loc[:, '연봉'].describe())
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 연봉 8000이상 출력 (조건) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(df.loc[df['연봉'] >= 8000])
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 성별에 따른 직급 출력 (조건) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    ctab = pd.crosstab(df['성별'], df['직급'], margins=True)
    print(ctab)
        
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 그룹으로(행) 묶인 성별, 직급 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(df.groupby(['성별', '직급'])['이름'].count()) 
                                    # Name: 이름, dtype: int64
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ pivot_table 연봉, 성별-직급, 피벗테이블 평균 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(df.pivot_table(['연봉'], index=['성별', '직급'], aggfunc = np.mean))    
        
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 시각화 : pie ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')   
    jik_ypay = df.groupby(['직급'])['연봉'].mean() # 직급별 연봉의 평균
    print(jik_ypay, type(jik_ypay))
    # 직급
    # 과장    7200.000000
    # 대리    5064.285714
    # 부장    8466.666667
    # 사원    3476.923077
    # 이사    9900.000000
    # Name: 연봉, dtype: float64 <class 'pandas.core.series.Series'>
    
    print(jik_ypay.index)
    # Index(['과장', '대리', '부장', '사원', '이사'], dtype='object', name='직급')
    
    print(jik_ypay.values)
    # [7200.         5064.28571429 8466.66666667 3476.92307692 9900.        ]
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ # 적은 양의 데이터를 사용할때 그래프 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')  
    plt.pie(x=jik_ypay, explode=(0.2,0,0,0.3,0), labels=jik_ypay.index,
            shadow = True, labeldistance = 0.7, counterclock=False)
    plt.show()
        
except Exception as e:    
    print('처리 오류 : ', e)
finally:
    cursor.close()    
    

    
    
    
    
    
    
    
    
    
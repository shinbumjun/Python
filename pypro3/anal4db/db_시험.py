# 15번 정답 
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결오류:',e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
    select buser_name, jikwon_gen, jikwon_pay
    from jikwon inner join buser on buser_no=buser_num
    """
    cursor.execute(sql)
    
    df1 = pd.DataFrame(cursor.fetchall(), columns=['부서명','성별','연봉'])
    print(df1.head(2))
    # 부서명 성별    연봉
    # 0  총무부  남  9900
    # 1  영업부  여  8800
    
    jik_ypay = df1.groupby(['성별'])['연봉'].mean()
    print(jik_ypay)
    # 성별
    # 남    5980.0
    # 여    4630.0
    # Name: 연봉, dtype: float64
    
    ctab = pd.crosstab(df1['부서명'],df1['성별'])
    print(ctab)
    # 성별   남  여
    # 부서명      
    # 관리부  2  2
    # 영업부  4  8
    # 전산부  3  4
    # 총무부  6  1
    
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(range(len(jik_ypay)), jik_ypay, color = ['black', 'red'])
    plt.xlabel('gender')
    plt.ylabel('pay')
    plt.xticks([0,1],labels=['Male', 'Female'])
    plt.show()
    # 그래프
    
except Exception as e:
    print('처리오류:',e)
finally:
    cursor.close()
    conn.close()


'''
Created on 2022. 4. 25.

@author: 82103
'''
'''
import pandas as pd
data = {
    'product':['아메리카노','카페라떼','카페모카'],
    'maker':['스벅','이디아','엔젤리너스'],
    'price':[5000,5500,6000]
}

df = pd.DataFrame(data)
'''
'''
# 2번
import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic.head())
#print(titanic.groupby(['sex'])['female'].max())
'''
'''
from pandas import DataFrame
frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']},
                  index=['a','b', 'c','d'])
print(frame)

print('실행결과 1:', DataFrame([a,b,c,d,])
# f= pd.DataFrame([a,b,c,d,])
'''
'''
import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic.head())

print(titanic.groupby(['sex'])['survived'].mean())

# 그룹으로 sex 묶고 survived의 mean (평균값)
'''
'''
from pandas import Series, DataFrame

data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
df = DataFrame(data)
results = Series([x.split()[0] for x in df.juso])

print(results)
'''
'''
import numpy as np

x = [1,2,3,4,5]
y = np.reshape([1,2,3], (3,1))

print(x + y)
'''

      
      
      
      
      
      
      
      
      
      
      
      
      
      









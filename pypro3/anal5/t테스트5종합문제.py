print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('[two-sample t 검정 : 문제1]') 

import numpy as np
from numpy import average # 평균
import scipy.stats as stats

# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.
# blue : 70 68 82 78 72 68 67 68 88 60 80
# red : 60 65 55 58 67 59 61 68 77 66 66

# 귀무 : 포장지 색상에 따른 제품의 매출액에 차이가 존재하지 않는다
# 대립 : 포장지 색상에 따른 제품의 매출액에 차이가 존재한다

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

print()
print('***** 평균')
print(average(blue), ' ', average(red)) # 72 vs 63
print()
print('***** 정규성 (0.05보다 크면 만족)') # 중앙집중 그래프가 맞는지?
print(stats.shapiro(blue)) # pvalue=0.51023 만족
print(stats.shapiro(red)) # pvalue=0.53479 만족
print()
print('***** 등분산성 확인 (0.05 보다 크면 만족) ') # 두개의 집단의 확률이 동일해야한다 등분산
print(stats.levene(blue, red).pvalue) # 0.43916 만족
print()
print('***** 귀무가설 채택 or 귀무가설 기각')
data1 = stats.ttest_ind(blue, red)
print(data1) # pvalue=0.00831 < 0.05 이므로 귀무가설 기각


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('[two-sample t 검정 : 문제2]') 
 
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
# 남자 : 0.9 2.2 1.6 2.8 4.2 3.7 2.6 2.9 3.3 1.2 3.2 2.7 3.8 4.5 4 2.2 0.8 0.5 0.3 5.3 5.7 2.3 9.8
# 여자 : 1.4 2.7 2.1 1.8 3.3 3.2 1.6 1.9 2.3 2.5 2.3 1.4 2.6 3.5 2.1 6.6 7.7 8.8 6.6 6.4

# 귀무 : 남여 혈관 내의 콜레스테롤 양에 차이가 없다
# 대립 : 남여 혈관 내의 콜레스테롤 양에 차이가 있다

m = [0.9,2.2,1.6,2.8,4.2,3.7,2.6,2.9,3.3,1.2,3.2,2.7,3.8,4.5,4,2.2,0.8,0.5,0.3,5.3,5.7,2.3,9.8]
g = [1.4,2.7,2.1,1.8,3.3,3.2,1.6,1.9,2.3,2.5,2.3,1.4,2.6,3.5,2.1,6.6,7.7,8.8,6.6,6.4]

data2 = stats.ttest_ind(m, g)
print(data2) # pvalue=0.48082 > 0.05 귀무가설 채택

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('[two-sample t 검정 : 문제3]')

# DB(mysql)에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.

# 귀무 : 총무부, 영업부 직원의 연봉의 평균에 차이가 없다
# 대립 : 총무부, 영업부 직원의 연봉의 평균에 차이가 있다

import numpy as np
from scipy import stats
import pandas as pd
import MySQLdb
import pickle

try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('읽기 오류 : ', e)
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select buser_name,jikwon_pay 
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql)
    
    df = pd.DataFrame(cursor.fetchall(), 
                       columns = ['부서명','연봉'])
    #print(df.groupby(['부서명']).mean(['연봉']))
    df.groupby(['부서명']).apply(lambda x: x.fillna(x.groupby(['부서명']).mean())) # 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.(?)
    print(df)

    # 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
    # 귀무 : 총무부, 영업부 직원의 연봉의 평균에 차이가 없다.
    # 대립 : 총무부, 영업부 직원의 연봉의 평균에 차이가 있다.
    
    buser1 = df[df['부서명']=='총무부'].연봉
    buser2 = df[df['부서명']=='영업부'].연봉
    print(np.average(buser1),' ',np.average(buser2)) # 5414.285714285715   4908.333333333333

    # 정규성 검증
    print(stats.shapiro(buser1).pvalue) # 0.02604489028453827 < 0.05 불만족
    print(stats.shapiro(buser2).pvalue) # 0.02560843899846077 < 0.05 불만족

    # 등분산성 검증
    print(stats.levene(buser1, buser2).pvalue) # 0.915044305043978 > 0.05 만족
        
    two_sample = stats.mannwhitneyu(buser1, buser2)

    print(two_sample) # MannwhitneyuResult(statistic=51.0, pvalue=0.47213346080125185)
    # pvalue=0.4721 > 0.05 귀무가설 채택.
    # 총무부, 영업부 직원의 연봉의 평균에 차이가 없다.
except Exception as e:
    print('오류 : ', e)
finally:
    cursor.close()
    conn.close()

print()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('[대응표본 t 검정 : 문제4]')
# 집단이 하나면 등분산성 사용x

# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.

# 중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
# 기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95

# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

exam1 = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
exam2 = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(stats.shapiro(exam1).pvalue)  # 0.3681465 > 0.05
print(stats.shapiro(exam2).pvalue)  # 0.1930028 > 0.05
print(np.mean(exam1), ' ', np.mean(exam2))  # 74.16   81.66
print(stats.ttest_rel(exam1, exam2))
# Ttest_relResult(statistic=-2.6281127723493993, pvalue=0.023486192540203194)
# 해석 : pvalue=0.023486192540203194 < 0.05 귀무가설 기각.
# 학업능력이 변화했다.





# 1. numpy
# tip : 합 -> 평균 -> 분산 -> 표준편차 구하기

'''
numpy : 고속 연산, ndarray를 지원
# 데이터 분석 관련 모듈 전체 생태계의 핵심을 이루고 있기에 잘 다룰 줄 알아야 한다

평균, 분산, 표준편차 구하기 (모집단 / 표본 통계량)
'''
# grades = [1, 3, -2, 4] # 변량(변수, 확률값, 관측값)
grades = [1, 2, 3, 4]

# 1. 숫자 나열
def show_grades(grades):
    for g in grades:
        print(g, end = ' ')

show_grades(grades) # 1 3 -2 4 

# 2. 합 구하기
def grades_sum(grades):
    tot = 0 # 지역변수
    for g in grades:
        tot += g
    return tot

print()
print('합은', grades_sum(grades)) # 합은 6

# 3. 평균 구하기
def grades_avg(grades):
    tot = grades_sum(grades)
    ave = tot / len(grades)
    return ave
print('평균은 ', grades_avg(grades)) # 평균은 1.5

# 4. 분산 구하기
def grades_variance(grades):
    ave = grades_avg(grades) # 평균
    vari = 0
    for su in grades:
        vari += (su - ave) ** 2
    return vari / len(grades) # 모집단으로 계산(python) *
    # return vari / (len(grades) -1) # 표본지단으로 계산(R)
print('분산은 ', grades_variance(grades)) # 분산은  5.25

# 5. 표준편차 구하기
import math
def grades_std(grades):
    # return grades_variance(grades) ** 0.5
    return math.sqrt(grades_variance(grades))
print('표준편차는 ', grades_std(grades)) # 표준편차는  2.29128784747792

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# 5. numpy로 계산
import numpy as np # 별명주기
print('합은 ', np.sum(grades)) # 합은 6
# print('평균은 ', np.average(grades)) # 평균은 1.5
print('평균운 ', np.mean(grades)) # 평균은 1.5
print('분산은 ', np.var(grades)) # 분산은 5.25
print('표준편차는 ', np.std(grades)) # 표준편차는 2.29128784747792






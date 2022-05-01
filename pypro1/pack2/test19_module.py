'''
Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리한다.
파이썬은 모듈 단위로 파일을 저장한다.
모듈의 멤버 : 변수, 실행문(명령), 함수, 클래스
main module 확인 : __name__ == '__main__'

[참고]
1. 표준 모듈(파이썬을 깔면 기본)

2. 사용자 정의 모듈

3. 제 3자 모듈(전문가-서브 party)
1번째 다운 방법 (직접 다운 -> C:\\anaconda3\\lib\\site-packages(여기에 밀어 넣어준다))
2번째 다운 방법 (pip, conda install(자바에선 maven))

import : 모듈을 사용하기 위해
라이브러리 : 여러 모듈
pyd : 실행 라이브러리 파일

'''
# 내장된 모듈(표준 모듈)
print('뭔가를 하다가...')

# sys.전역변수 사용
import sys
print(sys.path) 

# sys.exit() # 프로그램 강제종료

print()
import math # 수학과 관련 -> 나중에는 ***넘파이할 예정
print(math.pi) # 3.141592653589793
print(math.sin(math.radians(30))) # sin 30도 값 : 0.49999999999999994

print()
import calendar # 달력
calendar.setfirstweekday(6) # 0 ~ 6
calendar.prmonth(2022, 3) # 달력이 나옴 

print(dir(calendar))

print()
import time # 시간
print(time.localtime())
# print('start...')
# time.sleep(3) # 지연시간 3초
# print('finish')

print()
import os
# os.mkdir(path, mode, dir_fd=None) # 할 예정
print(os.getcwd()) # 현재 작업 경로

print()
import random # 난수 사용, 첫번째 사용 방법 
print(random.random())
print(random.randint(1, 10))

from random import randint # 바로 randint 사용할 수 있음, 두번째 사용 방법 
print(randint(1, 10)) # 난수인 정수

from random import * # 메모리 소요가 있기 때문에 권장하지 않음, 세번째 사용 방법 
print(random())
print(dir())
print('프로그램 종료')

























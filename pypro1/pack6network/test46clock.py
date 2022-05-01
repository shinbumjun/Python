'''
thread를 이용한 날짜 및 시간 출력

그래프를 배운다면 나중에 시계도 만들수 있다
'''
import time
now = time.localtime()
print(now.tm_year, now.tm_mon, now.tm_mday) # 2022 4 5

# print(now)
# time.struct_time(tm_year=2022, tm_mon=4, tm_mday=5, tm_hour=12, tm_min=58, tm_sec=9, tm_wday=1, tm_yday=95, tm_isdst=0)

import threading

def calendar_show():
    now = time.localtime()
    print('현재는 {0}년 {1}월 {2}일 {3}시 {4}분 {5}초'.format(now.tm_year, now.tm_mon, now.tm_mday,
                                                     now.tm_hour, now.tm_min, now.tm_sec) ) # 년 월 일 시 분 초

# calendar_show()

def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 9:break # 9분이 되면 종료
        
        calendar_show()
        time.sleep(1) # 1초에 한번씩

th = threading.Thread(target = myRun) # 함수의 이름만
th.start()
th.join()

print('프로그램 종료')















'''
자원을 공유하면서 충돌이 일어날수도 있다
'''
import threading, time
from threading import Thread, Condition


g_count = 0 # 전역변수는 자동으로 스레드의 공유자원이 됨 
lock = Condition() # 스레드 공유자원 접근에 제한을 강제하기 의한 잠금객체

def threadCount(id, count):
    global g_count
    
    for i in range(count):
        lock.acquire() # 알아두기1) 특정 스레드가 공유자원을 수행하는동안 락을 건다
        print('id %s==>count: %s, g_count: %s'%(id, i, g_count))
        g_count += 1
        lock.release() # 알아두기2) 락을 풀어준다
        
for i in range(1, 6): # 5개의 스레드
    Thread(target = threadCount, args = (i, 5)).start() # 아규먼트

time.sleep(1) # join()없이 지연시간을 줘서 끝나게함

print('최종 g_count : ', g_count)
print('bye')


















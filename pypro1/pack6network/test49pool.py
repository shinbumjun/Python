'''
# thread는 GIL이라는 메커니즘 때문에 완전한 멀티 프로세싱 불가.
# 멀티 프로세싱을 위한 Pool, Process 클래스를 별도 지원

# Pool 클래스 (병렬처리)
총 작업 시간이 덜 걸린다

시간을 절약하고 싶으면 스레드대신 Pool를 사용하라 !!!
'''
from multiprocessing import Pool
import time
import os

def pool_func(arg):
    print('값', arg, '에 대한 pid:', os.getpid()) # 현재 실행되는 process id를 출력한다
    time.sleep(1) # 1초 뒤에, 너무 빠른 처리가 되지 않도록 편의상 약간의 지연 시간을 준다 
    return arg + 10 # 매개변수 값에 10을 더해 반환한다

# pool_func(3) # 결괏값 3에 대한 pid: 57. 실행 후 아래 처리에 방해되므로 주석 처리하자.

if __name__ == '__main__':
    startTime = int(time.time()) # 시작 시간, 처리 시작 시간 체크용
    
    # 방법 1 : Pool 객체를 사용하지 않은 일반적인 방법으로 함수 호출 
#    for i in range(10): # 10회 반복
#        print(pool_func(i))      
#    endTime = int(time.time()) # 끝나는 시간, 처리 종료 시간 기억
#    print('총 작업 시간: ', (endTime - startTime))


    # 방법 2 : Pool 객체를 사용해서 함수 호출, 멀티 태스킹이 가능한 Pool 객체로 함수를 호출하기
    startTime = int(time.time())
    
    po = Pool(processes = 3) # 프로세스의 갯수는 3 ~ 5를 권장, 프로세스 개수를 인자로 주고 함수 호출
    print(po.map(pool_func, range(10))) # 함수와 인자 값을 매핑하면서 처리 10회 반복
    
    endTime = int(time.time()) # 처리 종료 시간 기억
    print('총 작업 시간 : ', (endTime - startTime))





















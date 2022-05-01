'''
process thread 차이점 알고있기 !!!

Thread
process는 실행가능한 파일을 말한다. 프로세스는 현재 실행 중인 프로그램은 의미하면 tesk라고도 부른다

process의 작은 실행 단위를 thread라고 한다. 
thread 기법을 이용하면 여러개의 thread를 통해 여러개의 작업을 할 수 있다

multi thread에 의한 multi tasking이 가능함
'''
import threading, time

def run(id): # Thread를 사용하기 위해서
    for i in range(1, 11): # 1부터 10까지
        print('id:{}-->{}'.format(id, i))
        time.sleep(0.5) # 0.5초 뒤에 실행
        
# 1) thread x
# run('일') # 요청된 일이 전부 끝나야 
# run('이') # 이가 실행된다

# 2) thread o
th1 = threading.Thread(target = run, args = ('일',)) # Thread 생성자를 부르면서 값을 줌 : 객체 생성
th2 = threading.Thread(target = run, args = ('이',))
th1.start() # 스레드 수행됨 (랜덤하게)
th2.start() # 스레드 수행됨 (랜덤하게)

th1.join() # 메인스레드의 실행을 대기 시킬수 있다
th2.join() # 메인스레드의 실행을 대기 시킬수 있다

print('프로그램 종료') # 먼저 실행됨 
# 모든 스레드가 종료가 되어야 프로세스가 종료가됨











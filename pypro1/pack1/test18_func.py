'''
재귀함수(recursive functiontion) : 함수가 자기 자신을 호출
반복처리를 한다는 말(for, while문)

[공부]
변수, 명령, 함수, 클래스

패키지(파일 저장소) 안에 모듈
변수, 명령, 함수, 클래스 = 모듈 
파이썬은 모듈(파일)형태로 저장 및 실행

1. 표준 모듈(파이썬을 깔면 기본)
2. 사용자 정의 모듈
3. 제 3자 모듈(전문가-서브 party)*
- 직접 다운 site-packages(여기에 밀어넣어 준다)
- pip, conda install(자바에선 maven)

라이브러리를 다운 받아서 사용
모바일 프로그램을 제외하고 거의 모든것을 다할 수 있다

자바보단 install 많이 할 예정...

*파이썬, R은 버젼이 맞지 않으면 실행이 안된다!
모듈공부 시작~
'''
print('5 카운트')
def countDown(n): # 매개변수n
    if n == 0:
        print('완료')
    else:
        print(n, end = ' ')
        countDown(n-1) # 함수가 자신을 호출
        
countDown(5)    

print()
print('10까지의 합')
def tot(n):
    if n == 1:
        print('탈출')
        return True
    return n + tot(n-1)

res = tot(10)
print('10까지의 합은 ', res)

print()
# factorial(계승) : 1부터 어떤 양의 정수 n까지의 정수를 모두 곱한 것. n!, 5! = 5*4*3*2*1
# 서로 다른 n개를 나열하는 것 
def facFunc(a):
    if a == 1:
        return 1   
    print(a)
    return a * facFunc(a-1)
print('5!:', facFunc(5))
print('종료')










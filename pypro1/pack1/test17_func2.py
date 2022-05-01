'''
https://cafe.daum.net/flowlife/RUrO/40 : 함수 처리 문제 풀기

연습문제) 키보드를 통해 직원 자료를 입력받아 가공 후 출력하기 함수를 두 개 작성

  datas = inputfunc() : 키보드로 값을 입력 받아 datas 변수에 담는 역할
                        while True: 문으로 무한루핑하며, 계속입력할까요?n이 될 때까지 자료를 입력받는다.
  processfunc(datas) : datas에 기억된 내용을 출력한다.


처리 조건 : 
        급여액은 기본급 + 근속수당 
        수령액은 급여액 – 공제액
        
 근무년수에 대한 수당표       
 .
 .
 .       
        
tip : 연도
import time 
print(time.localtime())
'''
def inputfunc():
    while True:
        
        print('사번, 이름, 기본급, 입사년도를 입력하세요 : ')
        data = list(input().splis())
        processfunc(data)
            
        yn = input('계속 하시겠습니까? y/n : ')
        
        tmp = 0
        if yn == 'y':
            tmp += 1
            continue
        else:
             break

 # datas = inputfunc()

entry = int(input("직원의 근무년수를 입력하세요 : "))

while True:
    if entry <= 3:
        money = 150000
        
    elif entry <= 8:
        money = 450000
        
    elif entry > 9:
        money = 1000000
        
    print(str(money) + '원')
    break


def processfunc(datas):
    
    return processfunc(datas)
















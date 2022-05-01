'''
함수 장식자 (function decorator) : meta 기능이 있음
장식자는 또 다른 함수를 감싼 함수다.

@이게 나오면 당황하지 말자
'''
def make2(fn):
    return lambda:'안녕 '+ fn() # fn은 반가워 홍길동

def make1(fn):
    return lambda:'반가워 '+ fn() # fn은 홍길동

def hello():
    return '홍길동'

hi = make2(make1(hello)) # 안녕 반가워 홍길동을 리턴해주는 객체의 주소를 hi가 받음 (주소를 치환)
print(hi()) # 안녕 반가워 홍길동

### 값보단 주소를 보고 이해하라 ###

print()
print('make2(make1(hell2)) 동일함')
@make2
@make1
def hello2():
    return '고길동'
print(hello2()) # 안녕 반가워 고길동

print('------')
hi2 = hello2() # 실행 결과를 치환한것
print(hi2) # 안녕 반가워 고길동
hi3 =hello2 # 주소를 치환한것
print(hi3) # <function make2.<locals>.<lambda> at 0x000001AFBC3ABCA0>

# https://cafe.daum.net/flowlife/RUrO/40 연습문제 풀어보기














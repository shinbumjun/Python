'''
변수의 생존 범위 (scope rule) : 전역변수, 지역변수
접근 우선 순서 : local(지역) > Enclosing function > Gloval(전역)
'''
print('--전역변수--')
player = '전국대표' # 전역변수 : 현재 모듈의 어디서든 공유가 가능
print(player) # 전국대표

print()
print('--지역변수--')
def funcSoccer():
    name = '신선해' # 지역변수 : 현재 함수 내에서만 유효
    player = '지역대표'
    print(name, player) # 신선해 지역대표
    
funcSoccer()
# print(name) # NameError: name 'name' is not defined

print()
print(player) # 전국대표

print()
print('----- *이해하기 -----')
a = 10; b = 20; c = 30 # 글로벌
print('1) a:{} b:{} c:{}'.format(a, b, c)) # 1) a:10 b:20 c:30

def foo():
    a = 40 # foo 함수 수준
    b = 50
    def bar():
        # c = 60
        global c # 전역변수 수준
        nonlocal b # foo 함수 수준의 변수
        print('2) a:{} b:{} c:{}'.format(a, b, c)) # 2) a:40 b:50 c:30
        
        # 지역변수(값을 할당받지 못함) : 문법에는 이상이 없지만 오류 : 실행 도중에 떨어진 에러 runtime 에러
        # UnboundLocalError: local variable 'c' referenced before assignment
        c = 60 
        b = 70
        
    bar() # 빠져나오기
    print('3) a:{} b:{} c:{}'.format(a, b, c)) # 3) a:40 b:70 c:60

foo() # 빠져나오기
print('처리 후) a:{} b:{} c:{}'.format(a, b, c)) # 처리 후) a:10 b:20 c:60

print()
print('----- 참고 (변수의 이름은 다르게 하는게 좋지만 공부를 하기 위해 똑같이 줘본다)-----')
g = 1 # 여기와 (전역)
def func():
    global g # 전역인지 지역인지 명활하게 지정하는게 좋음
    
    # g = 2
    # a = g # [2, 2]
    
    a = g
    g = 2 # 여기는 다른 g이다 (지역)
    return [a, g]
print(func()) # [1, 2]







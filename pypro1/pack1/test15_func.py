'''
**********중요**********
# 함수에 나오는 closure
closure : scope에 제약을 받지 않는 변수들을 포함하고 있는 코드 블럭이다
내부함수의 멤버를 함수 밖에서 참조가 가능. 내부함수의 주소를 반환해 사용.

데이터 분석 
(통계학) 오차가 있는 형태, 확률
y = ax + b
a : 기울기
b : 절편
'''
# from astropy.units import count
# from sympy.physics.units import amount
def funcTimes(a, b):
    c = a * b
    return c

print(funcTimes(2, 3)) # 6

kbs = funcTimes(2, 3) # 실행 결과를 치환 
print(kbs) # 6

kbs = funcTimes # 주소를 치환한것
print(kbs) # <function funcTimes at 0x000002AE7DE500D0>
print(kbs(2, 3)) # 6

print(id(kbs), id(funcTimes)) # 같은 객체를 참조하고 있다, 2137294307536

del funcTimes
# print(funcTimes(2, 3))
print(kbs(2, 3))

mbc = sbs = kbs
print(mbc(2, 3))
print(sbs(2, 3))
print(kbs(2, 3))

print()
print('--클로저를 사용하지 않은 경우--')
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())
out()
# print(count) # 

print()
print('--클로저를 사용한 경우--') # 함수 내부에 있는 
def outer():
    count = 0
    def inner(): 
        nonlocal count
        count += 1
        return count
    return inner # <== 요거를 클로저 : 내부함수의 주소를 반환, 내부함수의 주소를 리턴

var1 = outer() # outer를 이용해서 내부함수에 있는 주소를 var1이 가진다 *****
print(var1) # <function outer.<locals>.inner at 0x000002D89DC84310>
print(var1()) # 1
print(var1()) # 2

imsi = var1()
print(imsi) # 3

print()
var2 = outer()
print(var2()) # 1
print(var2()) # 2
print(id(var1), id(var2), type(var1), type(var2)) # 같은 함수이지만 다른 객체이다

# 다시한번 보기
print()
print('수량 * 단가 * 세금을 출력하는 함수')
# outer2는 inner2를 만들기 위한 도구
def outer2(tax): # tax는 지역변수 : 함수 안에서 선언
    def inner2(su, dan): # 수량과 단과
        amount = su * dan * tax # inner2가 tax를 참조할 수 있음
        return amount
    return inner2 # 클로저 사용

# 다시한번 보기
# 1분기에는 수량 * 단가에 대해 tax가 0.1이 부과
print('------')
q1 = outer2(0.1) # outer2를 사용해서 inner2의 객체 만듬
result1 = q1(5, 50000)
print('result1 :', result1) # 25000.0

result2 = q1(2, 10000)
print('result2 :', result2) # 2000.0

print('------')
q2 = outer2(0.05) # outer2를 사용해서 inner2의 객체 만듬
result3 = q2(5, 50000)
print('result3 :', result3) # 2000.0

result4 = q2(2, 10000)
print('result4 :', result4) # 1000.0
























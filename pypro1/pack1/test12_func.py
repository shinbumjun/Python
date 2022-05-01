'''
함수 작성
'''
# from conda.cli.common import arg2spec
a = 1
b = a + 1
# 어쩌구 저쩌구 하다가 모듈의 멤버로 함수 선언

# 함수이름은 내 마음
def DoFunc1():
    print('DoFunc1 수행')

c = b + 20

# 함수 호출
DoFunc1() # 함수 호출

# 딴 짓 하다가...
res = DoFunc1() # 함수 호출
print(res) # None : 함수는 리턴하지 않으면 None
print(DoFunc1())

print()
print('함수도 객체이다 - 함수에 ()를 줘야 실행이된다')
print(DoFunc1) # <function DoFunc1 at 0x00000171499000D0> : 객체
print(id(DoFunc1)) # 1673261335024 : 주소
print(id(print)) # 1360286332544
print(id(sum)) # 1397960488976
print(id(c)) # 1397956504528

print()
print('주소를 치환')
d = c # 주소를 치환
DoFunc2 = DoFunc1 
DoFunc2() # DoFunc1 수행
print('함수는 선언 후 사용')

print()
print('--공부하기 1 (값 넣기)--')
def doFunc3(arg1, arg2): # 매개변수 : 가인수(파라미터)
    res = arg1 + arg2
    # return res
    if res % 2 == 1:
        return # 홀수면 None
    else:
        return res # 짝수면 값

print('결과는', doFunc3(10, 20)) # 실인수(아규먼트)

aa = doFunc3(10, 20) # 받아도된다
print('결과는', aa)

print()
print('--공부하기 2 (함수로 함수를 부르기 - 삼각형의 면적구하기)--')
def area_tri(a, b):
    c = a * b / 2
    area_print(c)
    
def area_print(c):
    print('삼각형의 면적은 ' + str(c))
    
area_tri(5, 6)    

print()
print('--*공부하기 3 (함수안에 함수를 사용하기 - inner class생각)--')
def func1():
    print('func1 멤버 처리')
    def func2():
        print('func2 멤버 처리 : 내부 함수')
    #func2() # 빠져나오기
func1() # 빠져나오기

print()
print('--공부하기 4 ()--')
def swap(a, b):
    return b, a # tuple로 반환

a = 10; b = 20
c = swap(a, b)
print(c) # (20, 10)
print(c[0], c[1]) # 20 10

print()
print('중요')
print('--공부하기 5 (if 조건식 안에 함수 사용)--')
def isOdd(arg):
    return arg % 2 == 1 # 홀수

mydict = {x:x * x for x in range(11) if isOdd(x)} # dict로 반환, if의 조건으로 함수를 넣었음
print(mydict)

print()
print('********** 현재 파일(모듈)의 객체 목록 **********')
# print(dir(__builtins__)) # 내장영역에 있는 객체의 목록
print('현재 파일(모듈)의 객체 목록 : ', globals())

print()
print('프로그램 종료')
















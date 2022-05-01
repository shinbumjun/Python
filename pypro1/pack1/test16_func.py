'''
중요 : 일금함수 지원 성립 조건

3가지를 만족하면
함수 안에 함수를 선언
인자로 함수를 전달
반환값이 함수인 경우
'''
# from boto.pyami.startup import su
print('개념 익히기')
def func1(a, b):
    return a + b

print('주소를 치환')
func2 = func1 
print(func1(2, 3)) # 5
print(func2(2, 3)) # 5

print()
print('1급함수 성립 조건')
def func3(f): # 매개변수로 함수
    def func4(): # 내부함수
        print('나는 내부함수야~~~')
    func4()
    return f # 반환값이 함수 (리턴 값이 함수)

mbc = func3(func1) # f-> finc1
print(mbc(2, 3))

print()
print('--- 람다(lambda)함수 - 축약함수 : 이름이 없는 한 줄 짜리 함수 ---')
# def를 쓸 정도로 복잡하지 않거나, def를 쓸 수 없는 곳에 사용, 극히 일부의 영역에서만 사용
# 형식 : lambda 인자, ... : 표현식 <== return 없이 결과를 반환 
def Hap(x, y):
    return x + y

print(Hap(1, 2)) # 3

print('람다로 표현')
print((lambda x, y:x + y)(1, 2)) # 3, 1회용

g = lambda x, y:x * y
print(g(3, 4)) # 12
imsi = g(3, 4)
print(imsi) # 12

print()
print('람다도 가변인수를 사용할 수 있다 (함수기 떄문에)')
kbs = lambda a,su=10:a + su
print(kbs(5)) # 15
print(kbs(5, 6)) # 11

sbs = lambda a, *tu, **di:print(a, tu, di)
sbs(1, 2, 3, m=4, n=5) # 1 (2, 3) {'m': 4, 'n': 5}

print()
print('list안에 람다를 이용')
li = [lambda a,b:a + b, lambda a, b:a * b]
print(li[0](3, 4)) # 7
print(li[1](3, 4)) # 12

print()
print('다른 함수안에 람다를 이용')
# filter(함수, sequence 자료)
print(list(filter(lambda a:a < 5, range(10)))) # [0, 1, 2, 3, 4], 1~9에서 5미만
print(list(filter(lambda a:a % 2, range(10)))) # [1, 3, 5, 7, 9], 2로 나웠을때 1은 True 그러므로 홀수 
print(list(filter(lambda a:a % 5 == 0 or a % 7 ==0, range(1, 101)))) # 0의 배수 또는 7의 배수 전부다















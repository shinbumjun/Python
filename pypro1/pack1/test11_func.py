'''
function : 자원의 재활용 가능. 여러 개의 수행문을 하나의 이름으로 묶은 실행 단위이다
사용자 정의 함수 형식 : def 함수명(para...): ~~
내장 함수 : maker가 제공하는 함수
'''
print('표준 출력장치로 데이터를 출력하는 내장 함수')
print(sum([3, 5, 7])) # 15
print(bin(8)) # 0b1000
print(int(1.7), float(2), str(5)+ '5') # 1 2.0 55
a = 10
b = eval('a + 5')
print(b) # 15

print(all([True, False])) # False : 전부다 True이면 True
print(any([True, False])) # True : 하나라도 True면 True

print()
a = [1, 3, 2, 5, 7, 6]
res = all(i < 10 for i in a)
print('모든 숫자가 10 미만이냐', res) # 모든 숫자가 10 미만이냐 True

print()
x= [1, 2, 3]; y = ['a', 'b']
for i in zip(x, y):
    print(i)
# (1, 'a')
# (2, 'b')


print()
print(round(1.2), round(1.6)) # 1 2

import math # 외장함수 : math.py -> math.xxx
print(math.ceil(1.2), math.ceil(1.6)) # 2 2 : 올림
print(math.floor(1.2), math.floor(1.6)) # 1 1
print(math.pi)  # 3.141592653589793 : 전역변수가 값을 가지는것(필드) 




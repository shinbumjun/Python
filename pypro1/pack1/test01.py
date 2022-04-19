'''
여러 줄 
주석
'''

"""
여러 줄 
주석 
"""
# 한 줄 주석 

print("환영합니다. python 세상")
print('환영합니다. "python" 세상')
a = "안녕" # 객체의 주소를 기억. 참조형 기억 장소
a = '반가워' 
a = 10; b =20.5 #구분할 때는 ;작성
c = b # 주소 치환
print(a, b, c)
print(id(a), id(b), id(c))
a = 10
b = 10
print(a == b, a is b) # == 값 비교 연산자, is 주소 비교 연산자
aa = [10]
bb = [10]
print(aa == bb, aa is bb) # 같은 값을 가지고 있지만 

print()

A = 1; a = 2
print(A, a, id(A), id(a)) # 대, 소문자 기억

import keyword
print('예약어 : ', keyword.kwlist) # 예약어를 변수명으로 사용하면 안된다
# 예시 for = 3

print()

print('자료형 확인') 
print(3, type(3)) # int 정수
print(3.4, type(3.4)) # float 실수
print(3 + 4j, type(3+4j)) # complex 복소수
print(True, type(True)) # bool
print('kbs', type('kbs')) # str 문자열

print()
print('***중요')

print((1,), type((1,))) # tuple 소괄호
print([1], type([1])) # list 대괄호
print({1}, type({1})) # set 중괄호
print({'key':1},type({'key':1})) # dict json타입
























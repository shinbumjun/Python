'''
함수 : 실인수(매개변수)와 가인수의 매핑 

매개변수의 유형
위치 매개변수(순서), 기본값 매개변수(값), 키워드 매개변수(이름), 가변 매개변수
'''
print('구구단')
def showGugu(start, end = 5):
    for dan in range(start, end + 1): # (2, 3) 3에 +1했기 때문에 3단까지 찍힘
        print(str(dan) + '단 출력')
        
showGugu(2, 3) # 값 넣고 빠져나오기
# 구구단
# 2단 출력
# 3단 출력

print()
showGugu(3) # start 값만 넣기, end = 5
# 3단 출력
# 4단 출력
# 5단 출력

print()
print('키워드 매개변수')
showGugu(start = 2, end = 3)

print()
print('순서 매개변수')
showGugu(end = 3, start = 2)

print()
print('값, 키워드 매개변수')
showGugu(2, end = 3)

print()
print('에러')
# showGugu(start = 2, 3)
# showGugu(end = 3, 2) # 2번째 인자에 상수값x

print()
print('가변 매개변수')
def func1(*ar): # 갯수 상관없을 때는 -> *패킹연산자
    print(ar)
func1('김밥') # ('김밥',) 튜플로 받음
func1('김밥', '비빔밥') # ('김밥', '비빔밥')
func1('김밥', '비빔밥', '볶음밥') # ('김밥', '비빔밥', '볶음밥')

print()
print('')
def func2(a, *ar):
    print(a)
    for i in ar:
        print('배고프면', i)
        
func2('김밥') 

print()
func2('김밥', '비빔밥') 

print()
func2('김밥', '비빔밥', '볶음밥')

print()
print('sum, mul 사용하기')
def process(choice, *ar):
    if choice == 'sum':
        res = 0
        for i in ar:
            res += i
    elif choice == 'mul':
        res = 1
        for i in ar:
            res *= i
    return res

print(process('sum', 1, 2, 3, 4, 5)) # 15
print(process('mul', 1, 2, 3, 4, 5)) # 120
print(process('mul', 1, 2, 3)) # 6

print()
print('-- **두개 이용해보기, ** : dict 타입 --')
def func3(w, h, **other):
    print('몸무게: {}, 키: {}'.format(w, h)) # 몸무게: 66, 키: 177
    print(other) # {}
    
func3(66, 177) # 값 넣고 빠져나오기

print()
print('-- 잘 알아두기 - dict로 변환 --')
func3(66, 177, irim='지구인', nai = 22) 
# 몸무게: 66, 키: 177
# {'irim': '지구인', 'nai': 22}

print()
func3(66, 177, irim='한국인')
# 몸무게: 66, 키: 177
# {'irim': '한국인'}

print()
print('')
def func4(a, b, *v1, **v2):
    print(a, b)
    print(v1)
    print(v2)
func4(1, 2)

print()
func4(1, 2, 3, 4, 5)
func4(1, 2, 3, 4, 5, m=6, n=7) # 값, 튜플, dict








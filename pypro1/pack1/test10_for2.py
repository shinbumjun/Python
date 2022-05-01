'''
반복문 for와 range()
range(초기치, 목적치, 증가치) : 수열 생성 함수
for문에서 많이 사용함 

n-gram : 문자열에서 n개의 연속된 요소를 추출
'''
print(list(range(1, 6, 1))) # [1, 2, 3, 4, 5]
print(list(range(1, 6))) # [1, 2, 3, 4, 5]
print(set(range(1, 6))) # {1, 2, 3, 4, 5}
print(tuple(range(1, 6))) # (1, 2, 3, 4, 5)

print()
print(list(range(6))) # 숫자하나만 입력하면 목저치 [0, 1, 2, 3, 4, 5]
print(list(range(0, 6))) # [0, 1, 2, 3, 4, 5]
print(list(range(1, 11, 2))) # [1, 3, 5, 7, 9]
print(list(range(-10, -100, -20))) # [-10, -30, -50, -70, -90]

print()
print('2단')
for i in range(1, 10): # java : for(int i=1; i <= 10; i++){}
    print('{0}*{1}={2}'.format(2, i, i*2), end = ' ')

print()
print()
tot = 0
for i in range(1, 11):
    tot += i
    
print('합은 ' + str(tot)) # 합은 55
print('합은 ' + str(sum(range(1, 11)))) # 합은 55, 지금은 내장함수 공부가 아니라 for문 공부

"""
파이썬이 좋은 이유 : 무료로 된 lib가 많아서 사용 범위가 넓다 (데이터 분석)
데이터 분석을 하기 위해서 파이썬을 배운다
"""

print()
# 참고 : n-gram : 문자열에서 n개의 연속된 요소를 추출
# 문자 단위 2 - gram
text = 'hello'

for i in range(len(text)):
    print(text[i:i+2]) # 바로 다음 글자를 이어서 반복적으로
    # print(text[i:i+3]) 

print()
# 단어 단위
text = 'this is python program'
words = text.split()
print(words) # ['this', 'is', 'python', 'program']

for i in range(len(words) -1):
    print(words[i], words[i + 1])
# this is
# is python
# python program

print()
print('문1) 2 ~ 9단 모두 출력')
print('for문')
for dan in range(2, 10):
    for n in range(1, 10):
        print('{0} * {1} = {2}'.format(dan, n, n*dan))

print()
print('while문')
i = 2
while i <= 9:
    j = 1
    while j <= 9:
        print('{0} * {1} = {2}'.format(i, j, i*j))
        j += 1
    i += 1
    
    
print()
print('문2) 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합 출력')
i = list(range(1, 101))
hap = 0
for a in i:
    if a % 3 == 0 and a % 5 == 0:
        hap += a
print(hap)

print()
print('문3) 주사위를 두 번 던져서 나 온 숫자들의 합이 4의 배수가 되는 경우만 출력')
# 예) 1 3
# 예) 2 2
# ...
for a in range(1,7):
    for b in range(1, 7):
        if(a + b) % 4 ==0:
            print('a+b=4의 배수인 경우:' + str(a)+ ' ' + str(b))


















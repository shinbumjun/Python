'''
if문 사용해보기
'''

var = 5
if var >= 3:
    print('크구나')
    print('참일 때 수행')
print('end1')

print()
if var >= 3:
    #print('크구나2')
    pass # 참이여도 pass
else:
    print('작구나2')
print('end2')

print()
money = 1000
age = 23
if money >= 500:
    item = 'apple'
    if age <= 30:
        msg = 'young'
    else:
        msg = 'old'
else:
    item = 'orange'
    if age > 20:
        msg= 'man'
    else:
        msg ='child'
       
print(item, msg) # apple young

print()
jum = 70
# jum = int(input('점수 입력 :')) # 키보드로 입력 받는다 (정수)
# print(jum, type(jum))
res = ''

if jum >= 90:
    res = 'a'
elif jum >= 70:
    res = 'b'
else:
    res = 'c'
print('res :' + res) # res :b

print()
if 90 <= jum <= 100:
    res = 'a'
elif 70 <= jum < 90:
    res = 'b'
else:
    res = 'c'
print('res :', res) # res : b

print()
print('in:포함')
names = ['정화', '재이', '일환']
print(names[0]) # 정화
if '재이' in names:
    print('친구야~')
else:
    print('누구?')

print()
print('조건부 표현식')
a = 'kbs'
b = 9 if a =='kbs' else 11 # 9가 11을 가질 수도 있음 
print(b) # 9

print()
a = 11
b= 'mbc' if a == 9 else 'kbs' # 이건 자주 사용
print(b) # kbs

print()
print('')
a = 3
if a < 5:
    print(0) # 0
elif a < 10:
    print(1)
else: 
    print(2)

print(0 if a < 5 else 1 if a < 10 else 2) # 0 이건 자주 사용하지는 않음

print()
a = 3
res = a * 2 if a > 5 else a + 2
print(res) # 5

print((a + 2, a * 2)[a > 5]) # a값이 3 이라서 거짓인 0이 찍혀서 a+2로 5가 찍힘








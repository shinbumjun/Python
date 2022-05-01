'''
[중요] 
반복문 for : 형식)for target in 묶음형 object: ...
p.140 ~ 145

리스트 컴플레이션
너무 길게 사용하면 가독성이 떨어짐, 적당히 사용
'''

for i in [1,2,3,4,5]:
    print(i, end= ' ') # 1 2 3 4 5 
    
print()

for _ in [1,2,3,4,5]:
    print('반복') # 횟수만큼 반복

print()

for i in (1,2,3,4,5): # 튜블은 순서가 있다
    print(i, end= ' ')

print()

for i in {1,2,3,4,5}: # set은 순서가 없다
    print(i, end= ' ')

print()
soft = {'java':'웹용', 'python':'만능', 'oracle':'디비'}
for i in soft.items(): 
    print(i, end= ' ')
    print(i[0], i[1])

print()
for i in soft.keys():
    print(i, end= ' ') # java python oracle 

print()
for i in soft.values():
    print(i, end= ' ') # 웹용 만능 디비 

print()
print()
for k, v in soft.items():
    print(k)
    print(v)

print()
print('enumerate 내장함수 : 인덱스도 얻을 수 있음')
li = ['a', 'b', 'c'] # list타입
for idx, data in enumerate(li):
    print(idx, ')', data)

print()
print('2단, 3단')
for n in [2,3]:
    print('--{}단--'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{0}*{1}={2}'.format(n, i, i * n))

print()
datas = [1,2,3,4,5]
for i in datas:
    if i == 2: continue # 자기와 대응되는 for문으로 올라감
    if i == 4: break # 4일때 강제종료
    print(i, end = ' ')
else:
    print('정상 종료일 때 수행')

print()
print('70점 이상만 합격')
jumsu = [95, 70, 60, 50, 100]
number = 0
for jum in jumsu:
    number += 1
    if jum < 70:continue # 아래로 내려오지 말고 위로
    print('%d번은 합격'%number) # 1, 2, 5번은 합격

print()
print('for문으로 더하기')
li1 = [3, 4, 5]
li2 = [0.5, 1, 2]
result = []
for a in li1:
    for b in li2:
        # print(a + b, end = ' ') # 3.5 4 5 4.5 5 6 5.5 6 7 
        result.append(a + b)
print(result) # [3.5, 4, 5, 4.5, 5, 6, 5.5, 6, 7]
        
print()
print('리스트 컴플레이션 연습할 예정')        
datas = [a + b for a in li1 for b in li2]
print(datas)
     

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        













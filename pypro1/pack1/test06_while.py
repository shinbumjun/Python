'''
# 반복문 : while 조건
조건이 참이면 수행 거짓이면 탈출 

continue
break

겹치지만 않으면 블럭이 블럭을 포함할 수 있다
'''
a = 1

while a <= 5:
    print(a, end = ' ') # 1 2 3 4 5
    a = a + 1
    # break
    
print('while 종료')

print()
print('while 블럭안에 while')
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i:' + str(i) + ', j:' + str(j))
        j += 1
    i += 1

print('\nwhile 종료2')

print()
print('1 ~ 100 사이의 정수 중 3의 배수의 합')
i = 1; hap = 0
while i <= 100:
    # print(i, end = ' ') # 1 ~ 100까지
    if i % 3 == 0:
        # print(i, end = ' ') # 3의 배수 ~ 100까지
        hap += i
    i += 1
    
print('합은 ', hap) # 합은  1683
    
print()
colors = ['r', 'g', 'b']
print(len(colors)) # 3
a = 0
while a < len(colors):
    print(colors[a], end = ':') # r:g:b:
    a += 1
    
print()
while colors:
    print(colors.pop()) # pop은 추출
    
print(len(colors))

print()
print('*찍기')
i = 1
while i <= 10:
    j = 1
    res = ''
    while j <= i:
        res = res + '*'
        j += 1
    print(res)
    i += 1
















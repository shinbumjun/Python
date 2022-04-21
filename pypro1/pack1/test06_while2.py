'''
while문 문제
'''
# from conda.common._logic import FALSE, TRUE

# 문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
i = 1; j = 0
while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
    #if i % 2 and i % 3 == 0:
        j += i 
    i += 1
print('합은' , j) # 867


print()
# 문2) 2 ~ 5 까지의 구구단 출력
i = 2
while i <= 5: 
    j = 1
    while j <= 9:
        print(str(i) + ' x ' + str(j), '=' , int(i*j))
        j += 1
    i += 1


print('한번 더 보기')
# 문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 합을 출력
i = -1
hap = 0
while True:
    hap += i
    if i < 0:
        i = i*(-1)+2
    else:
        i = i*(-1)-2
    if i == -101:
        break
    
print('합은', hap)

print()
# 문4) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
aa = 2; count = 0
while aa<= 1000:
    imsi = False
    bb = 2
    while bb <= aa -1:
        if aa % bb == 0:
            imsi = True
        bb += 1
    
    if imsi == False:
        print(aa, end = ' ')
        count += 1
    
    aa += 1
print('갯수 : ', count)



















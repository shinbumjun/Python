'''
# while : continue, break
# 난수 : 정의된 범위 내에서 무작위로 추출
'''
a = 0

while a < 10:
# while True: # 무한 루프
# while 1: # 무한 루프...
# while 11.5:
# while -1.5:
    a += 1
    if a == 5:continue
    if a == 7:break # 7만나면 탈출
    print(a)
else:
    print('while 처리') # 정상적으로 종료가 되면 출력

print('while 수행 후 a : %d'%a)

# 난수 : 정의된 범위 내에서 무작위로 추출
import random
random.seed(12) # 12번째 난수 숫자
print(random.random()) # 실수
print(random.randint(1, 10)) # 1~10 숫자

# 임의의 숫자 알아 내기 
num = random.randint(1, 10)
while True: # 무한 루프에 빠트려 놓고 작업을 할 때도 있음 
    print('1 ~ 10 사이의 컴이 가진 예상 숫자 입력:')
    guess = int(input()) # 키보드 값을 받음 
    
    if guess == num:
        print('성공~~' * 10)
        break
    elif guess < num:
        print('더 큰 수 입력')
    elif guess > num:
        print('더 작은 수 입력')












'''
반복문 for
아침에 배운 정규표현식과 for문 이용해보기
'''

# 웹에서 읽은 자료라 가정 : 단어 수 출력 ex) 모터를:3

ss= """하이브리드차는 내연기관과 배터리로 움직이는 모터를 동시에 탑재한 차량이다. 
엔진이 아예 없는 전기차와 가장 큰 차이점은 충전할 필요가 없다는 점이다. 
이런 분위기 속에 한때 수입 하이브리드차의 대표 주자였던 렉서스 ES300h에 대한 관심도 높아지고 있다. 
렉서스 ES300h는 여러 차례 월 기준 수입차 판매 1위를 차지했을 정도로 인기가 많았다. 
ES300h는 최근 많이 출시되고 있는 마일드 하이브리드 차량과 달리 배터리(모터)만으로 차량 구동이 가능한 정통 하이브리드차다. 
마일드 하이브리드는 내연기관 차량에 48볼트(V) 배터리와 모터를 추가 장착한 형태로 전기모터만으로는 차량 구동이 불가능하다. 
엔진이 중심이 되고 모터와 배터리는 주행 효율을 높여주는 수준의 하이브리드라는 의미다.
엔진이 중심이 되고 모터와 배터리는 주행 효율을 높여주는 수준의 하이브리드라는 의미다.
엔진이 중심이 되고 모터와 배터리는 주행 효율을 높여주는 수준의 하이브리드라는 의미다."""

import re
ss2 = re.sub(r'[^가-힣\s]', '', ss) # 한글과 공백을 제외하고 없애기
print(ss2)

ss3 = ss2.split(sep=' ') # list 타입으로 반환
print(ss3) 
print(len(ss3)) # 숫자
print(len(set(ss3))) # 숫자 (set 중복 불가)

# 어떤 값이 들어오냐에 따라 set, dict
cou = {} # 단어의 발생 횟수를 dict로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1 # {'키':i}
print(cou)

# 워드 클라우드 차트

print()
print('전화번호 확인하기')
for test in ['111-1234', '일이삼-사오육칠', '2222-3333']:
    if re.match(r'^\d{3,4}-\d{4}$', test):
        print(test)
    else:
        print('전화번호 아니야')

print()
a = 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li) # [2, 4, 6, 8, 10]

print(list(i for i in a if i % 2 == 0)) # [2, 4, 6, 8, 10]

print()
datas = [1, 2, 'a', True, 3.4]
li = [i for i in datas if type(i) == int ] # datas을 i에 넣는다 그 타입이 int인지? 
print(li) # [1, 2]

print()
datas = {1,1,2,2,3}
se = {i * i for i in datas} # datas를 i에 (in)하고 i*i하기, set는 중복 불가
print(se) # {1, 4, 9}

print()
print('키와 밸류를 뒤집어 놓음')
id_name = {1:'tom', 2:'james'}
name_id = {value:key for key, value in id_name.items()}
print(name_id) # {'tom': 1, 'james': 2}

print()
print('변환')
temp = [1,2,3]
for i in temp:
    print(i, end = ' ') # 1 2 3 
print()
print([i for i in temp]) # [1, 2, 3] list 타입
# print((i for i in temp)) # 튜플은 안됨
print({i for i in temp}) # {1, 2, 3} set 타입

print()   
print('중요 : 과일 값 계산')
price = {'사과':2000, '오렌지':1000, '배':3000}        
guest = {'사과':2, '배':1}    
bill = sum(price[f] * guest[f] for f in guest) # sum(요소들) : 합을 구하는 내장 함수
print(bill)










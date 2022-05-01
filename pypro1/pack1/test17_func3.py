'''
풀이
'''
def inputfunc():
    tmp = 1
    while True:
        print('사번,이름,기본급,입사년도를 입력하세요')
        # 문자열을 이쁘게 나눠서 리스트로 만들때 사용하는 함수 - 문자열.split()
        data = list(input().split(",")) 
        processfunc(data)
        
        yn = input('계속 하시겠습니까? y/n : ')
        if yn == 'y':
            tmp +=1
            continue
        else:
            print('처리한 건수 : {}건'.format(tmp))
            break
        

def processfunc(data):
    num,name,income,year = data # 왜 반대로?
    a = 2022 - int(year)
    bonus = 0 # 보너스(근속수당)
    tax= 0 # 공제 세율
    if a>=9:
        bonus = 1000000
    elif a>=4:
        bonus = 450000
    else:
        bonus = 150000
               
    total = int(income)+bonus # 총금액 = 기본급 + 보너스
    if total >= 3000000: # 300만원 이상
        tax=0.5 # 공제 세율 0.5
    elif total >= 2000000: # 200만원 이상
        tax=0.3 # 공제 세율 0.3
    else: # 200만원 미만
        tax= 0.15 # 공제 세율 0.3
    
    # 사번, 이름 기본급, 근무년수, 근속수당, 공제액, 수령액
    print('사번:{} 이름:{} 기본급:{} 근무년수:{}년 근속수당:{}원 공제액:{}원 수령액:{}원'.format(num,name,income,a,bonus,int(total*tax),int(total-total*tax)))

# 1,신범준,1000000,2021 입력시
# 1,150,000원(총액) - 172,500(공제액) = 977,500원(수령액)
inputfunc()
    
    









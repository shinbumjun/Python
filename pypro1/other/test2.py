'''
1 ~ 100 사이의 정수 중에서 5의 배수의 합을 출력하는 소스 코드를 작성하시오.
이 때 func 라는 이름의 함수를 만들고, 함수 내에서 반복문 for를 사용하시오.
5의 배수의 합은 return 문을 사용하도록 한다
'''

j = list(range(1, 101))
hap = 0
def func(): 
    for i in j:
        
        if i % 5 == 0:
            hap += i
        return hap





























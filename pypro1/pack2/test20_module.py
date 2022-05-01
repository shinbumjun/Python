'''
2. 사용자 정의 모듈 작성 및 읽기
우리가 만든다음 읽어오기

중요 : 실행하는 파일이 main이다

# 패쓰가 걸려있는 폴더 (C:\anaconda3\Lib에 존재하는 파일)
# window -> Preferences -> Libraries(패쓰 확인 하는법) -> 서브party는 site-packager에 넣자!
'''
a = 10
print(a + 10)

print('작업을 하다가 외부 모듈 읽기')
# mymod1, mymod2, mymod3 사용하기

print(dir()) # 현재 모듈 종류

list1 = [1, 3]
list2 = [2, 4]
# listHap(list1, list2) # 그냥은 mymod1를 못씀, 에러

print()
print('----- 같은 패키지에 있더라도 패키지명.모듈명 -----')
import pack2.mymod1 # 방법1
pack2.mymod1.listHap(list1, list2) # ([1, 3], [2, 4])
# print(dir())

print()
print('중요 : 실행하는 파일이 main이다')
def listTot(*ar):
    print(ar)
    
    if __name__ == '__main__': 
        print('이 파일이 메인임을 선언하노라~~~')

listTot(list1, list2)

print()
from pack2.mymod1 import kbs # 방법2
kbs()

from pack2.mymod1 import mbc, price
mbc()
print('price : ', price)

print()
print('----- 다른 패키지 -----')
import other.mymod2
print(other.mymod2.Hap(5, 3)) # 8

from other.mymod2 import Cha
print(Cha(5, 3)) # 2

print()
# 패쓰가 걸려있는 폴더 (C:\anaconda3\Lib에 존재하는 파일 - mymod3)
# window -> Preferences -> Libraries(패쓰 확인 하는법) -> 서브party는 site-packager에 넣자!
import mymod3
print(mymod3.Gop(5, 3)) # 15

from mymod3 import Nanugi
print(Nanugi(5, 3)) # 1.6666666666666667









































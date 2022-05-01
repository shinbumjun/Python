'''
추상 클래스 : 추상 메소드를 하나라도 가지고 있는 경우 대체적으로 추상 클래스라고 한다

추상클래스는 자식이 풀어줘야지 객체로 만들어 질 수 있다

다형성을 목적으로 만든다

'''
from abc import *

# 내용은 없고 이름만 있다, 추상클래스는 자식이 풀어줘야지 객체로 만들어 질 수 있다

class AbstractClass(metaclass = ABCMeta): # 추상 클래스, metaclass = ABCMeta 가독성을 위해서 명시적으로 작성, ***빼면 안됨
    @abstractclassmethod
    def abcMethod(self): # 추상 메소드
        pass

    def normalMethod(self): # 일반 메소드
        print('추상 클래스 내의 일반 메소드')

# aa = AbstractClass() # 추상 클래스는 객체로 만들수 없다, 부모로만 의미
# 에러 TypeError: Can't instantiate abstract class AbstractClass with abstract method abcMetho

class Child1(AbstractClass): # 추상클래스 상속, 오버라이드를 해야 객체가 만들어 질수 있다
    name = '난 Child1'
    
    def abcMethod(self): # 추상 클래스의 파생 클래스는 반드시 추상 메소드를 재정의. 강제. (다형성을 구상하려고)
        print('추상메소드를 오버라이딩')
    
c1 = Child1() # 부모의 족쇄를 풀지않으면 객체가 만들어지지않는다 -> 추상메소드를 오버라이딩하면 객체로 만들어짐
print(c1.name) # 출력) 난 Child1
c1.abcMethod() # 출력) 추상메소드를 오버라이딩
c1.normalMethod() # 출력) 추상 클래스 내의 일반 메소드

print()
class Child2(AbstractClass):
    
    def abcMethod(self): # 오버라이딩을 강요 당함 (추상메소드)
        a = 10
        b = 20
        # ...
        print('추상메소드를 오버라이딩 해서 마법에서 풀림 ㅎㅎ')

    def normalMethod(self): # 오버라이딩이 선택적 (메소드)
        print('부모 클래스의 메소드를 다시 정의함')

c2 = Child2()
c2.abcMethod() # 출력) 추상메소드를 오버라이딩 해서 마법에서 풀림 ㅎㅎ
c2.normalMethod() # 출력) 부모 클래스의 메소드를 다시 정의함

print('----- 다형성 -----')
mbc = c1
mbc.abcMethod() # 출력) 추상메소드를 오버라이딩
print()
mbc = c2
mbc.abcMethod() # 출력) 추상메소드를 오버라이딩 해서 마법에서 풀림 ㅎㅎ

'''
https://cafe.daum.net/flowlife/RUrO/24
4번 문제 (월요일)
'''





















'''
***** 한번 더 보기 *****
메소드 오버라이드 : 다형성
단일 상속
'''
# Parent의 자식 클래스는 printData 오버라이드하길 바랄게~
class Parent:
    def printData(self):
        pass

class Child1(Parent):
    def printData(self): # 오버라이드
        print('Child1에서 override') # 부모랑 다른 정보
        
class Child2(Parent):
    def printData(self): # 오버라이드
        print('Child2에서 재정의')
        print('부모 메소드와 이름은 같으나 기능이 다름')
        
    def abc(self):
        print('Child2 고유 메소드')

c1 = Child1()
c1.printData() # Child1에서 override

print()
c2 = Child2()
c2.printData()
# Child2에서 재정의
# 부모 메소드와 이름은 같으나 기능이 다름

c2.abc() # Child2 고유 메소드

print('\n----- 다형성 (동일하지만 다르다) -----')
# par = Parent() # 부모 객체 변수 만들고, 자바에서는 이렇게 사용하지만 파이썬은 생략가능 
par = c1 # 부모객체에 자식의 주소를 넘김
par.printData() # Child1에서 override

print()
par = c2
par.printData()
# Child2에서 재정의
# 부모 메소드와 이름은 같으나 기능이 다름

print()
par.abc() # Child2 고유 메소드

print()
plist = [c1, c2] # 둘다 실행됨
for a in plist:
    a.printData()


















